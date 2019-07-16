import csv
from io import StringIO
from django.http import HttpResponse, StreamingHttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime, timedelta
from datetime import date
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from operator_form.models import Post

from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (TemplateView, ListView)

# Create your views here.
class Home(TemplateView):
    template_name = 'admin_form/a_login.html'
    redirect = '/admin_user_profile/'

@method_decorator(login_required, name='dispatch')
class AdminUserProfile(TemplateView):
    template_name = 'admin_form/a_loggedin.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(AdminUserProfile, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        context['total_accounts'] = User.objects.all().count
        context['total_actice_accounts'] = User.objects.filter(
            Q(is_active=True)
        ).count
        context['total_forms'] = Post.objects.all().count
        context['total_user_forms'] = Post.objects.filter(
                Q(published_date__lte=timezone.now()) &
                Q(published_date__gte=(timezone.now()-timedelta(6))) &
                Q(author=self.request.user)
            ).count
        return context

# class UserPostList(ListView):
#     template_name = 'admin_form/u_post_list.html'
#     model = Post

#     def get_queryset(self):
#         return Post.objects.filter(
#             Q(published_date__lte=timezone.now()) &
#             Q(author=self.request.user)
#         )

class UserParam(ListView):
    template_name = 'admin_form/u_post_list.html'
    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        # print(self.request.GET)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(author = self.request.GET.get('q',''))
        return qs
class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

class UserParamDownload(ListView):
    template_name = 'admin_form/success_download.html'
    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get('q', None)
        print(query)
        contents =[]
        qf = qs.filter(author = self.request.GET.get('q',''))
        # with open('new_result.csv', 'w', encoding='utf-8') as csvfile:
        #     for item in qf:
        #         writer = csv.writer(csvfile)
        #         writer.writerow([item.author,item.published_date,item.file_no,item.record_no,item.entry_date,item.ref_no,item.invoice_no,item.courier_name,item.con_no,item.dispatch_date,item.dispatch_by,item.sales_date,item.sales_time,item.customer_name,item.mail_address,item.agent_name,item.address,item.city,item.state,item.zip_code,item.customer_phone,item.credit_card_type,item.credit_card_number])
        #         print(item.file_no,item.record_no)
        if query is not None:
            qs = qs.filter(author = self.request.GET.get('q',''))
            # print(qs.values)
        return (qs)
    
    def download_view(request, *args, **kwargs):
        # Create the HttpResponse object with the appropriate CSV header.
        
        qs = Post.objects.all()
        qf = qs.filter(author = request.GET.get('q',''))

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="user_data.csv"'
        for item in qf:
                writer = csv.writer(response)
                writer.writerow([item.author,item.published_date,item.file_no,item.record_no,item.entry_date,item.ref_no,item.invoice_no,item.courier_name,item.con_no,item.dispatch_date,item.dispatch_by,item.sales_date,item.sales_time,item.customer_name,item.mail_address,item.agent_name,item.address,item.city,item.state,item.zip_code,item.customer_phone,item.credit_card_type,item.credit_card_number])

        return response


# def display_data(self):
#     # templet_name = 'admin_form/u_post_list.html'
#     return redirect("admin_user_profile",str(print('how are you?')))

# class AdminUserData(ListView):
#     template_name = 'admin_form/a_loggedin.html'
#     model = User
#     def get_context_data(self, **kwargs):
#         context = super(AdminUserData, self).get_context_data(**kwargs)
#         context['test_list'] = User.objects.all()
#         print(context['test_list'])
#         context['test1'] = "hey"
#         print(context['test1'])

#         return context


# class UsersView(TemplateView):
#     template_name = 'admin_form/a_loggedin.html'

   

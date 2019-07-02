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
    def get_queryset(self):
        return Post.objects.filter(
            Q(author = self.request.GET.get('q', ''))
        ) 


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

   

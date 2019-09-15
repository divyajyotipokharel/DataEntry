from datetime import datetime, timedelta
from datetime import date
from django.db.models import Q
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from operator_form.models import Post
from operator_form.forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,UpdateView,DeleteView)


from django.shortcuts import redirect
@login_required
# login in redirect options
def login_success(request):
    if request.user.is_superuser==True:
        # user is an admin
        return redirect("admin_user_profile")
    else:
        return redirect("user_profile")

# Create your views here.
class About(TemplateView):
    template_name = 'about.html'
class Home(TemplateView):
    template_name = 'index.html'

class UserProfile(TemplateView):
    template_name = 'operator_form/loggedin.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now(),author=self.request.user).order_by('-published_date')

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfile, self).get_context_data(*args, **kwargs)
        context['total_forms'] = Post.objects.filter(
                Q(published_date__lte=timezone.now()) &
                Q(published_date__gte=(timezone.now()-timedelta(6))) &
                Q(author=self.request.user)
            ).count
        
        context['day1'] = timezone.now().strftime('%d %b')
        day1_date = timezone.now().strftime('%Y-%m-%d')
        context['day1_data'] = Post.objects.filter(
                Q(published_date__date=day1_date) &
                Q(author=self.request.user)
            ).count
        print(context['day1'])
        context['day2'] = (timezone.now()-timedelta(1)).strftime('%d %b')
        day2_date = (timezone.now()-timedelta(1)).strftime('%Y-%m-%d')
        context['day2_data'] = Post.objects.filter(
                Q(published_date__date=day2_date) &
                Q(author=self.request.user)
            ).count
        context['day3'] = (timezone.now()-timedelta(2)).strftime('%d %b')
        day3_date = (timezone.now()-timedelta(2)).strftime('%Y-%m-%d')
        context['day3_data'] = Post.objects.filter(
                Q(published_date__date=day3_date) &
                Q(author=self.request.user)
            ).count
        context['day4'] = (timezone.now()-timedelta(3)).strftime('%d %b')
        day4_date = (timezone.now()-timedelta(3)).strftime('%Y-%m-%d')
        context['day4_data'] = Post.objects.filter(
                Q(published_date__date=day4_date) &
                Q(author=self.request.user)
            ).count
        context['day5'] = (timezone.now()-timedelta(4)).strftime('%d %b')
        day5_date = (timezone.now()-timedelta(3)).strftime('%Y-%m-%d')
        context['day5_data'] = Post.objects.filter(
                Q(published_date__date=day5_date) &
                Q(author=self.request.user)
            ).count
        context['day6'] = (timezone.now()-timedelta(5)).strftime('%d %b')
        day6_date = (timezone.now()-timedelta(3)).strftime('%Y-%m-%d')
        context['day6_data'] = Post.objects.filter(
                Q(published_date__date=day6_date) &
                Q(author=self.request.user)
            ).count
        context['day7'] = (timezone.now()-timedelta(6)).strftime('%d %b')
        day7_date = (timezone.now()-timedelta(3)).strftime('%Y-%m-%d')
        context['day7_data'] = Post.objects.filter(
                Q(published_date__date=day7_date) &
                Q(author=self.request.user)
            ).count

        return context

# for the working of form data
class PostList(ListView):
    template_name = 'operator_form/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            Q(published_date__lte=timezone.now()) &
            Q(author=self.request.user)
        )

class PostDetail(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'operator_form/post_detail.html'
    model = Post

class CreatePost(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'operator_form/post_detail.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'operator_form/post_detail.html'
    form_class = PostForm
    model = Post

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostListDraft(LoginRequiredMixin,ListView):
    login_url = '/login/'
    # redirect_field_name = 'operator_form/post_list_draft.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True, author=self.request.user).order_by('created_date')


# for the post to be published
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

# def showthis(request):
#     count= Book.objects.all().count()
#     context= {'count': count}
#     return render(request, 'operator_form/loggedin.html', context)

from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from operator_form.models import Post
from operator_form.forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.
class About(TemplateView):
    template_name = 'about.html'
class Home(TemplateView):
    template_name = 'index.html'

class UserProfile(TemplateView):
    template_name = 'operator_form/loggedin.html'
    model = Post

# for the working of form data
class PostList(ListView):
    template_name = 'operator_form/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now(),author=self.request.user).order_by('-published_date')

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
    redirect_field_name = 'operator_form/post_list_draft.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True, author=self.request.user).order_by('created_date')


# for the post to be published
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
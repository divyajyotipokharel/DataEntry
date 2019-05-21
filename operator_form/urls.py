from django.urls import path
from operator_form import views

urlpatterns = [
    path('',views.Home.as_view(), name = 'home'),
    path('profile/',views.UserProfile.as_view(), name = 'user_profile'),
    path('about/',views.About.as_view(), name = 'about'),

    path('post/all',views.PostList.as_view(), name = 'post_list'),
    path('post/<int:pk>/',views.PostDetail.as_view(), name = 'post_detail'),
    path('post/new/',views.CreatePost.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit/',views.PostUpdate.as_view(), name = 'post_edit'),
    path('post/<int:pk>/remove/',views.PostDelete.as_view(), name = 'post_remove'),
    path('post/drafts/',views.PostListDraft.as_view(), name = 'post_draft_list'),
    path('post/<int:pk>/publish/',views.post_publish, name = 'post_publish'),
    
]

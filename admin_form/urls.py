from django.urls import path
from admin_form import views

urlpatterns = [
    path('',views.Home.as_view(), name = 'admin_home'),
    path('profile/',views.AdminUserProfile.as_view(), name = 'admin_user_profile'),
    # path('operators/',views.UserPostList.as_view(), name = 'view_user_profile'),
    path('operator/',views.UserParam.as_view(), name = 'view_operator_profile'),

    # path('about/',views.About.as_view(), name = 'about'),
    # path('post/all',views.PostList.as_view(), name = 'post_list'),
    # path('post/<int:pk>/',views.PostDetail.as_view(), name = 'post_detail'),
    # path('post/new/',views.CreatePost.as_view(), name = 'post_new'),
    # path('post/<int:pk>/edit/',views.PostUpdate.as_view(), name = 'post_edit'),
    # path('post/<int:pk>/remove/',views.PostDelete.as_view(), name = 'post_remove'),
    # path('post/drafts/',views.PostListDraft.as_view(), name = 'post_draft_list'),
    # path('post/<int:pk>/publish/',views.post_publish, name = 'post_publish'),
]

from django.urls import path
from admin_form import views

urlpatterns = [
    path('',views.Home.as_view(), name = 'administrator_home'),
    path('profile/',views.AdminUserProfile.as_view(), name = 'admin_user_profile'),
    path('operator/',views.UserParam.as_view(), name = 'view_operator_profile'),
]

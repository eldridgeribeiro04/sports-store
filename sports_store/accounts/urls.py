from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

app_name= 'accounts'


urlpatterns = [
    path("create_user/", views.create_user, name="create_user"),
    
    path('change_details', views.edit_user, name="change_details"),
    
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
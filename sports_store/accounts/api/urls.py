from django.urls import path
from django.contrib.auth import views as auth_views

from rest_framework.authtoken.views import obtain_auth_token


from accounts.api import views

app_name= 'accounts'


urlpatterns = [
    path("create_user/", views.create_user, name="create_user"),
    path('login/', obtain_auth_token, name='login'),
    
    # path('change_details', views.edit_user, name="change_details"),
    # path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
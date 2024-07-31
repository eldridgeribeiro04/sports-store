from django.urls import path
from accounts.api import views

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('register/', views.CreateUserView.as_view(), name='create_user'),
]
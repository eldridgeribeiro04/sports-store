# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# from accounts.forms import CustomUserCreationForm

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout

# from django.views import View

### CREATING A REST API ###
###IMPORT API REQUIREMENTS ###
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from accounts.api.serializers import RegistrationSerializer
from rest_framework import status



# Create your views here.

def create_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(request.POST)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'User created successfully'
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
            
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)


# def edit_user(request):
#     if request.method == 'POST':
#         user = get_user_model().objects.get(pk=request.user.id)
#         user.username = request.POST['username']
#         user.email = request.POST['email']
#         user.save()
#         return redirect ("accounts/home")
#     else:
#         user = get_user_model().objects.get(pk=request.user.id)
#         form = CustomUserCreationForm(initial={
#             'username': user.username,
#             'email': user.email
#         })
#     return render(request, 'accounts/change_details.html', {'form': form})


# class CustomLogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('base:home')  # Redirect to home or any other page after logout

#     def post(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('base:home')

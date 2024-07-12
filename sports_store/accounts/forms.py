from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

from .models import MyUser


# Used to create a custom user. Next create manager.
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password1', 'password2')
        
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password')


# Create a user using the Django inbuilt User model
# class UserReg(forms.ModelForm):
#     password1 = forms.CharField(widget=forms.PasswordInput())
#     password2 = forms.CharField(widget=forms.PasswordInput())
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        
#     def clean(self):
#         cleaned_data = super().clean()
#         password1 = cleaned_data.get("password1")
#         password2 = cleaned_data.get("password2")
        
#         if password1 and password2 and password1 != password2:
#             self.add_error("password2" ,"Passwords must match")
            
#         return cleaned_data

from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .models import CustomUser

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Username', min_length=5, max_length=50)
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label="Last Name", max_length=50, required=False)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email")

    # def email_clean(self):
    #     email = self.clean_password2['email'].lower()
    #     new = self.objects.filter(email=email)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

                                                                               
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")
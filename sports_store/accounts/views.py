from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from accounts.forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views import View



# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect ("home")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/create_user.html', {'form': form})


def edit_user(request):
    if request.method == 'POST':
        user = get_user_model().objects.get(pk=request.user.id)
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        return redirect ("accounts/home")
    else:
        user = get_user_model().objects.get(pk=request.user.id)
        form = CustomUserCreationForm(initial={
            'username': user.username,
            'email': user.email
        })
    return render(request, 'accounts/change_details.html', {'form': form})


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('base:home')  # Redirect to home or any other page after logout

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('base:home')

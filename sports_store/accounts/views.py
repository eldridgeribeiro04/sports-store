from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import CustomUser
from django.shortcuts import get_object_or_404

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("login")
    template_name = "accounts/update.html"

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.kwargs.get('pk'))

    # def get_queryset(self):
    #     return CustomUser.objects.filter(id=self.request.user.id)


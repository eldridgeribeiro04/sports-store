from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

class MyUser(AbstractUser):
        username = models.CharField(_('Username'), max_length=100, unique=True)
        email = models.EmailField(_('Email'), max_length=100, unique=True)
        
        USERNAME_FIELD = "username"
        EMAIL_FIELD = "email"
        REQUIRED_FIELDS = ["email"]
        
        objects = CustomUserManager()
        
        def __str__(self):
                return self.username

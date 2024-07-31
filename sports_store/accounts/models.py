from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token


# Create your models here.

class MyUser(AbstractUser):
        REQUIRED_FIELDS = []
        
        def clean(self):
                super().clean()
                if not self.username and not self.email:
                        raise ValidationError(_('Username or email must be provided.'))
                if self.username and self.email:
                        raise ValidationError(_('Provide either username or email.'))
        
        objects = CustomUserManager()
        
        def __str__(self):
                return self.username

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomerUserChangeForm, CustomUserCreateForm
from accounts.models import CustomUser
# Register your models here.

class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]

admin.site.register(CustomUser, CustomerUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import MyUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = MyUser
        list_display = ("email", "username", "is_staff")
        list_filter = ("email", "username", "is_staff")
        fieldsets = (
            (None, {"fields": ("email", "username", "password")}),
            ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        )
        
        add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
        search_fields = ("email", "username")
        ordering = ("email",)

admin.site.register(MyUser, CustomUserAdmin)

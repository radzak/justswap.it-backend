# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from justswap.accounts.forms import UserChangeForm, UserCreationForm
from justswap.accounts.models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    """Admin configuration for User model."""

    fieldsets = (
        (None, {"fields": ("password", "username", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"fields": ("password1", "password2", "username", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "username", "is_active", "is_staff")
    list_editable = ("is_active",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "username")
    ordering = ("email", "username")

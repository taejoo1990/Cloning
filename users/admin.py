from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # users\models.py

# Register your models here.

# admin.site.register(models.User, CustomUserAdmin)
# !! i can code using either decorator(@admin.register) or class(admin.site.register(models.User, CustomUserAdmin))

# registrate user's model
# UserAdmin(django.contrib.auth.admin) provide basic form of display
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custon User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "super_host",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("super_host",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "super_host",
        "is_staff",
        "is_superuser",
    )


"""class CustomUserAdmin(admin.ModelAdmin) 
using admin.ModelAdmin let me custormize list_display


    CUSTOM USER ADMIN

    list_display = (
        "username",
        "gender",
        "email",
        "language",
        "currency",
        "super_host",
    )

    list_filter = (
        "super_host",
        "gender",
        "language",
        "currency",
    )"""

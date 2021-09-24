from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rooms import models as RoomsModel
from . import models  # users\models.py


# admin.site.register(models.User, CustomUserAdmin)
# !! i can code using either decorator(@admin.register) or class(admin.site.register(models.User, CustomUserAdmin))

"""class CustomUserAdmin(admin.ModelAdmin) 
using admin.ModelAdmin let me custormize list_display"""
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

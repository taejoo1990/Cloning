from django.contrib import admin
from . import models  # users\models.py

# Register your models here.
# sudo lsof -t -i tcp:8000 | xargs kill -9

# registrate user's model
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass

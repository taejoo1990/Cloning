from django.contrib.auth.models import AbstractUser
from django.db import models


# sudo lsof -t -i tcp:8000 | xargs kill -9
# AbstractUser Class provide Basic model(ex.ID,password...etc) and i will extend model :)
class User(AbstractUser):
    bio = models.TextField(default="")


# Create your models here.

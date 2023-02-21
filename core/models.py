from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Creating a User in Core app to decuple the core app from the bookings app.
class User(AbstractUser):
    email = models.EmailField(unique=True)
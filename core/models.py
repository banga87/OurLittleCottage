from django.contrib.auth.models import AbstractUser
from django.db import models

"""
Creating a User in Core app to decuple the core app from the bookings app.
Email UNIQUE constraint handled in serializers.py and admin.py
"""

class User(AbstractUser):
    email = models.EmailField(unique=True)
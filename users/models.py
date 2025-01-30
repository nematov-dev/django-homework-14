from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(blank=True, upload_to="users")

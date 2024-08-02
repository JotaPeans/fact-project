from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.CharField(max_length=2000)
    role = models.CharField(max_length=15)
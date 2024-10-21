from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company = models.CharField(max_length=100, blank=True, null=True)
    plan = models.CharField(
        max_length=50, choices=[("free", "Free"), ("pro", "Pro")], default="free"
    )

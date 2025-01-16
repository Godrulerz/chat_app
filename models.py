# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='chat_user_groups',  # Changed related_name to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='chat_user_permissions',  # Changed related_name to avoid clash
        blank=True
    )

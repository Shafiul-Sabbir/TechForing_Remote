from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    # Custom fields for my user model.
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Resolve the related_name clashes with django
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )
    
    class Meta:
        db_table = 'Custom Users'

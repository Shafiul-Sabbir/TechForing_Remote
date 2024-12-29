from django.db import models
from projects.models import Project
from users.models import CustomUser

# Create your models here.
class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)        
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


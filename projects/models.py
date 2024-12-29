from django.db import models
from users.models import CustomUser

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='owned_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

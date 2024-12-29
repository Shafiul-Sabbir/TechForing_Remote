from django.db import models
from users.models import CustomUser
from tasks.models import Task

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    task = models.ForeignKey(Task, on_delete = models.CASCADE, related_name = 'comments')
    created_at = models.DateTimeField(auto_now_add = True)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    desc = models.CharField(max_length=250)
    is_delete = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

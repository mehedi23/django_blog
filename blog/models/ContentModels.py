from django.db import models
from .Categorice import Categorice 
from account.models import User
from datetime import datetime

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='images/', blank=True)
    tittle = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    category = models.ManyToManyField(Categorice)
    create_at = models.DateTimeField(auto_created=True, default=datetime.now)

    def __str__(self):
        return self.tittle
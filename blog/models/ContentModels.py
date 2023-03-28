from django.db import models
from .Categorice import Categorice 

class Blog(models.Model):
    banner = models.ImageField(upload_to='images/')
    tittle = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=1000, default="")
    category = models.ManyToManyField(Categorice)

    def __str__(self):
        return self.tittle
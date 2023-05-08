from django.db import models
from account.models import User
from blog.models.ContentModels import Blog

# Create your models here.
class Likes(models.Model):
    post = models.ForeignKey(Blog, related_name='liked_post', on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name='liked_user')
from django.urls import path
from reactions.views import setLikes

urlpatterns = [
    path('likes/<int:blog_id>', setLikes, name='likes'),
]
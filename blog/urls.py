from django.urls import path
from blog.views import BlogDetailsView, AllBlogView

urlpatterns = [
    path('blogs/', AllBlogView.as_view(), name='blog'),
    path('blogs/<int:blog_id>', BlogDetailsView.as_view(), name='blog-details'),
]
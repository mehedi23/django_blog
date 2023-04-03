from django.urls import path
from blog.views import BlogDetailsView, AllBlogView, UserBlogList

urlpatterns = [
    path('blogs/', AllBlogView.as_view(), name='blog'),
    path('blogs/<int:blog_id>', BlogDetailsView.as_view(), name='blog-details'),
    path('user/blogs/', UserBlogList.as_view(), name='user-blogs')
]
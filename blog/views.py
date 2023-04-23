from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, pagination
from rest_framework.views import APIView
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from .models.ContentModels import Blog
from .models.Categorice import Categorice



class BlogDetailsView(APIView):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class AllBlogPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page_number'


class AllBlogView(APIView):
    pagination_class = AllBlogPagination

    def get(self, request):
        paginator = self.pagination_class()
        blog = Blog.objects.all()
        paginated_blog = paginator.paginate_queryset(blog, request)
        serializer = BlogSerializer(paginated_blog, many=True)

        return paginator.get_paginated_response(serializer.data)
    


class UserBlogList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blog = Blog.objects.filter(user = request.user)
        serializer = BlogSerializer(blog , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            blog = serializer.save(user_id=self.request.user.id)
            category_ids = request.data.get('category', [])
            
            for category_id in category_ids:
                try:
                    category = Categorice.objects.get(id=category_id)
                except:
                    return Response("no category", status=status.HTTP_400_BAD_REQUEST)
                blog.category.add(category)

            serializer = BlogSerializer(instance=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

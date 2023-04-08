from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
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
    

class AllBlogView(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    


class UserBlogList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blog = Blog.objects.filter(user = request.user)
        serializer = BlogSerializer(blog , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        category_obj = request.data.get('category')

        if category_obj is None:
            category_error = {
                                "category": [
                                    "This list may not be empty."
                                ]
                            }
            return Response(category_error, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid(raise_exception=True):
            blog = serializer.save(user_id=self.request.user.id, category=request.data['category'])
            serializer = BlogSerializer(instance=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

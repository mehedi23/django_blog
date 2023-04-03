from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from .models.ContentModels import Blog



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
        
        if serializer.is_valid():
            blog = serializer.save()
            serializer = BlogSerializer(instance=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

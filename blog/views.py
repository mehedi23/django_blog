from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from .models.ContentModels import Blog



class BlogDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AllBlogView(APIView):
    def get(sefl, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
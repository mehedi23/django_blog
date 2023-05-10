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

        serializer = BlogSerializer(blog, context={'request': request})
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
        try:
            blog = Blog.objects.filter(user = request.user, id=request.GET['blog_no'])
        except:
            blog = Blog.objects.filter(user = request.user)

        serializer = BlogSerializer(blog , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=self.request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def patch(self, request):
        try:
            blog = Blog.objects.filter(user = request.user).get(id=request.GET['blog_no'])
            serializer = BlogSerializer(blog, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
            return Response("Update success", status=status.HTTP_200_OK)
        except:
            return Response("no blog found", status=status.HTTP_400_BAD_REQUEST)

    


    def delete(self, request):
        try:
            blog = Blog.objects.filter(user = request.user).get(id=request.GET['blog_no'])
            blog.delete()
            return Response("delete success", status=status.HTTP_200_OK)
        except:
            return Response("no blog found", status=status.HTTP_400_BAD_REQUEST)


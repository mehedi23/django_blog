from rest_framework import serializers
from blog.models.ContentModels import Blog
from blog.models.Categorice import Categorice
from account.serializers import UserProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorice
        fields = ('id', 'name')

class BlogSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = ("__all__" )

    # def create(self, validated_data):
    #     category = validated_data.pop('category')
    #     blog_instance = Blog.objects.create(**validated_data)

    #     for category_name in category:
    #         # categorice_obj = Categorice.objects.get(id=category_name['id'])

    #     pass

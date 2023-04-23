from rest_framework import serializers
from blog.models.ContentModels import Blog
from blog.models.Categorice import Categorice
from account.serializers import UserProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorice
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    category = serializers.SerializerMethodField()
    create_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = ('id', 'user', 'banner', 'tittle', 'description', 'category', 'create_at', 'abc'  )

    def get_category(self, obj):
        categories = obj.category.all()
        return [{'id': category.id, 'name': category.name} for category in categories]
    
    def get_create_at(self, obj):
        return obj.create_at.date().strftime('%d-%m-%y %X') # time is given 00:00

import base64
from rest_framework import serializers
from blog.models.ContentModels import Blog
from account.serializers import UserProfileSerializer
from reactions.models import Likes
from blog.models.Categorice import Categorice
from django.core.files.base import ContentFile


def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))


class BlogSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    category = serializers.SerializerMethodField()
    create_at = serializers.SerializerMethodField()
    blog_likes = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = ('id', 'user', 'banner', 'tittle', 'description', 'category', 'create_at', 'blog_likes' )
        

    def create(self, validated_data, **kwargs):
        category_ids = self.initial_data.get('category', [])
        image_data = self.initial_data.get('banner_image', '')
        category_tags = []

        blog = super().create(validated_data, **kwargs)
        
        for category_id in category_ids:
            try:
                category = Categorice.objects.get(id=category_id)
                category_tags.append(category)
            except Categorice.DoesNotExist:
                category_tags = []
                raise serializers.ValidationError(f"Category with ID '{category_id}' does not exist")
            
            blog.category.set(category_tags)

        blog.banner.save(image_data['image_name'], base64_file(image_data['image_url']), save=True)
        return blog
    

    def update(self, instance, validated_data):
        category_ids = self.initial_data.get('category', [])
        image_data = self.initial_data.get('banner_image', '')
        category_tags = []

        for category_id in category_ids:
            try:
                category = Categorice.objects.get(id=category_id)
                category_tags.append(category)
            except Categorice.DoesNotExist:
                category_tags = []
                raise serializers.ValidationError(f"Category with ID '{category_id}' does not exist")
            
            instance.category.set(category_tags)
        
        blog = super().update(instance, validated_data)
        
        if image_data != '':
            blog.banner.save(image_data['image_name'], base64_file(image_data['image_url']), save=True)

        return blog
    

    def get_category(self, obj):
        categories = obj.category.all()
        return [{'id': category.id, 'name': category.name} for category in categories]
    
    
    def get_create_at(self, obj):
        return obj.create_at.strftime('%d-%m-%y %I:%M %p') # time is given 00:00
    
    
    def get_blog_likes(self, obj):
        likes = {}

        try:
            likes_obj = Likes.objects.get(post=obj.id)
            checking_liked = likes_obj.user.all()

            likes['total_likes'] = likes_obj.user.count()
            likes['is_liked'] = self.context['request'].user in checking_liked

        except:
            likes['total_likes'] = 0
            likes['is_liked'] = False
        
        return likes

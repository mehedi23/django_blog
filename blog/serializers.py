from rest_framework import serializers
from blog.models.ContentModels import Blog
from account.serializers import UserProfileSerializer
from reactions.models import Likes


class BlogSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    category = serializers.SerializerMethodField()
    create_at = serializers.SerializerMethodField()
    blog_likes = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = ('id', 'user', 'banner', 'tittle', 'description', 'category', 'create_at', 'blog_likes'  )

    def get_category(self, obj):
        categories = obj.category.all()
        return [{'id': category.id, 'name': category.name} for category in categories]
    
    def get_create_at(self, obj):
        return obj.create_at.date().strftime('%d-%m-%y %X') # time is given 00:00
    
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

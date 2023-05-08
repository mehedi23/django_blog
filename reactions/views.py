from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from blog.models.ContentModels import Blog
from reactions.models import Likes



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def setLikes(request, blog_id):

    try:
        blog = Blog.objects.get(id=blog_id)
    except:
        return Response("no blog")
    
    try:
        licked_obj = Likes.objects.get(post=blog)
    except:
        licked_obj = Likes.objects.create(post=blog)

    is_licked = licked_obj.user.filter(id=request.user.id).exists()

    if is_licked:
        licked_obj.user.remove(request.user)
    else:
        licked_obj.user.add(request.user)

    return Response("ok")
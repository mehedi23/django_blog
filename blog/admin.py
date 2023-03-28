from django.contrib import admin
from .models.ContentModels import Blog
from .models.Categorice import Categorice

# Blog admin
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle')

admin.site.register(Blog, BlogsAdmin)



# Calegorice
class CategoriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Categorice, CategoriceAdmin)
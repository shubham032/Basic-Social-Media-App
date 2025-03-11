from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'user')  # Add 'id' to list_display

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
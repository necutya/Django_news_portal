from django.contrib import admin
from .models import Post, Comment

# Register models for admin page
admin.site.register(Post)
admin.site.register(Comment)

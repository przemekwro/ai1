from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post, Like, Comment, Followers

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Followers)
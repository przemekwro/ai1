from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.ProtectedError)
    content = models.CharField(max_length = 500)
    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    comment_counter = models.IntegerField(default=0, blank=True)
    like_counter = models.IntegerField(default=0, blank=True)


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.ProtectedError)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    added_date = models.DateTimeField(auto_now_add=True, blank=True)


class Followers(models.Model):
    follow_by = models.ForeignKey(User, on_delete=models.ProtectedError, related_name="follow_by")
    follow_to = models.ForeignKey(User, on_delete=models.ProtectedError, related_name="follow_to")

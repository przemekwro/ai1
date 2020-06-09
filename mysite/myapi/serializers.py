from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Followers
from .models import Comment
from .models import Like
from .models import Post


class FollowersSerializer(serializers.HyperlinkedModelSerializer):
    follow_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    follow_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Followers
        fields = ('follow_by','follow_to')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=False)
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=False)
    class Meta:
        model = Like
        fields = ('owner','post')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    class Meta:
        model = Post
        fields = ('owner','content')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')





import json

from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import LikeSerializer, CommentSerializer, FollowersSerializer, UserSerializer, PostSerializer
from .models import Post, Like, Comment, Followers


# Create your views here.

@api_view(['POST','DELETE','GET'])
@authentication_classes([TokenAuthentication])
def post(request):
    if request.method=="POST":
        post = Post()
        post.owner = User.objects.get(id = request.data['owner'])
        post.content = request.data['content']
        post.save()
        return JsonResponse({'Response':'200'})
    elif request.method=="GET":
        queryset = Post.objects.filter(owner=request.query_params.get('owner')).values()
        return JsonResponse({"posts": list(queryset)})

    elif request.method == "DELETE":
        try:
            post = Post.objects.get(id=request.data['id'])
            post.delete()
            return JsonResponse({'response': 'deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'response': 'error'},status=status.HTTP_400_BAD_REQUEST)
    return Response( status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@authentication_classes([TokenAuthentication])
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        post = self.request.query_params.get('post')
        queryset = Like.objects.filter(post=post)
        return queryset


@authentication_classes([TokenAuthentication])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = Post.objects.get(id=self.request.query_params.get('post'))
        queryset = Comment.objects.filter(post=post)
        return queryset


@api_view(['POST','DELETE','GET'])
@authentication_classes([TokenAuthentication])
def follow(request):
    if request.method == "POST":
        try:
            print(request)
            follower = Followers()
            follower.follow_to = User.objects.get(id=request.data['follow_to'])
            follower.follow_by = User.objects.get(id=request.data['follow_by'])
            follower.save()
            return Response({'response': 'added'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'response': 'error'},status=status.HTTP_400_OK)

    elif request.method == "GET":
        queryset = Followers.objects.filter(follow_by=request.query_params.get('follow_by')).values()
        return JsonResponse({"followers": list(queryset)})
    elif request.method == "DELETE":
        try:
            follow = Followers.objects.get(id=request.data['id'])
            follow.delete()
            return JsonResponse({'response': 'deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'response': 'error'},status=status.HTTP_400_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


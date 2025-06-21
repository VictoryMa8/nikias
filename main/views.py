from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Profile, Friendship, Board, Post
from .serializers import ProfileSerializer, FriendshipSerializer, BoardSerializer, PostSerializer

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
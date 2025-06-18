from rest_framework import serializers
from .models import Profile, Friendship, Board, Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # 'class Meta' tells ModelSerializer which model to serialize and which fields to include
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    # Can't update the user through this profile endpoint
    # A nested serializer allows us to include the serialized representation of a related object directly within the parent object's JSON
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'avatar', 'created_at']

class FriendshipSerializer(serializers.ModelSerializer):
    # Instead of showing just the id of a related object, this lets us represent it with a more readable value (the user's username)
    sender = serializers.SlugRelatedField(slug_field='user__username', queryset=Profile.objects.all())
    receiver = serializers.SlugRelatedField(slug_field='user__username', queryset=Profile.objects.all())

    class Meta:
        model = Friendship
        fields = ['sender', 'receiver', 'status', 'created_at']

class BoardSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='user__username', read_only=True)

    class Meta:
        model = Board
        fields = ['title', 'description', 'author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='user__username', read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'author', 'source', 'boards', 'created_at']


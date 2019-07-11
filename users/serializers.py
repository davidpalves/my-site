# -*- coding: utf-8 -*-
from rest_framework import serializers
from users.models import User
from blog.serializers import PostSerializer
from blog.models import Post


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'full_name', 'email', 'bio', 'posts')
        model = User

    def get_posts(self, obj):
        posts = Post.objects.filter(author__id=obj.id)
        serializer = PostSerializer(posts, many=True)
        return serializer.data


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'bio', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

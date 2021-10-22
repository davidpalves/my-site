# -*- coding: utf-8 -*-
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from blog.models import Post
from blog.serializers import ChangePostStatusSerializer, PostSerializer
from blog.choices import POST_STATUS_ENUM
from blog.filters import PostsFilter


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'slug'
    filter_class = PostsFilter

    def get_queryset(self):
        if not self.request.user.is_staff or not self.request.user.is_superuser:
            return Post.objects.filter(status=POST_STATUS_ENUM.published).order_by('-published_date')
        
        return Post.objects.all().order_by('-published_date')
        
    @action(detail=True, methods=['POST'], name='Publish Post', serializer_class=ChangePostStatusSerializer)
    def publish_post(self, request, slug=None):
        post = self.get_object()
        action = request.data.get('action', None)
        
        if action not in ['draft', 'publish', 'archive']:
            return Response({'status': 'Action must be [draft, publish, archive]'}, status=status.HTTP_400_BAD_REQUEST)

        if post is not None:
            change_post_status = getattr(post, action, None)
            change_post_status()
            return Response({'status': 'Post status changed'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

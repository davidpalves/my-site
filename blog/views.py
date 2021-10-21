# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

    @action(detail=True, methods=['GET'], name='Publish Post')
    def publish_post(self, request, slug=None):
        post = self.get_object()

        if post is not None:
            post.publish()
            return Response({'status': 'Post published'})
        else:
            return Response({'status': 'Failed'})

    def perform_create(self, serializer):
        import ipdb; ipdb.set_trace()
        serializer.save(author=self.request.user)

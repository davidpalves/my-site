from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)

    class Meta:
        fields = (
            'slug',
            'title',
            'author',
            'text',
            'published_date'
        )
        model = Post
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

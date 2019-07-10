from rest_framework import serializers
from .models import Post
from blog.enums import POST_STATUS_ENUM


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    slug = serializers.SlugField(read_only=True, required=False)
    status = serializers.ChoiceField(choices=POST_STATUS_ENUM, default=0)

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)

    class Meta:
        fields = (
            'slug',
            'title',
            'author',
            'status',
            'text',
            'published_date'
        )
        model = Post
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

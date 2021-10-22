from rest_framework import serializers
from blog.models import Post, Tag
from blog.enums import POST_STATUS_ENUM


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('label',)
        model = Tag


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.first_name')
    slug = serializers.SlugField(read_only=True, required=False)
    status = serializers.ChoiceField(choices=POST_STATUS_ENUM, default=0)
    published_date = serializers.DateField(required=True)
    tags = TagsSerializer(many=True)

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
            'published_date',
            'tags'
        )
        model = Post
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ChangePostStatusSerializer(serializers.ModelSerializer):
    action = serializers.CharField(required=True)

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)

    class Meta:
        fields = (
            'action',
        )
        model = Post


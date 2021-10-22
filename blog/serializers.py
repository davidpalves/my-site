from rest_framework import serializers
from blog.models import Post
from blog.choices import POST_STATUS_CHOICES


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.first_name')
    slug = serializers.SlugField(read_only=True, required=False)
    status = serializers.ChoiceField(choices=POST_STATUS_CHOICES, default=POST_STATUS_CHOICES.draft)
    published_date = serializers.DateField(required=False)
    tags = serializers.SerializerMethodField()

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
            'tags',
            'read_time',
            'published_date',
        )
        model = Post
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def get_tags(self, obj):
        tags = obj.tags.split(", ")
        return tags


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


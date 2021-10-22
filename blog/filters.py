from django_filters import rest_framework as filters

from blog.models import Post


class PostsFilter(filters.FilterSet):
    tags = filters.CharFilter(lookup_expr="icontains")
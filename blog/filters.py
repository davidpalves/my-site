from django_filters import rest_framework as filters


class PostsFilter(filters.FilterSet):
    tags = filters.CharFilter(lookup_expr="icontains")
    author = filters.CharFilter(lookup_expr="iexact")

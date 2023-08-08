from django_filters import (
    CharFilter,
    FilterSet,
)
from django.contrib.postgres.search import SearchVector
from django.utils import timezone
from .models import Post
from rest_framework.exceptions import APIException

class FilterPost(FilterSet):
    search = CharFilter(method="title_search")
    author__in = CharFilter(method="filter_author__in")
    
    def title_search(self, queryset , name , value):
        return queryset.annotate(search = SearchVector("title")).filter(search=value)
    
    def filter_author__in(self, queryset , name , value):
        authors = value.split(",")
        return queryset.filter(author__username__in=authors)
    
    class Meta:
        model = Post
        fields = (
            "slug",
            "description",
        )
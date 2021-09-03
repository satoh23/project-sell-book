from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny
from rest_framework import generics
from article.serializers import ListDetailSerializer
from article.models import Detail


class DetailFilter(filters.FilterSet):
    title = filters.CharFilter(
        lookup_expr='contains')

    class Meta:
        model = Detail
        fields = ['title', ]


class ListDetailView(generics.ListAPIView):
    queryset = Detail.objects.filter(now_public=True)
    serializer_class = ListDetailSerializer
    permission_classes = (AllowAny,)
    filter_class = DetailFilter

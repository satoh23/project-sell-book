from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from article.serializers import ListBoughtArticleSerializer
from article.models import PurchaseHistory


# class DetailFilter(filters.FilterSet):
#     title = filters.CharFilter(
#         lookup_expr='contains')
#
#     class Meta:
#         model = Detail
#         fields = ['title', ]


class ListBoughtArticleView(generics.ListAPIView):
    serializer_class = ListBoughtArticleSerializer
    permission_classes = (IsAuthenticated,)
    # filter_class = DetailFilter

    def get_queryset(self):
        user = self.request.user
        return PurchaseHistory.objects.filter(purchase=user)

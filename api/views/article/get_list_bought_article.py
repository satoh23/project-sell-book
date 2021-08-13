from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from article.serializers import ListBoughtArticleSerializer
from article.models import PurchaseHistory


class ListBoughtArticleView(generics.ListAPIView):
    serializer_class = ListBoughtArticleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return PurchaseHistory.objects.filter(purchase=user)

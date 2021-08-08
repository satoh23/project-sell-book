from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from article.serializers import GetHistorySerializer
from article.models import PurchaseHistory


class BuyArticleView(generics.CreateAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = GetHistorySerializer
    permission_classes = (IsAuthenticated,)

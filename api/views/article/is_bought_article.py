from article.serializers import GetHistorySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from article.models import PurchaseHistory, Detail
from rest_framework.response import Response
from rest_framework import status
from article.serializers import GetBodySerializer


class IsBoughtView(APIView):
    """ 記事が未購入の場合は400エラー
     　　購入済みの場合は記事の本文を返す"""
    serializer_class = GetHistorySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        purchase_history = PurchaseHistory.objects.filter(purchase=request.data['purchase'], article=request.data['article'])
        if len(purchase_history) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST,)
        article = Detail.objects.values_list('body', flat=True).get(pk=request.data['article'])
        article_body = GetBodySerializer(data=article)
        return Response(data={'body': article_body.initial_data}, status=status.HTTP_200_OK,)

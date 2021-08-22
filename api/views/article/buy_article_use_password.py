from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from accounts.models import CustomUser
from article.models import PurchaseHistory, Detail


@api_view(['POST'])
def Buy_article_use_password(request):
    data = request.data
    purchase_id = ""
    article_id = ""
    password = ""
    if len(data['purchase']) < 2:
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': '先にログインしてください'})
    else:
        purchase_id = data['purchase']
        article_id = data['article']
        password = data['password']

    purchase = CustomUser.objects.get(pk=purchase_id)
    article = Detail.objects.get(pk=article_id)
    history = PurchaseHistory.objects.filter(purchase=purchase, article=article)
    if len(history) > 0:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': '既に購入済みです'})

    if article.password == password:
        purchase_history = PurchaseHistory(purchase=purchase, article=article)
        purchase_history.save()
        return Response(status=status.HTTP_200_OK,
                        data={'message': 'Success'})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'パスワードが違います'})

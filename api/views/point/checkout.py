import math

import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from accounts.models import CustomUser
from article.models import PurchaseHistory, Detail


stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['POST'])
def save_stripe_info(request):
    data = request.data
    purchase_id = ""
    article_id = ""
    amount = 0
    if len(data['purchase']) < 2:
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': '先にログインしてください'})
    else:
        purchase_id = data['purchase']
        article_id = data['article']
        amount = Detail.objects.values_list('amount', flat=True).get(pk=article_id)

    purchase = CustomUser.objects.get(pk=purchase_id)
    article = Detail.objects.get(pk=article_id)
    history = PurchaseHistory.objects.filter(purchase=purchase, article=article)
    if len(history) > 0:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': '既に購入済みです'})

    if amount >= 1:
        name = data['name']
        email = data['email']
        payment_method_id = data['payment_method_id']

        customer_data = stripe.Customer.list(email=email).data

        if len(customer_data) == 0:
            customer = stripe.Customer.create(
                name=name, email=email, payment_method=payment_method_id)
        else:
            customer = customer_data[0]

        try:
            stripe.PaymentIntent.create(
                customer=customer,
                payment_method=payment_method_id,
                currency='jpy',
                amount=math.ceil(amount*1.038),
                confirm=True
            )
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': '決済に失敗しました'})

    purchase_history = PurchaseHistory(purchase=purchase, article=article)
    purchase_history.save()
    return Response(status=status.HTTP_200_OK,
                    data={'message': 'Success'})

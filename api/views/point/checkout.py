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
    name = data['name']
    email = data['email']
    purchase_id = data['purchase']
    article_id = data['article']
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
            amount=math.ceil(data['amount']*1.038),
            confirm=True
        )
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': '決済に失敗しました'})

    purchase = CustomUser.objects.get(pk=purchase_id)
    article = Detail.objects.get(pk=article_id)
    purchase_history = PurchaseHistory(purchase=purchase, article=article)
    purchase_history.save()
    return Response(status=status.HTTP_200_OK,
                    data={'message': 'Success'})

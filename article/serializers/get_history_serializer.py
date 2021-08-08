from rest_framework import serializers
from article.models import PurchaseHistory


class GetHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseHistory
        fields = ('purchase', 'article')

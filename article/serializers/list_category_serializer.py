from rest_framework import serializers
from article.models import Category


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category',)

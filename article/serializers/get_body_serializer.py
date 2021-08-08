from rest_framework import serializers
from article.models import Detail


class GetBodySerializer(serializers.ModelSerializer):
    """各ブログの詳細取得に使う"""

    class Meta:
        model = Detail
        fields = ('body',)
        read_only_fields = ('body',)

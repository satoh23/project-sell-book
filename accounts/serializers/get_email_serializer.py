from rest_framework import serializers
from accounts.models import CustomUser


class GetEmailSerializer(serializers.ModelSerializer):
    """各ユーザーのemail取得に使う"""
    class Meta:
        model = CustomUser
        fields = ('email',)
        read_only_fields = ('email',)

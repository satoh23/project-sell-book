from rest_framework import serializers
from article.models import Detail


class CreateDetailNotThumbnailSerializer(serializers.ModelSerializer):
    """記事の作成、編集でサムネイルが存在しない場合に使う(これを使わないとBadRequestになる)"""

    class Meta:
        model = Detail
        fields = ('title', 'summary', 'body', 'category', 'author_id')

    def create(self, validated_data):
        article = Detail(
                         title=validated_data['title'],
                         summary=validated_data['summary'],
                         body=validated_data['body'],
                         category=validated_data['category'],
                         author_id=validated_data['author_id'],
                         )
        article.save()
        return article

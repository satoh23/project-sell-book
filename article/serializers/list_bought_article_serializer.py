from rest_framework import serializers
from article.models import PurchaseHistory

from rest_framework.serializers import SerializerMethodField


class ListBoughtArticleSerializer(serializers.ModelSerializer):
    article_id = SerializerMethodField()
    article_thumbnail = SerializerMethodField()
    article_title = SerializerMethodField()
    article_summary = SerializerMethodField()
    article_category = SerializerMethodField()
    article_author = SerializerMethodField()

    class Meta:
        model = PurchaseHistory
        fields = ('purchase', 'article', 'article_id',
                  'article_thumbnail', 'article_title', 'article_summary', 'article_category', 'article_author')

    def get_article_id(self, obj):
        try:
            article_id = obj.article.id
            return article_id
        except:
            return None

    def get_article_thumbnail(self, obj):
        try:
            article_thumbnail = obj.article.encoded_thumbnail
            return article_thumbnail
        except:
            return None

    def get_article_title(self, obj):
        try:
            article_title = obj.article.title
            return article_title
        except:
            return None

    def get_article_summary(self, obj):
        try:
            article_summary = obj.article.summary
            return article_summary
        except:
            return None

    def get_article_category(self, obj):
        try:
            article_category = obj.article.category.category
            return article_category
        except:
            return None

    def get_article_author(self, obj):
        try:
            article_author = obj.article.author_id.username
            return article_author
        except:
            return None

from django.contrib import admin

from article.models import Category, Detail, PurchaseHistory

admin.site.register(Category)
admin.site.register(Detail)
admin.site.register(PurchaseHistory)

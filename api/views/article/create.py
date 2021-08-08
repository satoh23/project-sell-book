from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from article.serializers import CreateDetailSerializer
from article.models import Detail


class CreateView(generics.CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = CreateDetailSerializer
    permission_classes = (IsAdminUser,)

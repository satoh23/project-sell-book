from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from article.serializers import GetBodySerializer
from article.models import Detail


class GetBodyView(generics.RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = GetBodySerializer
    permission_classes = (IsAuthenticated,)

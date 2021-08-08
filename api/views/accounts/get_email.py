from accounts.serializers import GetEmailSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models.custom_user import CustomUser


class GetEmailView(RetrieveAPIView):
    """
    cookieにAccessTokenが入っている時だけアクセス可能
    """
    serializer_class = GetEmailSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()

    def get_object(self):
        return self.request.user

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountList(ListAPIView):
    """
    List all registerd user accounts
    """

    permission_classes = (IsAdminUser, )
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


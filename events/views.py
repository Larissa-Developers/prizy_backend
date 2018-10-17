from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

# TODO: implement event-related views


class EventList(ListAPIView):
    """
    List all registered user accounts
    """

    permission_classes = (IsAdminUser, )



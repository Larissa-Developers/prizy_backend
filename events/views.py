from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from events.models import Event
from events.serializers import EventSerializer


class EventList(ListAPIView):
    """
    List all registerd user accounts
    """

    permission_classes = (IsAdminUser, )
    queryset = Event.objects.all()
    serializer_class = EventSerializer


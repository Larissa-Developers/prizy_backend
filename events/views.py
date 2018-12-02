from django.conf import settings
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import meetup.api

from events.models import Event
from events.serializers import EventSerializer, EventDetailSerializer


class EventList(ListAPIView):
    """
    List all Meetup events
    """

    permission_classes = (IsAdminUser, )
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetails(RetrieveAPIView):
    """
    List one event with all the fields
    """
    permission_classes = (IsAdminUser, )
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class Meetupcom(APIView):
    """
    Bridging for www.meetup.com
    """

    permission_classes = (IsAuthenticated,)

    def get(self, req):
        try:
            client = meetup.api.Client(settings.MEETUPCOM_API_KEY)
            group_info = client.GetGroup({'urlname': 'Larissa-Developers-Meetup'})
            # use various method on client from
            # https://meetup-api.readthedocs.io/en/latest/meetup_api.html#api-client-details
            return Response(status=status.HTTP_200_OK, data=group_info.__dict__.values())
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))

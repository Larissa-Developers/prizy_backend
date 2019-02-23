from django.conf import settings

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import meetup.api

from events.models import Event, EventCheckIn
from events.serializers import EventSerializer, EventCheckInSerializer


class EventList(ListAPIView):
    """
    List all Meetup events
    """

    permission_classes = (IsAuthenticated, )
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetails(RetrieveAPIView):
    """
    List one event with all the fields
    """

    permission_classes = (IsAuthenticated, )
    lookup_field = 'pk'
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCheckInCreate(APIView):
    """
    Create a new event check-in
    """

    permission_classes = (IsAuthenticated, )

    def post(self, req, pk):
        checkin = EventCheckIn()
        serializer = EventCheckInSerializer(instance=checkin, data=req.data)
        if serializer.is_valid() and serializer.validated_data['event'].id == pk:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            'reason': 'Request data not properly structured'
        })


class MeetupCom(APIView):
    """
    Bridging for www.meetup.com
    """

    permission_classes = (IsAuthenticated,)

    def get(self, req):
        try:
            client = meetup.api.Client(settings.MEETUPCOM_API_KEY)
            group_info = client.GetGroup({'urlname': 'Larissa-Developers-Meetup'})
            # use various methods on client from
            # https://meetup-api.readthedocs.io/en/latest/meetup_api.html#api-client-details
            return Response(status=status.HTTP_200_OK, data=group_info.__dict__.values())
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))

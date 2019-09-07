from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

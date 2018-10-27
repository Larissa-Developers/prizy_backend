from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import meetup.api
import json


# TODO: implement event-related views


class EventList(ListAPIView):
    """
    List all registered user accounts
    """

    permission_classes = (IsAdminUser, )


class Meetupcom(APIView):
    """
    Bridging for www.meetup.com
    """

    permission_classes = (AllowAny,)

    def get(self, req):
        try:
            client = meetup.api.Client('648562f7e53693e31722361f144756')
            group_info = client.GetGroup({'urlname': 'Larissa-Developers-Meetup'})
            # use various method on client from https://meetup-api.readthedocs.io/en/latest/meetup_api.html#api-client-details
            return Response(status=status.HTTP_200_OK, data=group_info.__dict__.values())
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



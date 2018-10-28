from django.conf import settings
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import meetup.api


class EventList(ListAPIView):
    """
    List all registered user accounts
    """

    permission_classes = (IsAdminUser, )
    # TODO: implement view


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

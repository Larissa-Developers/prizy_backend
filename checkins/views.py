from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from checkins.models import Checkin
from checkins.serializers import CheckinSerializer, CheckinDetailsSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class CheckinCreate(APIView):
    """
    Create a new check in
    """
    permission_classes = (IsAuthenticated, )

    def post(self, req, pk):
        checkin = Checkin()
        serializer = CheckinSerializer(checkin, data=req.data)
        # The body's id must be the same with the url's pk
        if serializer.is_valid() and serializer.validated_data['event'].id == pk:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            'reason': 'Request data not properly structured'
        })


class CheckinDetails(RetrieveAPIView):
    """
    List one check-in in depth
    """
    permission_classes = (IsAuthenticated, )
    queryset = Checkin.objects.all()
    serializer_class = CheckinDetailsSerializer
    depth = 1


class CheckinList(ListAPIView):
    """
    List all check-ins
    """

    permission_classes = (IsAuthenticated,)
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer

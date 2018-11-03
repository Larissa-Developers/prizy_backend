from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from checkins.models import Checkin
from checkins.serializers import CheckinSerializer, CheckinDetailsSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

from events.models import Event


class CheckinCreate(APIView):
    """
    Create a new check in
    """
    permission_classes = (IsAdminUser, )
    def post(self, req):
        checkin = Checkin()
        serializer = CheckinSerializer(checkin, data=req.data)
        if serializer.is_valid():
            if Event.objects.filter(id=serializer.validated_data['event'].id).exists() and Account.objects.filter(id=serializer.validated_data['account'].id).exists():
                serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            'reason': 'Request data not properly structured'
        })



class CheckinDetails(RetrieveAPIView):
    """
    List one check-in in depth
    """
    permission_classes = (IsAdminUser, )
    queryset = Checkin.objects.all()
    serializer_class = CheckinDetailsSerializer
    depth = 1


class CheckinList(ListAPIView):
    """
    List all check-ins
    """

    permission_classes = (IsAdminUser,)
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer

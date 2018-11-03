from rest_framework import serializers

from checkins.models import Checkin


class CheckinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkin
        fields = '__all__'


class CheckinDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkin
        fields = '__all__'
        depth = 1

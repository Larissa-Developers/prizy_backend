from rest_framework import serializers

from events.models import *


class EventVenueSerializer(serializers.ModelSerializer):
    """
    Serializer class for a single venue
    """

    class Meta:
        model = EventVenue
        fields = (
            'id',
            'venue_meetup_id',
            'country',
            'city',
            'address',
            'name',
            'lon',
            'lat',
            'repinned',
        )


class EventFeeSerializer(serializers.ModelSerializer):
    """
    Serializer class for a single event fee
    """

    class Meta:
        model = EventFee
        fields = '__all__'


class EventCheckInSerializer(serializers.ModelSerializer):
    """
    Serializer class for a single event check-in
    """

    class Meta:
        model = EventCheckIn
        fields = (
            'account',
            'event'
        )


class EventDrawParticipationSerializer(serializers.ModelSerializer):
    """
    Serializer class for a single event prize draw participation
    """

    class Meta:
        model = EventDrawParticipation
        fields = (
            'id'
        )


class EventDrawSerializer(serializers.ModelSerializer):
    """
    Serializer class for a single event prize draw
    """

    draw_participations = EventDrawParticipationSerializer(many=True)

    class Meta:
        model = EventDraw
        fields = (
            'title'
        )


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer class for a single event instance
    """

    event_venue = EventVenueSerializer()
    event_fee = EventFeeSerializer()
    event_checkins = EventCheckInSerializer(many=True)
    event_draws = EventDrawSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

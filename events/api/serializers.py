from rest_framework import serializers, relations
from rest_framework.relations import PrimaryKeyRelatedField

from events.models import Event, Venue, Fee


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = [
            'id',
            'venue_meetup_id',
            'country',
            'city',
            'address',
            'name',
            'lon',
            'lat',
            'repinned',
        ]


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = [
            'amount',
            'label',
            'required',
        ]


class EventSerializer(serializers.ModelSerializer):
    event_venue = VenueSerializer()
    event_fee = FeeSerializer()

    class Meta:
        model = Event
        fields = [
            'id',
            'event_venue',
            'reservation_limit',
            'headcount',
            'visibility',
            'waitlistcount',
            'event_fee',
            'description',
            'event_url',
            'yes_reservation_count',
            'duration',
            'name',
            'time',
            'updated',
            'status',


        ]



from rest_framework import serializers

from events.models import Event, EventVenue, EventFee


class EventVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVenue
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


class EventFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFee
        fields = [
            'amount',
            'label',
            'required',
        ]


class EventSerializer(serializers.ModelSerializer):
    event_venue = EventVenueSerializer()
    event_fee = EventFeeSerializer()

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

    def create(self, validated_data):
        return Event.objects.create(**validated_data)


class EventDetailSerializer(serializers.ModelSerializer):
    event_venue = EventVenueSerializer()
    event_fee = EventFeeSerializer()

    class Meta:
        model = Event
        fields = '__all__'

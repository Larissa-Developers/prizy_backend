import datetime

from django.db import models
from accounts.models import Account


def get_current_datetime():
    return datetime.datetime.now()


class EventVenue(models.Model):
    """
    Data representation of a Meetup event venue
    """

    venue_meetup_id = models.CharField(max_length=32, default='')
    country = models.CharField(max_length=32, blank=False, null=False)
    city = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=80, blank=False, null=False)
    name = models.CharField(max_length=80, blank=False, null=False)
    lon = models.DecimalField(max_digits=10, decimal_places=7)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    repinned = models.BooleanField(default=False)

    def __str__(self):
        return 'Venue : {} {}'.format(self.id, self.name)


class EventFee(models.Model):
    """
    Data representation of a Meetup event participation fee
    """

    amount = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=10, default='EU')
    label = models.CharField(max_length=30, default='price')
    required = models.BooleanField(default=True)

    def __str__(self):
        return 'Fee: {} {}'.format(self.id, self.label)


class Event(models.Model):
    """
    Equivalent to the Meetup API event model
    """

    event_meetup_id = models.CharField(max_length=32, default='')
    event_venue = models.OneToOneField(to=EventVenue, on_delete=models.CASCADE)
    event_fee = models.OneToOneField(to=EventFee, on_delete=models.CASCADE)
    reservation_limit = models.IntegerField(default=100)
    headcount = models.IntegerField(default=0)
    visibility = models.CharField(max_length=10)
    waitlist_count = models.IntegerField(default=0)
    description = models.TextField()
    event_url = models.CharField(max_length=250)
    yes_reservation_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    name = models.CharField(max_length=80, blank=False, null=False)
    time = models.IntegerField()
    updated = models.IntegerField()
    status = models.CharField(max_length=50, default='upcoming')

    def __str__(self):
        return 'Event: {} {}'.format(self.id, self.name)


class EventCheckIn(models.Model):
    """
    Data representation of a user check-in to an Event
    """

    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    date = models.DateTimeField(default=get_current_datetime)

    class Meta:
        unique_together = ('account', 'event')

    def __str__(self):
        return 'Account: {} - Event: {}'.format(self.account.username, self.event.id)


class EventDraw(models.Model):
    """
    Data representation of an event prize draw
    """

    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=True, default="")

    def __str__(self):
        return 'Draw: {} {}'.format(self.event.id, self.id)


class EventDrawParticipation(models.Model):
    """
    Data representation of an event prize draw participation
    """

    checkin = models.ForeignKey(to=EventCheckIn, on_delete=models.CASCADE)
    draw = models.ForeignKey(to=EventDraw, on_delete=models.CASCADE)
    date = models.DateTimeField(default=get_current_datetime)

    class Meta:
        unique_together = ('checkin', 'draw')

    def __str__(self):
        return 'Draw Participation: {} {}'.format(self.draw.id, self.id)

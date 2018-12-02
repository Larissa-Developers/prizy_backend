from django.db import models
from PIL import Image
from accounts.models import Account


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
        return 'Venue : {}'.format(self.id)


class EventFee(models.Model):
    """
    Data representation of a Meetup event participation fee
    """

    amount = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=10, default='EU')
    label = models.CharField(max_length=30, default='price')
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class Event(models.Model):
    """
    Equivalent to meet up's api Event model
    """

    event_meetup_id = models.CharField(max_length=32, default='')
    event_venue = models.ForeignKey(to=EventVenue, on_delete=models.CASCADE)
    reservation_limit = models.IntegerField(default=100)
    headcount = models.IntegerField(default=0)
    visibility = models.CharField(max_length=10)
    waitlistcount = models.IntegerField(default=0)
    event_fee = models.ForeignKey(to=EventFee, on_delete=models.CASCADE)
    description = models.TextField()
    event_url = models.CharField(max_length=250)
    yes_reservation_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    name = models.CharField(max_length=80, blank=False, null=False)
    photo = models.ImageField(default='event_pics/default.png', upload_to='event_pics')
    time = models.IntegerField()
    updated = models.IntegerField()
    status = models.CharField(max_length=50, default='upcoming')
    checkins = models.ManyToManyField(Account, blank=True, related_name='checked_in')

    def save(self, *kwargs):
        """
        Overrides default behaviour to crop the image
        """

        super().save()

        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        return self.name

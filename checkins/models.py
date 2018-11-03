from django.db import models

from accounts.models import Account
from events.models import Event


class Checkin(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('account', 'event')

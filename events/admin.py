from django.contrib import admin
from .models import Event, EventFee, EventVenue
# Register your models here.
admin.site.register(EventVenue)
admin.site.register(EventFee)
admin.site.register(Event)

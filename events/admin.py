from django.contrib import admin
from .models import Event, Fee, Venue
# Register your models here.
admin.site.register(Venue)
admin.site.register(Fee)
admin.site.register(Event)

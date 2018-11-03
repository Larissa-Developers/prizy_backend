# Generated by Django 2.1.2 on 2018-11-01 21:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_checkins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='checkins',
            field=models.ManyToManyField(blank=True, related_name='checked_in', to=settings.AUTH_USER_MODEL),
        ),
    ]
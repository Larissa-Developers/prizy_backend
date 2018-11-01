from django.urls import path

from events import views

urlpatterns = [
    path('events', views.EventList.as_view(), name='events'),
    path('meetupcom', views.Meetupcom.as_view(), name='meetupcom'),
]

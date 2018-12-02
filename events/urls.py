from django.urls import path, re_path
from events import views
from checkins import views as checkin_views

urlpatterns = [
    re_path(r'^events/$', views.EventList.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetails.as_view(), name='events-details'),
    path('events/<int:pk>/checkin', checkin_views.CheckinCreate.as_view(), name='events-checkin'),
    path('meetupcom', views.Meetupcom.as_view(), name='meetupcom'),
]

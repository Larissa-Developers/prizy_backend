from django.urls import path, re_path

from events import views

urlpatterns = [
    re_path(r'^events/$', views.EventList.as_view(), name='events'),
    path('events/<pk>', views.EventDetails.as_view(), name='events-details'),
    path('meetupcom', views.Meetupcom.as_view(), name='meetupcom'),

]

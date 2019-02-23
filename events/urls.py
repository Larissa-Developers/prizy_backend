from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:pk>', views.EventDetails.as_view(), name='events-details'),
    path('events/<int:pk>/checkin', views.EventCheckInCreate.as_view(), name='events-checkin'),
    path('meetupcom', views.MeetupCom.as_view(), name='meetupcom'),
]

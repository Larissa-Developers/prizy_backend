from django.urls import path

from events.api import views

urlpatterns = [
    path('', views.EventsListAPIView().as_view(), name='events'),
]

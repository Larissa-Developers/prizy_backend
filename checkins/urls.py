from django.urls import path

from . import views

urlpatterns = [
    path('checkins', views.CheckinList.as_view(), name='checkins'),
    path('checkins/<int:pk>', views.CheckinDetails.as_view(), name='accounts_checkin_details'),
    path('checkins/create', views.CheckinCreate.as_view(), name='accounts_account_setup'),
]

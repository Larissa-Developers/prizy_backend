from django.urls import path

from accounts import views

urlpatterns = [
    path('accounts', views.AccountList.as_view(), name='accounts'),
]

from django.urls import path

from accounts import views

urlpatterns = [
    path('accounts', views.AccountList.as_view(), name='accounts'),
    path('accounts/register', views.AccountRegister.as_view(), name='accounts_account_register'),
    path('accounts/login', views.AccountLogin.as_view(), name='accounts_account_login'),
    path('accounts/<pk>', views.AccountDetails.as_view(), name='accounts_account_details'),
    path('accounts/<pk>/setup/<key>', views.AccountSetup.as_view(), name='accounts_account_setup'),
]

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class Account(AbstractUser):
    """
    Base Prizy user account class
    """

    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=False, null=False)
    init_pass = models.UUIDField(default=uuid.uuid4, null=True)
    phone_num = models.CharField(max_length=32, blank=True, null=True)
    profile_pic = models.ImageField(default="", blank=True, upload_to="")

    def __str__(self):
        return 'Account: {}'.format(self.username)


class AccountSetupForm(forms.Form):
    """
    Prizy Account setup form class
    """

    passw = forms.CharField(label='Password', widget=forms.PasswordInput)
    passw_repeat = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    def clean(self):
        """
        Validate values passed to the password fields
        """

        cleaned_data = super().clean()
        passw = cleaned_data.get("password")
        passw_repeat = cleaned_data.get("password_repeat")

        if passw != passw_repeat:
            raise forms.ValidationError("Password values do not match.")

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import Account


class AccountChangeForm(UserChangeForm):
    """
    Implements the (html) form when editing an Account object through the Django admin panel.
    """

    class Meta(UserChangeForm.Meta):
        model = Account


class AccountAdmin(UserAdmin):
    """
    Account class fields that are exposed in the Django admin panel.
    """

    form = AccountChangeForm
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')}),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # Extras
        ('Extra Info', {'fields': ('phone_num', 'profile_pic')}),
    )


# Don't forget to register the model and it's related admin panel helper class
admin.site.register(Account, AccountAdmin)
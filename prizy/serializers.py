from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.compat import Serializer
from rest_framework_jwt.settings import api_settings

from accounts.models import Account

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class PrizyJWTSerializer(Serializer):
    """
    Custom JSON Web Token serializer class for Prizy.
    Modifies DRF JSONWebTokenSerializer to use username & email fields for JWT generation.
    """

    def __init__(self, *args, **kwargs):
        """
        Set fixed JWT credential fields
        """
        super(PrizyJWTSerializer, self).__init__(*args, **kwargs)

        self.fields['username'] = serializers.CharField()
        self.fields['email'] = serializers.CharField()

    def validate(self, attrs):
        credentials = {
            'username': attrs.get('username'),
            'email': attrs.get('email')
        }

        if all(credentials.values()):
            account = Account.objects.filter(username=credentials['username'], email=credentials['email']).first()

            if account:
                if not account.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(account)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': account
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)

        else:
            msg = _('Must include "username" and "email".')
            raise serializers.ValidationError(msg)

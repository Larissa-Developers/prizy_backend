from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    """
    Prizy Account model instance serializer
    """

    password = serializers.CharField(max_length=128, allow_blank=True, write_only=True, required=False)

    class Meta:
        model = Account
        fields = "__all__"

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


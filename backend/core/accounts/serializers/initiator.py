from rest_framework import serializers

from core.accounts.utils.get_user_model import User


class InitiatorReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'profile_picture',
        ]

from rest_framework import serializers

from core.accounts.utils.get_user_model import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

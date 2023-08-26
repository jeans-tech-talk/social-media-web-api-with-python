from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from core.accounts.utils.get_user_model import User
from core.common.mixins.request_user_serializer import RequestUserSerializerMixin


class ChangePasswordSerializer(RequestUserSerializerMixin, serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password',
            'confirm_new_password',
        ]

    def validate_old_password(self, value):
        request_user = self.get_request_user()
        if request_user and not request_user.user.check_password(value):
            raise serializers.ValidationError('Old password is not correct')
        return value

    def validate_new_password(self, value):
        validate_password(value, self.get_request_user())
        return value

    def validate(self, data):
        if data.get('new_password') != data.get('confirm_new_password'):
            raise serializers.ValidationError('Password did not match')
        return data

    def update(self, instance, validated_data):
        new_password = validated_data.get('new_password')
        instance.password = make_password(new_password)
        instance.save()
        return instance

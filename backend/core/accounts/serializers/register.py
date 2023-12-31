from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from drf_base64.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.accounts.utils.get_user_model import User
from core.common.mixins.request_user_serializer import RequestUserSerializerMixin


class RegisterSerializer(RequestUserSerializerMixin, serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    profile_picture = Base64ImageField(required=False)
    profile_cover = Base64ImageField(required=False)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'profile_picture',
            'profile_cover',
            'bio',
            'password',
            'confirm_password',
        ]

    def validate_password(self, value):
        validate_password(value, self.get_request_user())
        return value

    def validate(self, data):
        if data.get('password') != data.pop('confirm_password'):
            raise serializers.ValidationError('Password did not match')
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')

        return User.objects.create(
            password=make_password(password),
            **validated_data,
        )

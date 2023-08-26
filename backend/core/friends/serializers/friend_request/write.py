from rest_framework import serializers

from core.common.mixins.request_user_serializer import RequestUserSerializerMixin
from core.friends.models import FriendRequest


class FriendRequestWriteSerializer(RequestUserSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['acceptor']

    def create(self, validated_data):
        validated_data['initiator'] = self.get_request_user()
        return super().create(validated_data)

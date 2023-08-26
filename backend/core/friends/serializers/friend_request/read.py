from rest_framework import serializers

from core.accounts.serializers.acceptor import AcceptorReadSerializer
from core.accounts.serializers.initiator import InitiatorReadSerializer
from core.common.utils.timer import Timer
from core.friends.models import FriendRequest


class FriendRequestReadSerializer(serializers.ModelSerializer):
    initiator = InitiatorReadSerializer()
    acceptor = AcceptorReadSerializer()
    status_display = serializers.CharField(source='get_status_display')
    since = serializers.SerializerMethodField()

    class Meta:
        model = FriendRequest
        fields = '__all__'

    @staticmethod
    def get_since(obj):
        timer = Timer(created_at=obj.created_at)
        return timer.calculate_time_different()

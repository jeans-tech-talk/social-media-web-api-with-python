from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.common.mixins.write_read_serializer import WriteReadSerializerMixin
from core.friends.choices.friend_request_status import FriendRequestStatus
from core.friends.models.friend_request import FriendRequest
from core.friends.serializers.friend_request.read import FriendRequestReadSerializer
from core.friends.serializers.friend_request.write import FriendRequestWriteSerializer


class FriendRequestViewSet(WriteReadSerializerMixin, viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_classes = {
        'write': FriendRequestWriteSerializer,
        'read': FriendRequestReadSerializer,
    }
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(
            acceptor=self.request.user,
            status=FriendRequestStatus.SENT,
        ).order_by('-created_at')

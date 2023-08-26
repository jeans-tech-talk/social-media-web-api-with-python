from django.db import models

from core.accounts.utils.get_user_model import User
from core.friends.choices.friend_request_status import FriendRequestStatus


class FriendRequest(models.Model):
    initiator = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='initiator_friend_requests',
    )
    acceptor = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='acceptor_friend_requests',
    )
    status = models.CharField(
        max_length=8,
        choices=FriendRequestStatus.choices,
        default=FriendRequestStatus.SENT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = 'friends_friend_request'

from django.db import models
from django.utils.translation import gettext_lazy as _


class FriendRequestStatus(models.TextChoices):
    SENT = 'SENT', _('Sent')
    ACCEPTED = 'ACCEPTED', _('Accepted')
    REJECTED = 'REJECTED', _('Rejected')

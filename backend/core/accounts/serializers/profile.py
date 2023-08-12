from core.accounts.serializers.user import UserSerializer


class ProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = [
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions',
        ]

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from core.accounts.serializers.change_password import ChangePasswordSerializer
from core.accounts.serializers.profile import ProfileSerializer
from core.accounts.serializers.register import RegisterSerializer
from core.accounts.serializers.user import UserSerializer
from core.accounts.utils.get_user_model import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('pk')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        if self.action in ['retrieve_profile', 'update_profile', 'change_password']:
            return self.request.user
        return super().get_object()

    @action(
        methods=['post'],
        detail=False,
        url_path='register',
        serializer_class=RegisterSerializer,
        permission_classes=[AllowAny],
    )
    def register(self, request):
        return super().create(request)

    @action(
        methods=['get'],
        detail=False,
        url_path='profile',
        serializer_class=ProfileSerializer,
        permission_classes=[IsAuthenticated],
    )
    def retrieve_profile(self, request):
        return super().retrieve(request)

    @retrieve_profile.mapping.put
    def update_profile(self, request):
        return super().update(request)

    @action(
        methods=['put'],
        detail=False,
        url_path='change-password',
        serializer_class=ChangePasswordSerializer,
        permission_classes=[IsAuthenticated],
    )
    def change_password(self, request):
        return super().update(request)

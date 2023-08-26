from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.accounts.views import UserViewSet
from core.friends.views import FriendRequestViewSet

router = routers.DefaultRouter()
router.register(prefix=r'users', viewset=UserViewSet)
router.register(prefix=r'friend-requests', viewset=FriendRequestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

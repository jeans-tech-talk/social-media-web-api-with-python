from django.contrib import admin

from core.accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_staff',
    ]


admin.site.register(User, UserAdmin)

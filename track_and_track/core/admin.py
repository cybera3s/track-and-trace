from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from core.models import User


admin.site.site_header = f"{settings.SITE_NAME} Admin"
admin.site.site_title = f"{settings.SITE_NAME} Admin Portal"
admin.site.index_title = f"{settings.SITE_NAME}"

admin.site.register(User, UserAdmin)


class BaseAdmin(admin.ModelAdmin):
    """
    This class used to exclude unused base model
    fields from admin panel
    """

    exclude = (
        "created",
        "last_updated",
        "delete_timestamp",
        "deleted_at",
        "is_deleted",
        "is_active"
    )
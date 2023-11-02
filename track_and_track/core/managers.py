from django.db import models


class BaseManager(models.Manager):
    """
    Base manager that works with logical operations
    like: logical delete, etc ...
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    # define method for access all queryset
    def get_archive(self):
        return super().get_queryset()

    # define method for access all active query
    def get_active_list(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    # define deleted item for easy access data
    def get_deleted_list(self):
        return super().get_queryset().filter(is_deleted=True)

    # define deactivate item
    def get_deactivate_list(self):
        return self.get_queryset().filter(is_active=False)
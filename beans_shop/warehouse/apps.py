from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WarehouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beans_shop.warehouse'
    verbose_name = _("Warehouse")

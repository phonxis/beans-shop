from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RestocksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beans_shop.restocks'
    verbose_name = _("Restocks")

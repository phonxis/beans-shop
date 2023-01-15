from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WriteOffsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beans_shop.write_offs'
    verbose_name = _("Write-offs")

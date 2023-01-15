from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from beans_shop.users.models import User


class ProductWeight(models.TextChoices):
    GRAM100 = "100gram", _("100 g")
    GRAM250 = "250gram", _("250 g")
    KILOGRAM1 = "1kg", _("1 kg")
    KILOGRAM2 = "2kg", _("2 kg")


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=256)
    weight = models.CharField(_("Weight"), max_length=64, choices=ProductWeight.choices, blank=True)
    count = models.IntegerField(_("Count"), default=0)
    expiration_dt = models.DateField(_("Expiration date"))
    created_dt = models.DateTimeField(_("Creating date"), auto_now_add=True)
    updated_dt = models.DateTimeField(_("Updating date"), auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.name} - {self.get_weight_display()} [{self.expiration_dt.strftime('%d %b, %Y')}]"


class ProductActionChoice(models.TextChoices):
    SELL = 'sell', _('Sell')
    CANCEL_ORDER = 'cancel_order', _('Cancel Order')
    RESTOCK = 'restock', _('Restock Beans&Dots')
    WASTE = 'waste', _('Waste (expired product)')


class ProductAction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="actions")
    action = models.CharField(_("Action"), max_length=128, choices=ProductActionChoice.choices)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="product_actions")
    previous_count = models.IntegerField(_("Previous count"))
    new_count = models.IntegerField(_("New count"))
    created_dt = models.DateTimeField(_("Creating date"), auto_now_add=True)
    comment = models.TextField(_("Comment"), blank=True)

    class Meta:
        verbose_name = _("Product Action")
        verbose_name_plural = _("Product Actions")

    def __str__(self):
        return self.action


class WarehouseSettings(SingletonModel):
    notification_expiration_days = models.IntegerField(_("Expiration notification (days)"), default=20)

    class Meta:
        verbose_name = _('Warehouse settings')
        verbose_name_plural = _('Warehouse settings')

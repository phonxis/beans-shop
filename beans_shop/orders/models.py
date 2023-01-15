from django.db import models
from django.utils.translation import gettext_lazy as _

from beans_shop.warehouse.models import Product


class Order(models.Model):
    comment = models.TextField(_("Comment"), blank=True)
    created_dt = models.DateTimeField(_("Creating date"), auto_now_add=True)
    updated_dt = models.DateTimeField(_("Updating date"), auto_now=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.created_dt)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_products")
    count = models.IntegerField(_("Count"), blank=False, null=False)

    class Meta:
        verbose_name = _("Order Product")
        verbose_name_plural = _("Order Product")

    def __str__(self):
        return str(self.product)

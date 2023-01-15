from django.contrib import admin, messages
from django.shortcuts import render
from django.contrib.admin.helpers import ActionForm
from django import forms
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin
from django.http import HttpResponseRedirect
from django.urls import reverse
from beans_shop.orders.models import Order

from beans_shop.warehouse.models import Product, ProductAction, WarehouseSettings


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "weight", "count", "expiration_dt")
    list_filter = ("weight",)
    search_fields = ("name",)
    actions = ['create_order']

    def create_order(self, request, queryset):
        opts = Order._meta
        redirect_url = reverse(
            "admin:%s_%s_add" % (opts.app_label, opts.model_name),
            current_app=self.admin_site.name,
        )

        products = []
        for product in queryset:
            products.append(f"product={product.id}")
        return HttpResponseRedirect(f"{redirect_url}?{'&'.join(products)}#/tab/inline_0/")

    create_order.short_description = _("Create order")


@admin.register(ProductAction)
class ProductActionAdmin(admin.ModelAdmin):
    list_display = ("action", "product", "user", "created_dt")
    list_filter = ("action", "product", "user")
    search_fields = ("product_name",)


@admin.register(WarehouseSettings)
class WarehouseSettingsAdmin(SingletonModelAdmin):
    ...

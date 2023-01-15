from django.contrib import admin

from beans_shop.orders.models import Order, OrderProduct
from beans_shop.warehouse.models import ProductActionChoice, ProductAction


class OrderProductAdminInline(admin.TabularInline):
    model = OrderProduct
    extra = 1
    min_num = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

    def get_extra(self, request, obj=None, **kwargs):
        extra = super().get_extra(request, obj, **kwargs)
        products = request.GET.getlist('product', [])
        if products:
            extra = len(products)
        return extra

    def get_min_num(self, request, obj=None, **kwargs):
        min_num = super().get_extra(request, obj, **kwargs)
        products = request.GET.getlist('product', [])
        if products:
            min_num = len(products)
        return min_num


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductAdminInline,)

    def log_addition(self, request, obj, message):

        for order_product in obj.order_products.all():

            previous_count = order_product.products.count
            new_count = previous_count - order_product.count
            order_product.product.count = new_count
            order_product.product.save()

            ProductAction.objects.create(
                product=order_product.product,
                action=ProductActionChoice.SELL.value,
                user=request.user,
                previous_count=previous_count,
                new_count=new_count,
                comment=order_product.order.comment
            )

        return super().log_addition(request, obj, message)

    def get_formset_kwargs(self, request, obj, inline, prefix):
        formset_params = super().get_formset_kwargs(request, obj, inline, prefix)

        if not obj.id and isinstance(inline, OrderProductAdminInline):
            products = request.GET.getlist('product', [])
            if products:
                initial = []
                for product in products:
                    initial.append({"product": product})
                formset_params.update({"initial": initial})

        return formset_params

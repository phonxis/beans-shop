from rest_framework import serializers

from beans_shop.warehouse.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "weight",
            "count",
            "expiration_dt",
        )

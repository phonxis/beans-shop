import logging
from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response

from beans_shop.api.serializers import ProductSerializer
from beans_shop.api.viewsets import PublicViewSet
from beans_shop.warehouse.models import WarehouseSettings, Product

logger = logging.getLogger(__name__)


class ProjectCheckAutoupdateView(PublicViewSet):
    def exp_products(self, request, *args, **kwargs):
        notification_expiration_days = WarehouseSettings.get_solo().notification_expiration_days
        exp_date = timezone.now() + timedelta(days=notification_expiration_days)
        exp_products = Product.objects.filter(expiration_dt__lte=exp_date)
        data = ProductSerializer(exp_products, many=True).data
        return Response(status=status.HTTP_200_OK, data=data)

from django.urls import include, path

from beans_shop.api.views import ProjectCheckAutoupdateView

app_name = "api"

urlpatterns = [
    path(
        "v1/expired_products/",
        ProjectCheckAutoupdateView.as_view({"get": "exp_products"}, name="expired_products_list")
    ),
]

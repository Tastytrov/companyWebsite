from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("shop/", views.ShopView.as_view(), name="shop_view"),
]
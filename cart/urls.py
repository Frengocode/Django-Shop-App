from django.urls import path
from .views import AddProductToCartView, GetCartItems, RemoveProductFromCartView


urlpatterns = [
    path(
        "add-product-to-cart/<int:pk>/",
        AddProductToCartView.as_view(),
        name="adding-product-to-cart",
    ),
    path("get-carts/", GetCartItems.as_view(), name="get-cart-items"),
    path(
        "remove-cart/<int:pk>/",
        RemoveProductFromCartView.as_view(),
        name="remove-product-from-cart-item",
    ),
]

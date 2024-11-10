from django.urls import path
from .views import (
    ListOFProducts,
    CreateProductView,
    ProductDetailView,
    SearchProductView,
    UpdateProductView,
    DeleteProductView,
)


urlpatterns = [
    path("", ListOFProducts.as_view(), name="home"),
    path("create-product/", CreateProductView.as_view(), name="creating-product"),
    path("product-detail/<int:pk>/", ProductDetailView.as_view(), name="get-product"),
    path(
        "search-product-by-title/", SearchProductView.as_view(), name="search-product"
    ),
    path(
        "update-product/<int:pk>/", UpdateProductView.as_view(), name="update-product"
    ),
    path(
        "delete-product/<int:pk>/",
        DeleteProductView.as_view(),
        name="delete-user-product",
    ),
]

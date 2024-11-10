from django.urls import path
from .views import CreateOrderView, GetOrders, OrderDetailView


urlpatterns = [
    path("create-order/", CreateOrderView.as_view(), name="create-order"),
    path("get-orders/", GetOrders.as_view(), name="my-orders"),
    path("get-order/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]

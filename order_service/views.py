from django.shortcuts import redirect
from .models import OrderModel, CartModel
from django.views.generic import View, TemplateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db import transaction
from typing import Any


@method_decorator(login_required, name="dispatch")
class CreateOrderView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        cart_items = CartModel.objects.filter(
            user=request.user, is_ready_to_order=False
        )

        if not cart_items.exists():
            messages.error(request, "No items in your cart to create an order.")
            return redirect("get-cart-items")

        with transaction.atomic():
            order = OrderModel.objects.create(user=request.user)
            order.cart.add(*cart_items)

            cart_items.update(is_ready_to_order=True)

            return redirect("my-orders")


@method_decorator(login_required, name="dispatch")
class GetOrders(TemplateView):
    template_name = "order/get_orders.html"

    def get_context_data(self, **kwargs: transaction) -> dict[str, Any]:
        context = super().get_context_data()
        context["orders"] = OrderModel.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name="dispatch")
class OrderDetailView(DetailView):
    model = OrderModel
    template_name = "order/order_detail.html"
    context_object_name = "order"

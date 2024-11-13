from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import ProductModel, CartModel
from django.views.generic import View, ListView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib import messages


@method_decorator(login_required, name="dispatch")
class AddProductToCartView(View):
    model = ProductModel

    def get(
        self, request: HttpRequest, pk: int, *args: str, **kwargs: Any
    ) -> HttpResponse:
        product = ProductModel.objects.get(pk=pk)

        existing_cart_item = CartModel.objects.filter(
            user=request.user, product=product, is_ready_to_order=False
        ).first()

        if existing_cart_item:
            return redirect("get-product", pk=pk)

        if existing_cart_item:
            messages.error(request, "This product is already in your cart.")

        new_cart = CartModel(user=request.user, product=product)
        new_cart.save()
        messages.success(request, "Product added to cart successfully.")
        return redirect("get-cart-items")


@method_decorator(login_required, name="dispatch")
class GetCartItems(ListView):

    model = CartModel
    template_name = "cart/get_carts.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context["cart_items"] = CartModel.objects.filter(
            user=self.request.user, is_ready_to_order=False
        )
        return context


@method_decorator(login_required, name="dispatch")
class RemoveProductFromCartView(DeleteView):
    model = CartModel
    success_url = "/cart/"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        cart_obj = CartModel.objects.get(pk=kwargs["pk"], user=request.user)
        cart_obj.delete()
        messages.success(request, "Product removed from cart successfully.")
        return redirect("get-cart-items")







from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import ProductModel
from django.contrib.auth.decorators import login_required
from .forms import CreateProductForm, SearchForm
from django.shortcuts import render
from django.contrib import messages


@method_decorator(login_required, name="dispatch")
class SearchProductView(TemplateView):
    template_name = "product/search.html"

    def get(
        self, request: HttpRequest, *args: reverse_lazy, **kwargs: reverse_lazy
    ) -> HttpResponse:

        form = SearchForm(request.GET or None)
        search_result = None
        if form.is_valid():
            search = form.cleaned_data["search"]
            search_result = ProductModel.objects.filter(product_title__icontains=search)

        return render(
            request, self.template_name, {"form": form, "result": search_result}
        )


@method_decorator(login_required, name="dispatch")
class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    context_object_name = "product"
    model = ProductModel


@method_decorator(name="dispatch", decorator=login_required)
class ListOFProducts(ListView):
    template_name = "product/get_products.html"
    model = ProductModel
    context_object_name = "products"


@method_decorator(login_required, name="dispatch")
class CreateProductView(CreateView):
    model = ProductModel
    form_class = CreateProductForm
    template_name = "product/create_product.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        product = form.save() 

        self.request.user.products.add(product)
        self.request.user.save()

        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class UpdateProductView(UpdateView):
    template_name = "product/update_product.html"
    model = ProductModel
    form_class = CreateProductForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        if not queryset.exists():
            messages.error(self.request, "No products found.")
        return queryset

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("get-product", kwargs={"pk": pk})


@method_decorator(login_required, name="dispatch")
class DeleteProductView(DeleteView):
    model = ProductModel
    template_name = "product/delete_product.html"
    success_url = reverse_lazy("get-current-user")

    def get_queryset(self):
        return ProductModel.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Product deleted successfully.")
        return super().delete(request, *args, **kwargs)

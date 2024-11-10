from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import SignUpForm, UploadProfilePictureForm
from django.views.generic import CreateView, FormView, DetailView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ProductModel
from typing import Any


@method_decorator(login_required, name="dispatch")
class UploadProfilePictureView(FormView):
    template_name = "user/update_profile_picture.html"
    success_url = reverse_lazy("user-me")
    form_class = UploadProfilePictureForm

    def get(
        self, request: HttpRequest, *args: str, **kwargs: reverse_lazy
    ) -> HttpResponse:
        return render(request, self.template_name, {"form": self.form_class})

    def post(
        self, request: HttpRequest, *args: str, **kwargs: reverse_lazy
    ) -> HttpResponse:
        user_profile_picture, created = CustomUser.objects.get_or_create(
            username=request.user
        )

        if not created and user_profile_picture.profile_picture:
            messages.success(request, "")

        form = UploadProfilePictureForm(
            request.POST, request.FILES, instance=user_profile_picture
        )
        if form.is_valid():
            new_photo_ = form.save(commit=False)
            new_photo_.user = request.user
            new_photo_.save()
            return redirect("home")


@method_decorator(login_required, name="dispatch")
class GetUser(DetailView):
    context_object_name = "user"
    model = CustomUser
    template_name = "user/user_detail.html"


class SignUpView(CreateView):
    template_name = "user/sign_up.html"
    success_url = reverse_lazy("login")
    model = CustomUser
    form_class = SignUpForm


@method_decorator(login_required, name="dispatch")
class UserMeView(TemplateView):
    template_name = "user/user_me.html"

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, Any]:
        context = super().get_context_data()
        context["products"] = ProductModel.objects.filter(user=self.request.user)
        return context

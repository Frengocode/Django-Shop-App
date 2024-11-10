from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    template_name = "auth/login.html"
    http_method_names = "get, post"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if not user:
            return render(request, "auth/error.html")
        else:
            login(request, user=user)
            return redirect("/")


def logout_user(request):
    logout(request)
    return redirect("login")

from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def register(request) -> HttpResponse:
    context = {}
    return render(request, "accounts/register.html", context)


def login(request) -> HttpResponse:
    context = {}
    return render(request, "accounts/login.html", context)


def logout(request) -> HttpResponse:
    return redirect("index")


def dashboard(request) -> HttpResponse:
    context = {}
    return render(request, "accounts/dashboard.html", context)

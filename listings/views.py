from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "listings/listings.html")


def listing(request) -> HttpResponse:
    return render(request, "listings/listing.html")


def search(request) -> HttpResponse:
    return render(request, "listings/search.html")

from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing


# Create your views here.
def index(request) -> HttpResponse:
    listings = Listing.objects.order_by("-list_date")
    listings = listings.filter(is_published=True)[:3]

    context = {
        "listings": listings,
    }

    return render(request, "pages/index.html", context)


def about(request) -> HttpResponse:
    return render(request, "pages/about.html")

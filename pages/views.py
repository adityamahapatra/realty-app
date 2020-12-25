from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


# Create your views here.
def index(request) -> HttpResponse:
    listings = Listing.objects.order_by("-list_date")
    listings = listings.filter(is_published=True)[:3]

    context = {
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
    }

    return render(request, "pages/index.html", context)


def about(request) -> HttpResponse:
    # Get all the realtors
    realtors = Realtor.objects.order_by("-hire_date")

    # Get the MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors,
    }

    return render(request, "pages/about.html", context)

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Listing


# Create your views here.
def index(request) -> HttpResponse:
    listings = Listing.objects.order_by("-list_date")
    paginator = Paginator(listings, 3)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings,
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id: int) -> HttpResponse:
    return render(request, "listings/listing.html")


def search(request) -> HttpResponse:
    return render(request, "listings/search.html")

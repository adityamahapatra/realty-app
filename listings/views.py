from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings,
    }
    return render(request, "listings/listings.html", context)


def listing(request: HttpRequest, listing_id: int) -> HttpResponse:
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing,
    }

    return render(request, "listings/listing.html", context)


def search(request: HttpRequest) -> HttpResponse:
    query_set_list = Listing.objects.order_by("-list_date")

    # Keywords
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            query_set_list = query_set_list.filter(
                description__icontains=keywords
            )

    # City
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            query_set_list = query_set_list.filter(city__iexact=city)

    # State
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            query_set_list = query_set_list.filter(state__iexact=state)

    # Bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)

    # Price
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            query_set_list = query_set_list.filter(price__lte=price)

    context = {
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "listings": query_set_list,
        "values": request.GET,
    }

    return render(request, "listings/search.html", context)

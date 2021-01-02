from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from .models import Contact


# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        # Check if the user has already made an inquiry about a property.
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id
            )
            if has_contacted:
                messages.error(
                    request,
                    "You have already made an inquiry for this listing"
                )
                return redirect(f"/listings/{listing_id}")

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )

        contact.save()

        # Send an email to the realtor whenever an inquiry is posted.
        send_mail(
            subject="BT Realty Property Inquiry",
            message=f"New inquiry for {listing}. Sign in for more info.",
            from_email="bantai.realestate@gmail.com",
            recipient_list=[realtor_email],
            fail_silently=False
        )

        messages.success(
            request,
            "Your request has been submitted. A realtor will get back to you \
                soon"
        )
        return redirect(f"/listings/{listing_id}")

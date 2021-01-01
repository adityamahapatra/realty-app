from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def register(request) -> HttpResponse:
    if request.method == "POST":
        # Get values from the registration form.
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Check if the passwords match.
        if password == confirm_password:
            # Check if the username already exists.
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, f"The username '{username}' already exists."
                )
                return redirect("register")
            # Check if the email is already in use.
            elif User.objects.filter(email=email).exists():
                messages.error(
                    request, f"The email '{email}' is already in use."
                )
                return redirect("register")
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                # Log in the user after registration is successful.
                user.save()
                auth.login(request, user)
                messages.success(request, "Registration successful!")
                return redirect("index")
        else:
            messages.error(request, "The passwords do not match")
            return redirect("register")
    else:
        context = {}
        return render(request, "accounts/register.html", context)


def login(request) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successful")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request) -> HttpResponse:
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Logged out succesfully.")
        return redirect("index")


def dashboard(request) -> HttpResponse:
    context = {}
    return render(request, "accounts/dashboard.html", context)

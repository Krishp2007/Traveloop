from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpForm


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("travel:dashboard")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome to Traveloop. Your account is ready.")
            return redirect("travel:dashboard")
    else:
        form = SignUpForm()
    return render(request, "travel/auth/signup.html", {"form": form})

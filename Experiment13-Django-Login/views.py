
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        username_pattern = r'^[A-Za-z0-9_]{4,20}$'
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$'

        if not re.fullmatch(username_pattern, username):
            messages.error(request, "Invalid username format.")

        elif not re.fullmatch(password_pattern, password):
            messages.error(request, "Password must have at least 8 characters, including uppercase, lowercase and a number.")

        else:
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("success")
            else:
                messages.error(request, "Incorrect username or password.")

    return render(request, "login.html")


@login_required
def success_view(request):
    return render(request, "success.html")

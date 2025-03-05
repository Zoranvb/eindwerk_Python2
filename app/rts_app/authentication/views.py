from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Stuur door naar de homepage of dashboard
        else:
            return render(request, "authentication/login.html", {"error": "Invalid credentials"})
    return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Na registratie naar login
    else:
        form = RegisterForm()
    return render(request, "authentication/register.html", {"form": form})

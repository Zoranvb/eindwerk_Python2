from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rts_app.forms.loginform import LoginForm

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "authentication/login.html", {"form": form, "error": "Ongeldige gebruikersnaam of wachtwoord."})
    else:
        form = LoginForm()
    return render(request, "authentication/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")

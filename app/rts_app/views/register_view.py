from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log de gebruiker direct in na registratie
            return redirect('home')  # Pas dit aan naar je eigen homepagina
    else:
        form = UserCreationForm()
    
    return render(request, 'authentication/register.html', {'form': form})

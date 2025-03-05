from django.shortcuts import render, redirect

def home(request):  # Zorg ervoor dat 'request' wordt meegegeven als argument
    if not request.user.is_authenticated:
        return redirect('login')  # Als de gebruiker niet ingelogd is, redirecten naar de loginpagina
    
    return render(request, "homepage.html")  # Geef de homepagina weer

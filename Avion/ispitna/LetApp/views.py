from django.shortcuts import render, redirect
from .models import Pilot,AirlinePilot,Balloon,Airline,Flight
from .forms import FlightForm
# Create your views here.

def index(request):

    return render(request, "index.html")

def flight(request):

    if request.method == "POST":
        form_data = FlightForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            flight = form_data.save(commit=False)
            flight.user = request.user
            flight.save()
            return redirect("flight")

    qs = Flight.objects.filter(user=request.user, aerodrom_From="Skopje",).all()

    return render(request, "flights.html",  {"flights": qs, "form": FlightForm, })

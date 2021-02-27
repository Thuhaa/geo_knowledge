from django.shortcuts import render
from .models import WorldCountries

def homepage_view(request):
	world_countries = WorldCountries.objects.all()

	return render(request, 'countries/homepage.html')
# Create your views here.

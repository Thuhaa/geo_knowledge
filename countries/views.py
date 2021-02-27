from django.shortcuts import render
from .models import WorldCountries
from django.core.serializers import serialize
import json



def homepage_view(request):
	countries = serialize('geojson', WorldCountries.objects.all(),
          geometry_field='geom',
          fields=('cntry_name','objectid'))
	countries_json = json.loads(countries)
	print(type(countries_json))
	return render(request, 'countries/homepage.html', {'countries_json':countries_json})


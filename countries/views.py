from django.shortcuts import render
from .models import WorldBorder
from django.core.serializers import serialize
import json



def homepage_view(request):
	'''
	This is the homepage view(for now). This view will be grabbing countries data, serializing it, and
	passing it as a dict to the views in readiness for the conversion of the dict to json, including
	rendering the homepage.html file
	'''

	# Grab the countries data and serialize
	countries = serialize('geojson', WorldBorder.objects.all(),
          geometry_field='geom',
          fields=('objectid','name'))

	# Convert the countries data to a python dict and pass it in the context variable
	countries_json = json.loads(countries)
	return render(request, 'countries/homepage.html', {'countries_json':countries_json})


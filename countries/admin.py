#from django.contrib import admin
from django.contrib.gis import admin
from .models import WorldCountries

admin.site.register(WorldCountries, admin.GeoModelAdmin)
# Register your models here.

#from django.contrib import admin
from django.contrib.gis import admin
from .models import WorldBorders

admin.site.register(WorldBorders, admin.GeoModelAdmin)
# Register your models here.

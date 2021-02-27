#from django.db import models
from django.contrib.gis.db import models
class WorldCountries(models.Model):
    objectid = models.IntegerField()
    cntry_name = models.CharField(max_length=39)
    geom = models.MultiPolygonField()


    def __str__(self):
    	return self.cntry_name

    class Meta:
    	verbose_name_plural = 'World Countries'

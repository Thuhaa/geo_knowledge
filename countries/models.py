#from django.db import models

# This model was generated automatically with the python manage.py ogrinspect command
# Note that the models module has been imported from the django.contrib.gis.db
from django.contrib.gis.db import models

class WorldBorder(models.Model):
    objectid = models.BigIntegerField()
    name = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)


    
    def __str__(self):
    	'''
    	This function ensures that the name of the class instances are referenced by their names(cntry_names)
    	'''
    	return self.name


    # This class ensures that the right plural(in this case) is used
    class Meta:
    	verbose_name_plural = 'World Borders'

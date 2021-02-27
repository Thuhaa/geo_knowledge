from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldCountries


worldcountries_mapping = {
    'objectid': 'OBJECTID',
    'cntry_name': 'CNTRY_NAME',
    'geom': 'MULTIPOLYGON',
}

world_shp = Path(__file__).resolve().parent / 'data' / 'World_Countries' / 'world_countries.shp'

def run(verbose=True):
    lm = LayerMapping(WorldCountries, str(world_shp), worldcountries_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
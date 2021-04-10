from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorders


worldborders_mapping = {
    'objectid': 'OBJECTID',
    'cntry_name': 'CNTRY_NAME',
    'geom': 'MULTIPOLYGON',
}

world_shp = Path(__file__).resolve().parent / 'data' / 'world' / 'world.shp'

def run(verbose=True):
    lm = LayerMapping(WorldBorders, str(world_shp), worldborders_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
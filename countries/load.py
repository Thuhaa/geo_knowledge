from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder


worldborder_mapping = {
    'objectid': 'OBJECTID',
    'name': 'name',
    'geom': 'MULTIPOLYGON',
}

world_shp = Path(__file__).resolve().parent / 'data' / 'world' / 'world.shp'

def run(verbose=True):
    lm = LayerMapping(WorldBorder, str(world_shp), worldborder_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
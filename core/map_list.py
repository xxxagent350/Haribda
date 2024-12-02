from models.world_objects.map import Map
from DB_operators.maps_saver import load_maps_from_file

maps = {}

try:
    maps = load_maps_from_file("maps.json")
except:
    maps[0] = Map()

if len(maps) == 0:
    maps[0] = Map()

import asyncio

from models.world_objects.map import Map
from DB_operators.maps_saver import load_maps_from_file
from core.map_list import maps


try:
    maps = load_maps_from_file("maps.json")
except Exception as exception:
    maps = {0 : Map()}
    print(f'Ошибка загрузки карт из maps.json: {exception}')

if len(maps) == 0:
    maps[0] = Map()

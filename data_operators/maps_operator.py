import asyncio
import os
from random import randint

from core.vector2 import Vector2
from data_operators import pickle_operator
from variables.maps_dict import maps
from models.map import Map
from models.world_objects.monster import Monster
from settings import global_settings

saved_maps_path = os.path.join(global_settings.data_path, 'maps.pkl')


def save_maps():
    success, exception = pickle_operator.try_save_data(maps, saved_maps_path)
    if success:
        print("Карты успешно сохранены")
    else:
        print(f"Ошибка сохранения карт: {exception}")

def load_maps():
    loaded_data, exception = pickle_operator.try_load_data(saved_maps_path)
    if loaded_data is not None:
        print("Карты успешно загружены")
        maps.update(loaded_data)
    else:
        print(f"Ошибка загрузки карт: {exception}")
        try:
            if os.path.exists(saved_maps_path):
                file_name, file_extension = os.path.splitext(saved_maps_path)
                damaged_file_path = f"{file_name}(damaged){file_extension}"
                os.rename(saved_maps_path, damaged_file_path)
                print(f'Повреждённый файл переименован в {damaged_file_path}')
        except Exception as exception:
            input(f'Непредвиденная ошибка при создании резервной копии файла с картами: {exception}. Если вы хотите пересоздать файл с сохранёнными картами(в этом случае данные предыдущего будут БЕЗВОЗВРАТНО ПОТЕРЯНЫ), нажмите enter')

        test_map = Map()
        for i in range(10000):
            x = randint(-500, 500)
            y = randint(-50, 50)
            if test_map.check_if_square_is_free(Vector2(x, y)):
                test_map.add_new_object(Monster(Vector2(x, y), 0, "gorinych", max_hp=30, agr_range=3, view_range=4, updates_to_move=2))
        maps.update({0 : test_map})
        save_maps()
        print('Создан новый список карт')

from os import path
from aiogram import types
from project_path import get_global_path

def get_image_path_from_ship_name(ship_name):
    # Определяем корневую папку проекта (там, где лежит основной файл проекта)
    return get_global_path(path.join('sprites', 'ships', f'{ship_name}.png'))

def get_image_from_ship_name(ship_name):
    image_path = get_image_path_from_ship_name(ship_name)
    return types.FSInputFile(image_path)

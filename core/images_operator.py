from os import path

import cv2
from aiogram import types
from project_path import get_global_path

cached_cv2_images = dict() # key - путь, value - изображение


def get_cv2_image_from_path(path_):
    if path_ in cached_cv2_images:
        return cached_cv2_images[path_]
    else:
        cached_cv2_images[path_] = cv2.imread(path_, cv2.IMREAD_UNCHANGED)  # Чтение с альфа-каналом
        return get_cv2_image_from_path(path_)

def get_image_path_from_ship_name(ship_name):
    # Определяем корневую папку проекта (там, где лежит основной файл проекта)
    return get_global_path(path.join('sprites', 'ships', f'{ship_name}.png'))

def get_image_path_from_monster_name(monster_name):
    # Определяем корневую папку проекта (там, где лежит основной файл проекта)
    return get_global_path(path.join('sprites', 'monsters', f'{monster_name}.png'))

def get_ship_image_from_name(ship_name):
    image_path = get_image_path_from_ship_name(ship_name)
    return get_cv2_image_from_path(image_path)

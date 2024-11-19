from os import path
from aiogram import types

def get_image_path_from_ship_name(ship_name):
    return path.join('sprites', 'ships', f'{ship_name}.png')

def get_image_from_ship_name(ship_name):
    image_path = get_image_path_from_ship_name(ship_name)
    return types.FSInputFile(image_path)

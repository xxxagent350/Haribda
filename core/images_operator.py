from os import path
from aiogram import types

def get_image_path_from_ship_name(ship_name):
    return path.join('sprites', 'ships', f'{ship_name}.png')

def get_image_from_card_id(card_num):
    image_path = get_image_path_from_ship_name(card_num)
    return types.FSInputFile(image_path)

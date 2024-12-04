import math
import time
import cv2
import numpy as np
from aiogram import types
import random
import asyncio

from UI import inline_keyboard_buttons
from core import images_operator
from core.map_list import maps
from core.user_list import users_id
from core.vector2 import Vector2
from models.world_objects.ship import Ship
from network.async_messages_operator import try_delete_message
from variables.bot import bot
from settings.global_settings import render_out_of_border_range
from network import async_messages_operator

def create_background(width, height, color=(252, 141, 56)):  # RGB вместо HEX
    """Создание фона."""
    return np.full((height, width, 3), color, dtype=np.uint8)


def render_visible_objects(base_image, map_, player_ship):
    """Добавление видимых объектов на изображение."""
    full_view_range = player_ship.view_range + render_out_of_border_range
    min_visible_pos = player_ship.position.summ(Vector2(-full_view_range, -full_view_range))
    max_visible_pos = player_ship.position.summ(Vector2(full_view_range, full_view_range))
    resolution = base_image.shape[0]
    pixels_in_cell = resolution / (player_ship.view_range * 2 + 1)

    for object_ in map_.objects:
        # Проверка на то, находиться ли объект в поле видимости
        if min_visible_pos.x <= object_.position.x <= max_visible_pos.x and min_visible_pos.y <= object_.position.y <= max_visible_pos.y:
            relative_cells_pos = object_.position.summ(Vector2(-player_ship.position.x, -player_ship.position.y))
            pixels_pos = Vector2(relative_cells_pos.x * pixels_in_cell, -relative_cells_pos.y * pixels_in_cell).summ(Vector2(resolution / 2, resolution / 2))
            add_object(base_image, object_, pixels_pos, object_.rotation, pixels_in_cell)


def add_object(base_image, object_, position, rotation, pixels_in_cell):
    """Рендерит один отдельный объект с указанными позицией в пикселях(0, 0 = левый верхний угол) и поворотом в градусах"""
    object_type = type(object_)

    if object_type == Ship:
        # Получаем изображение корабля в нужном формате
        ship_img = images_operator.get_cv2_image_from_path(object_.image_path)

        # Масштабируем изображение корабля
        additive_scale = 1.1  # Дополнительное увеличение изображения (если хотите чтобы картинка слегка вылазила за грани ячейки)
        scale = pixels_in_cell / max(ship_img.shape[0], ship_img.shape[1])

        add_image(base_image, ship_img, position, rotation, scale * additive_scale)


def add_image(base_image, image, position, rotation=0, scale=1.0):
    """
    Добавляет изображение на base_image с учетом позиции, поворота и масштаба.

    :param base_image: Основное изображение (numpy array).
    :param image: Накладываемое изображение (numpy array с альфа-каналом).
    :param position: Центр наложения Vector2(x, y) на base_image.
    :param rotation: Угол поворота (в градусах).
    :param scale: Масштаб изображения.
    """
    # Убедимся, что изображение с альфа-каналом
    if image.shape[2] != 4:
        raise ValueError("Изображение должно содержать альфа-канал (4 канала)")

    # Масштабируем изображение
    new_size = (int(image.shape[1] * scale), int(image.shape[0] * scale))
    scaled_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LANCZOS4)

    # Поворачиваем изображение
    center = (scaled_image.shape[1] // 2, scaled_image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation, 1)
    rotated_image = cv2.warpAffine(
        scaled_image,
        rotation_matrix,
        (scaled_image.shape[1], scaled_image.shape[0]),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0, 0, 0, 0)
    )

    # Определяем позиции вставки
    x, y = int(position.x - rotated_image.shape[1] / 2), int(position.y - rotated_image.shape[0] / 2)

    # Убедимся, что координаты вставки не выходят за границы base_image
    x_start, x_end = max(0, x), min(base_image.shape[1], x + rotated_image.shape[1])
    y_start, y_end = max(0, y), min(base_image.shape[0], y + rotated_image.shape[0])

    # Рассчитываем координаты для cropped region
    crop_x_start = max(0, -x)
    crop_x_end = crop_x_start + (x_end - x_start)
    crop_y_start = max(0, -y)
    crop_y_end = crop_y_start + (y_end - y_start)

    # Извлекаем альфа-канал и выполняем наложение
    alpha = rotated_image[crop_y_start:crop_y_end, crop_x_start:crop_x_end, 3] / 255.0
    for c in range(3):  # Каналы RGB
        base_image[y_start:y_end, x_start:x_end, c] = (
            alpha * rotated_image[crop_y_start:crop_y_end, crop_x_start:crop_x_end, c] +
            (1 - alpha) * base_image[y_start:y_end, x_start:x_end, c]
        )


def add_grid(
    base_image,
    cell_count,
    grid_thickness_ratio=0.002,  # Толщина линий относительно ширины изображения
    grid_color=(0, 0, 0, 100),  # Цвет сетки (RGBA)
    text_color=(0, 0, 0, 100),  # Цвет текста (RGBA)
    font_scale_ratio=0.001,  # Размер текста относительно ширины изображения
    font_thickness_ratio=0.0025,  # Толщина текста относительно ширины изображения
    text_offset_ratio=0.005  # Отступ текста от границ изображения
):
    """Добавление сетки с буквами и цифрами на изображение."""
    height, width = base_image.shape[:2]
    cell_width = width // cell_count
    cell_height = height // cell_count

    # Абсолютные значения для толщины линий, размера и толщины текста
    grid_thickness = max(1, int(grid_thickness_ratio * width))
    font_scale = font_scale_ratio * width
    font_thickness = max(1, int(font_thickness_ratio * width))
    text_offset = int(text_offset_ratio * width)

    # Создаем временные слои
    grid_layer = base_image.copy()
    text_layer = base_image.copy()

    # Рисуем линии сетки
    for i in range(1, cell_count):
        x = i * cell_width
        y = i * cell_height

        # Вертикальные линии
        cv2.line(grid_layer, (x, 0), (x, height), grid_color[:3], grid_thickness, lineType=cv2.LINE_AA)

        # Горизонтальные линии
        cv2.line(grid_layer, (0, y), (width, y), grid_color[:3], grid_thickness, lineType=cv2.LINE_AA)

    # Добавляем текст (буквы сверху и снизу, цифры слева и справа)
    for i in range(cell_count):
        letter = chr(65 + i)  # Генерация букв 'A', 'B', ...
        number = str(i + 1)   # Цифры от 1 до cell_count

        # Позиции текста
        letter_x = int(i * cell_width + cell_width / 2)
        letter_top_y = text_offset
        letter_bottom_y = height - text_offset

        number_y = int(i * cell_height + cell_height / 2)
        number_left_x = text_offset
        number_right_x = width - text_offset

        # Центровка текста по границе
        letter_size = cv2.getTextSize(letter, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
        number_size = cv2.getTextSize(number, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]

        # Рисуем буквы сверху и снизу
        cv2.putText(
            text_layer, letter,
            (letter_x - letter_size[0] // 2, letter_top_y + letter_size[1]),
            cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color[:3], font_thickness, lineType=cv2.LINE_AA
        )
        cv2.putText(
            text_layer, letter,
            (letter_x - letter_size[0] // 2, letter_bottom_y),
            cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color[:3], font_thickness, lineType=cv2.LINE_AA
        )

        # Рисуем цифры слева и справа
        cv2.putText(
            text_layer, number,
            (number_left_x, number_y + number_size[1] // 2),
            cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color[:3], font_thickness, lineType=cv2.LINE_AA
        )
        cv2.putText(
            text_layer, number,
            (number_right_x - number_size[0], number_y + number_size[1] // 2),
            cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color[:3], font_thickness, lineType=cv2.LINE_AA
        )

    # Накладываем сетку с ее прозрачностью
    grid_alpha = grid_color[3] / 255.0
    cv2.addWeighted(grid_layer, grid_alpha, base_image, 1 - grid_alpha, 0, base_image)

    # Накладываем текст с его прозрачностью
    text_alpha = text_color[3] / 255.0
    cv2.addWeighted(text_layer, text_alpha, base_image, 1 - text_alpha, 0, base_image)


def get_user_map_image(user):
    start_time = time.perf_counter()
    if user.current_map is not None:
        map_ = maps[user.current_map]
    else:
        raise Exception(f'Невозможно сгенерировать изображение карты пользователю {user.name}, так как user.current_map == None')

    # Задаём размер карты
    resolution = 1024
    cells_num = (user.controlled_ship.view_range * 2) + 1  # Количество клеток на карте

    # Создаем фон
    base_image = create_background(resolution, resolution)

    # Отрисовываем видимые игроку объекты на карте
    render_visible_objects(base_image, map_, user.controlled_ship)

    # Добавляем сетку
    add_grid(base_image, cells_num)

    # Преобразуем изображение
    _, buffer = cv2.imencode('.png', base_image)
    image_bytes = buffer.tobytes()

    print(f'Время генерации картинки карты: {(time.perf_counter() - start_time) * 1000:.1f} мс')
    return types.BufferedInputFile(image_bytes, filename="map.png")


async def update_map_message_of_user(user, dont_update_map_image = False, iteration_num = 0):
    """
    Генерация карты и отправка пользователю
    :param user: Пользователь которому обновить сообщение с картой
    :param dont_update_map_image: При True не обновляет изображение карты(полезно если нужно обновить только кнопки или текст)
    :param iteration_num: Номер попытки, нужен для предотвращения бесконечного цикла
    """
    if iteration_num > 5:
        return

    # Проверяем заданы ли у юзера корабль и карта
    if user.controlled_ship is None:
        print(f"Невозможно отобразить карту игроку {user.name}, так как у него не задан controlled_ship")
        return
    if user.current_map is None:
        print(f"Невозможно отобразить карту игроку {user.name}, так как у него не задан current_map")
        return

    if not dont_update_map_image:
        map_image = get_user_map_image(user)
    else:
        map_image = None

    # Проверяем есть ли у игрока ожидаемые действия и если да то отображаем кнопку отмены
    if not maps[user.current_map].check_if_object_has_delayed_actions(user.controlled_ship):
        new_reply_markup=inline_keyboard_buttons.ship_control_buttons
    else:
        new_reply_markup=inline_keyboard_buttons.cancel_button

    result, new_message_id = await async_messages_operator.try_strong_edit_message_media(chat_id=user.id, message_id=user.map_message_id, new_photo=map_image, new_caption="Это карта", new_reply_markup=new_reply_markup)
    if result:
        if user.map_message_id != new_message_id:
            asyncio.create_task(try_delete_message(user.id, user.map_message_id))
            user.map_message_id = new_message_id
    else:
        await try_delete_message(user.id, new_message_id)
        user.map_message_id = None
        asyncio.create_task(update_map_message_of_user(user, iteration_num=iteration_num + 1))
        print(f"Неудача изменения сообщения с картой, генерирую и высылаю заново({iteration_num})...")

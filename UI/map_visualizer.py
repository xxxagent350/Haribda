import time
import cv2
import numpy as np
from aiogram import types
import random
import asyncio
from core import images_operator
from core.vector2 import Vector2
from variables.bot import bot


def create_background(width, height, color=(56, 141, 252)):  # RGB вместо HEX
    """Создание фона."""
    return np.full((height, width, 3), color, dtype=np.uint8)


def add_ship(base_image, ship_image_path, position, scale=1.0, rotation=0):
    """Добавление корабля на изображение."""
    ship_img = cv2.imread(ship_image_path, cv2.IMREAD_UNCHANGED)  # Чтение с альфа-каналом
    if ship_img is None:
        raise FileNotFoundError(f"Файл {ship_image_path} не найден")

    # Масштабируем изображение корабля
    if scale != 1.0:
        new_size = (int(ship_img.shape[1] * scale), int(ship_img.shape[0] * scale))
        ship_img = cv2.resize(ship_img, new_size, interpolation=cv2.INTER_LANCZOS4)

    # Поворот изображения
    if rotation != 0:
        center = (ship_img.shape[1] // 2, ship_img.shape[0] // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, rotation, 1)
        ship_img = cv2.warpAffine(ship_img, rotation_matrix, (ship_img.shape[1], ship_img.shape[0]),
                                  flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))

    # Определяем позицию для наложения
    x, y = int(position[0] - ship_img.shape[1] / 2), int(position[1] - ship_img.shape[0] / 2)

    # Наложение корабля с учетом альфа-канала
    alpha = ship_img[:, :, 3] / 255.0  # Нормализованный альфа-канал
    for c in range(3):  # Каналы RGB
        base_image[y:y + ship_img.shape[0], x:x + ship_img.shape[1], c] = (
            alpha * ship_img[:, :, c] + (1 - alpha) * base_image[y:y + ship_img.shape[0], x:x + ship_img.shape[1], c]
        )


def add_grid(base_image, cell_count, grid_thickness=2, grid_color=(0, 0, 0)):
    """Добавление сетки на изображение."""
    height, width = base_image.shape[:2]
    cell_width = width // cell_count
    cell_height = height // cell_count

    # Рисуем линии сетки
    for i in range(1, cell_count):
        x = i * cell_width
        y = i * cell_height
        cv2.line(base_image, (x, 0), (x, height), grid_color, grid_thickness)
        cv2.line(base_image, (0, y), (width, y), grid_color, grid_thickness)


async def visualize_map_to_user(user):
    """Генерация карты и отправка пользователю."""
    start_time = time.time()
    resolution = 2048
    width, height = resolution, resolution  # Размер карты

    # Создаем фон
    base_image = create_background(width, height)

    # Определяем центр
    center = Vector2(resolution / 2, resolution / 2)

    # Добавляем корабль
    ship_image_path = images_operator.get_image_path_from_ship_name(f"ship {random.randint(1, 5)}")
    add_ship(base_image, ship_image_path, position=(center.x, center.y), scale=0.4, rotation=0)

    # Добавляем сетку
    add_grid(base_image, 11)

    # Кодируем изображение в память
    _, buffer = cv2.imencode('.png', base_image)
    image_bytes = buffer.tobytes()

    # Отправляем изображение пользователю
    asyncio.create_task(bot.send_photo(chat_id=user.id, photo=types.BufferedInputFile(image_bytes, filename="map.png")))
    print(f'Время генерации: {(time.time() - start_time) * 1000:.1f} мс')

from PIL import Image, ImageDraw, ImageFont
from core import images_operator
import random
from os import path

from core.vector2 import Vector2
from project_path import get_global_path


def create_background(width, height, color="#388dfc"):
    img = Image.new("RGBA", (width, height), color)
    return img


def add_ship(base_image, ship_image_path, position, scale=1.0, rotation=0):
    ship_img = Image.open(ship_image_path).convert("RGBA")

    # Масштабируем
    if scale != 1.0:
        new_size = (int(ship_img.width * scale), int(ship_img.height * scale))
        ship_img = ship_img.resize(new_size, Image.Resampling.LANCZOS)

    # Поворачиваем
    ship_img = ship_img.rotate(rotation, expand=True)
    print(f'w: {ship_img.width}, h: {ship_img.height}')

    # Изменяем позицию чтобы было относительно центра картинки, а не верхнего левого края
    position = (position[0] - (ship_img.width / 2), position[1] - (ship_img.height / 2))
    position = (int(position[0]), int(position[1]))

    # Вставляем на карту
    base_image.paste(ship_img, position, mask=ship_img)  # mask=ship_img сохраняет прозрачность


def add_island(base_image, points, color="#D2B48C"):
    draw = ImageDraw.Draw(base_image)
    draw.polygon(points, fill=color)


def add_grid(
    base_image,
    cell_count,
    grid_thickness=2,
    font_size=32,
    font_offset = 5,
    grid_color=(0, 0, 0, 50),
    text_color=(0, 0, 0, 100)
):
    width, height = base_image.size

    # Создаем временный слой с прозрачной сеткой
    grid_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(grid_layer)

    # Размер клетки
    cell_width = width / cell_count
    cell_height = height / cell_count

    # Рисуем вертикальные линии
    for i in range(1, cell_count + 1):
        x = int(i * cell_width)
        draw.line([(x, 0), (x, height)], fill=grid_color, width=grid_thickness)

    # Рисуем горизонтальные линии
    for i in range(1, cell_count + 1):
        y = int(i * cell_height)
        draw.line([(0, y), (width, y)], fill=grid_color, width=grid_thickness)

    # Накладываем слой сетки на основное изображение
    base_image.alpha_composite(grid_layer)

    # Добавляем подписи (буквы и цифры)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    text_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # Отдельный слой для текста
    text_draw = ImageDraw.Draw(text_layer)

    for i in range(cell_count):
        # Буквы сверху и снизу
        letter = chr(65 + i)  # 'A', 'B', ...
        x = int(i * cell_width + cell_width / 2 - font_size / 2)
        text_draw.text((x, font_offset), letter, fill=text_color, font=font)
        text_draw.text((x, height - font_size - font_offset), letter, fill=text_color, font=font)

        # Цифры слева и справа
        number = str(i + 1)
        y = int(i * cell_height + cell_height / 2 - font_size / 2)
        text_draw.text((font_offset, y), number, fill=text_color, font=font)
        text_draw.text((width - font_size - font_offset, y), number, fill=text_color, font=font)

    # Накладываем слой с текстом на основное изображение
    base_image.alpha_composite(text_layer)


def generate_map(map = None, resolution = 2048):
    width, height = resolution, resolution  # Размер карты
    base_image = create_background(width, height)

    center = Vector2(resolution / 2, resolution / 2)

    # Добавляем остров
    island_points = [(200, 300), (300, 200), (400, 260), (360, 400), (240, 360)]
    add_island(base_image, island_points)

    # Добавляем корабль
    ship_image_path = images_operator.get_image_path_from_ship_name(f"ship {random.randint(1, 5)}")  # Заменить на путь к твоему изображению
    add_ship(base_image, ship_image_path, position=(center.x, center.y), scale=0.4, rotation=0)

    # Добавляем сетку
    add_grid(base_image, 11)

    # Сохраняем изображение
    map_path = get_global_path(path.join("cache", "map.png"))
    base_image.save(map_path)
    print(f"Карта сохранена в {map_path}")


generate_map()

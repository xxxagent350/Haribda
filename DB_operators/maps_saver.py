import pickle
import copy
from models.map import Map
from models.world_objects.ship import Ship

# Функция для сохранения карт в файл
def save_maps_to_file(maps_, file_path):
    with open(file_path, "wb") as file:  # Используем бинарный режим
        pickle.dump(maps_, file)

# Функция для загрузки карт из файла
def load_maps_from_file(file_path):
    with open(file_path, "rb") as file:  # Используем бинарный режим
        return pickle.load(file)

# Пример использования
if __name__ == "__main__":
    maps = {0: Map()}
    ship = Ship(position=(0, 0), rotation=0, sprite_name="sprite")
    maps[0].add_changed_square(copy.deepcopy(ship))  # Пример добавления объекта

    # Сохранение в файл
    save_maps_to_file(maps, "maps.pkl")

    # Загрузка из файла
    loaded_maps = load_maps_from_file("maps.pkl")

    print(loaded_maps)

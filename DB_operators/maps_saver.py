import json
import copy
from models.map import Map
from models.world_objects.ship import Ship


# Пользовательский JSONEncoder для сериализации Map
class MapEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Map):
            # Преобразуем Map в словарь с сериализацией вложенных объектов
            return {
                "objects": [self.default(o) for o in obj.objects],
                "delayed_actions": [self.default(a) for a in obj.delayed_actions],
                "short_delayed_actions": [self.default(a) for a in obj.short_delayed_actions],
                "changed_squares": obj.changed_squares,
            }
        elif isinstance(obj, Ship):
            # Пример сериализации Ship, адаптируйте под свою структуру
            return obj.__dict__
        elif hasattr(obj, "__dict__"):
            # Сериализация произвольного объекта с атрибутами
            return obj.__dict__
        return super().default(obj)


# Декодер для создания объектов Map и вложенных данных
def map_decoder(dct):
    if "objects" in dct and "delayed_actions" in dct:
        # Создаем объект Map
        map_obj = Map()
        map_obj.objects = [decode_object(o) for o in dct["objects"]]
        map_obj.delayed_actions = [decode_object(a) for a in dct["delayed_actions"]]
        map_obj.short_delayed_actions = [decode_object(a) for a in dct["short_delayed_actions"]]
        map_obj.changed_squares = dct["changed_squares"]
        return map_obj
    return dct


# Общая функция для декодирования вложенных объектов
def decode_object(dct):
    if "some_property" in dct:  # Замените "some_property" на уникальное свойство объекта
        return Ship(**dct)  # Если это Ship, создаем экземпляр
    return dct


# Функция для сохранения карт в файл
def save_maps_to_file(maps_, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        #json.dump(maps_, file, cls=MapEncoder)
        pass


# Функция для загрузки карт из файла
def load_maps_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        loaded_maps = json.load(file, object_hook=map_decoder)
        return {int(k): v for k, v in loaded_maps.items()}  # Преобразуем ключи в int


# Пример использования
if __name__ == "__main__":
    maps = {0: Map()}
    maps[0].add_changed_square(copy.deepcopy(Ship()))  # Пример добавления объекта

    save_maps_to_file(maps, "maps.json")
    loaded_maps = load_maps_from_file("maps.json")

    print(loaded_maps)

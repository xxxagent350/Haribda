import json
from models.world_objects.map import Map

# Функция для сериализации карты в JSON
class MapEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Map):
            # Преобразуйте объект Map в словарь
            return obj.__dict__
        return super().default(obj)

# Функция для десериализации JSON в объект Map
def map_decoder(dct):
    if 'property_name' in dct:  # Замените "property_name" на имя свойства Map
        # Создайте объект Map и установите свойства
        map_obj = Map()
        map_obj.__dict__.update(dct)
        return map_obj
    return dct

# Функция для сохранения карт в файл
def save_maps_to_file(maps, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(maps, file, cls=MapEncoder)

# Функция для загрузки карт из файла
def load_maps_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        loaded_maps = json.load(file, object_hook=map_decoder)
        return {int(k): v for k, v in loaded_maps.items()}  # Преобразование ключей в int

if __name__ == "__main__":
    # Пример использования
    save_maps_to_file({}, 'maps.json')
    loaded_maps = load_maps_from_file('maps.json')

    print(loaded_maps)

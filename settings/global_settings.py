import os

from settings import not_synchronized
import project_path

token = not_synchronized.bot_token
data_path = project_path.get_global_path('data')

render_out_of_border_range = 0  # Дополнительная прорисовка за краями карты. Установите на 0, если хотите, чтобы игрок никак не мог увидеть, что находится за краями его поля зрения и на 1, если хотите оставить возможность увидеть выглядывающий объект из-за краёв карты


if not os.path.exists(data_path):
        os.makedirs(data_path)
        print(f'Создана папка {data_path}')

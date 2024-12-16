import sqlite3
import os
from shutil import copyfile
from a_library.custom_translator import List_in_Str, Str_in_List
from models.world_objects.ship import Ship
from variables.maps_dict import maps
from variables.users_dict import users_dict
from models.user import User
from settings import global_settings
from data_operators.db_column import DBColumn
from core.nick_generator import get_random_name

db_filename = 'users.db'
db_path = os.path.join(global_settings.data_path, db_filename)

# Структура базы данных
REQUIRED_COLUMNS = [
    DBColumn("id", "INTEGER", not_null=True),
    DBColumn("name", "TEXT", not_null=True),
    DBColumn("artefacts", "TEXT"),
    DBColumn("special_info", "TEXT"),
    DBColumn("controlled_ship_id", "TEXT"),
    DBColumn("current_map_id", "INTEGER", "0")
]

def init_db():
    try:
        # Создаём базу данных, если её нет
        if not os.path.exists(db_path):
            print("База данных не найдена. Создаётся новая база.")
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(build_create_table_query("users_data", REQUIRED_COLUMNS))
            print("Новая база данных создана.")
            return

        # Подключение к существующей базе
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            # Проверяем текущую архитектуру базы данных
            cursor.execute("PRAGMA table_info(users_data)")
            existing_columns = [
                DBColumn(name=row[1], type_=row[2], default=None, not_null=row[3] == 1)
                for row in cursor.fetchall()
            ]

            # Если структура базы данных не совпадает, адаптируем её
            if not columns_match(existing_columns, REQUIRED_COLUMNS):
                print("Архитектура базы данных отличается. Адаптируем...")
                backup_path = f"{db_path}.backup"
                copyfile(db_path, backup_path)
                print(f"Резервная копия базы данных создана: {backup_path}")
                adapt_database(cursor, existing_columns, REQUIRED_COLUMNS)

            # Создаём таблицу, если её нет
            cursor.execute(build_create_table_query("users_data", REQUIRED_COLUMNS))
            print("База данных успешно инициализирована")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")

def columns_match(existing, required):
    if len(existing) != len(required):
        return False
    return all(
        existing_col.name == required_col.name and
        existing_col.type_ == required_col.type_ and
        (existing_col.not_null == required_col.not_null)
        for existing_col, required_col in zip(existing, required)
    )

def adapt_database(cursor, existing_columns, required_columns):
    temp_table = "users_data_temp"
    try:
        # Создаем временную таблицу с новой структурой
        cursor.execute(build_create_table_query(temp_table, required_columns))

        # Перенос данных из старой таблицы во временную
        existing_names = [col.name for col in existing_columns]
        required_names = [col.name for col in required_columns]

        intersecting_columns = [name for name in existing_names if name in required_names]
        select_columns = ", ".join(intersecting_columns)
        insert_columns = ", ".join(intersecting_columns)

        cursor.execute(f"INSERT INTO {temp_table} ({insert_columns}) SELECT {select_columns} FROM users_data")

        # Удаляем старую таблицу и переименовываем временную
        cursor.execute("DROP TABLE users_data")
        cursor.execute(f"ALTER TABLE {temp_table} RENAME TO users_data")
        print("База данных успешно адаптирована.")
    except Exception as e:
        print(f"Ошибка при адаптации базы данных: {e}")

def build_create_table_query(table_name, columns):
    column_definitions = []
    for col in columns:
        definition = f"{col.name} {col.type_}"
        if col.not_null:
            definition += " NOT NULL"
        if col.default is not None:
            definition += f" DEFAULT {col.default}"
        column_definitions.append(definition)
    column_definitions_str = ", ".join(column_definitions)
    return f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions_str})"

def add_user(user_id, name=None, artefact=None, special_info=None, current_map_id=0):
    """
    :param user_id: ID пользователя
    :param name: Имя пользователя. При None генерируется автоматически
    :param artefact: Артефакты
    :param special_info: Дополнительная информация
    :param current_map_id: Номер карты, на которой сейчас находится корабль игрока
    :return:
    """
    if name is None:
        name = get_random_name()
    artefact = artefact or []
    special_info = special_info or []
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO users_data (id, name, artefacts, special_info, current_map_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (user_id, name, List_in_Str(artefact), List_in_Str(special_info), current_map_id)
            )
            print(f"Пользователь '{name}' успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")

def try_get_user(user_id):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            loaded_user_data = cursor.execute("SELECT * FROM users_data WHERE id = ?", (user_id,)).fetchone()
            if loaded_user_data:
                loaded_user = User(loaded_user_data[0])
                loaded_user.name = loaded_user_data[1]
                loaded_user.artefacts = Str_in_List(loaded_user_data[2])
                loaded_user.special_info = loaded_user_data[3]

                # Поиск корабля игрока на картах
                controlled_ship_id = loaded_user_data[4]
                searching_complete = False
                for map_ in maps.values():
                    for object_ in map_.objects:
                        if type(object_) == Ship and object_.index == controlled_ship_id:
                            loaded_user.controlled_ship = object_
                            searching_complete = True
                            break
                    if searching_complete:
                        break

                if loaded_user_data[5] in maps:
                    loaded_user.current_map = maps[loaded_user_data[5]]
                return loaded_user
            else:
                return None
    except Exception as e:
        print(f"Ошибка при получении пользователя: {e}")
        return None

def save_user(user_id, name=None, artefact=None, special_info=None, current_map=None, controlled_ship=None):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            existing_user = cursor.execute("SELECT * FROM users_data WHERE id = ?", (user_id,)).fetchone()
            if not existing_user:
                print(f"Пользователь с ID {user_id} не найден!")
                return False
            # Обновляем только переданные поля
            if name is not None:
                cursor.execute("UPDATE users_data SET name = ? WHERE id = ?", (name, user_id))
            if artefact is not None:
                cursor.execute("UPDATE users_data SET artefact = ? WHERE id = ?", (List_in_Str(artefact), user_id))
            if special_info is not None:
                cursor.execute("UPDATE users_data SET special_info = ? WHERE id = ?", (List_in_Str(special_info), user_id))
            if current_map is not None:
                cursor.execute("UPDATE users_data SET current_map_id = ? WHERE id = ?", (current_map, user_id))
            if controlled_ship is not None:
                cursor.execute("UPDATE users_data SET controlled_ship_id = ? WHERE id = ?", (controlled_ship, user_id))
            print(f"Пользователь с ID {user_id} успешно обновлен!")
            return True
    except Exception as e:
        print(f"Ошибка при обновлении пользователя: {e}")
        return False

def get_all_user_ids():
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            user_ids = cursor.execute("SELECT id FROM users_data").fetchall()
            return [user_id[0] for user_id in user_ids]
    except Exception as e:
        print(f"Ошибка при получении списка ID пользователей: {e}")
        return []

def get_all_users_dict():
    all_users_dict = dict()
    for user_id in get_all_user_ids():
        loaded_user = try_get_user(user_id)
        if loaded_user is not None:
            all_users_dict[user_id] = loaded_user
    return all_users_dict

def load_all_users():
    all_users_dict = get_all_users_dict()
    users_dict.update(all_users_dict)

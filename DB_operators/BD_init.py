import sqlite3
import os
from a_library.custom_translator import List_in_Str, Str_in_List

# Имя файла базы данных
DB_FILE = os.path.join(os.path.dirname(__file__), "local_database.db")

def init_db():
    try:
        # Подключаемся к локальной базе данных (файл создается автоматически, если его нет)
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Создаем таблицу
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS example_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    artefact TEXT,
                    special_info TEXT,
                    current_map INTEGER 
                )
            """)
            print("Таблица успешно создана!")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")

def add_user(user_id, name, artefact=None, special_info=None, current_map = None):
    if artefact is None:
        artefact = []
    if special_info is None:
        special_info = []
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Добавляем пользователя
            cursor.execute("""
                INSERT INTO example_table (id,name, artefact, special_info,current_map)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, name, List_in_Str(artefact), List_in_Str(special_info),current_map,))
            print(f"Пользователь '{name}' успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")

def get_user(user_id):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()

            # Получаем всех пользователя
            user = cursor.execute("SELECT * FROM example_table WHERE id = ?", (user_id,)).fetchone()

            user = [x for x in user]
            if user != None:
                print("f : ",user)
                user[2] = Str_in_List(user[2])
                user[3] = Str_in_List(user[3])
                return user, True
            else:
                return None, False
    except Exception as e:
        print(f"Ошибка при получении пользователей: {e}")
        return None ,False

def save_user(user_id, name=None, artefact=None, special_info=None, current_map = 0):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()

            # Проверяем, существует ли пользователь
            existing_user = cursor.execute("SELECT * FROM example_table WHERE id = ?", (user_id,)).fetchone()
            if not existing_user:
                print(f"Пользователь с ID {user_id} не найден!")
                return False

            # Обновляем только переданные поля
            if name is not None:
                cursor.execute("UPDATE example_table SET name = ? WHERE id = ?", (name, user_id))
            if artefact is not None:
                cursor.execute("UPDATE example_table SET artefact = ? WHERE id = ?", (List_in_Str(artefact), user_id))
            if special_info is not None:
                cursor.execute("UPDATE example_table SET special_info = ? WHERE id = ?", (List_in_Str(special_info), user_id))
            cursor.execute("UPDATE example_table SET current_map = ? WHERE id = ?",
                           (map, user_id))
            print(f"Пользователь с ID {user_id} успешно обновлен!")
            return True

    except Exception as e:
        print(f"Ошибка при обновлении пользователя: {e}")
        return False

def get_all_user_ids():
    """
    Возвращает список всех ID зарегистрированных пользователей.
    """
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Получаем все ID из таблицы example_table
            user_ids = cursor.execute("SELECT id FROM example_table").fetchall()
            # Преобразуем список кортежей в список чисел
            return [user_id[0] for user_id in user_ids]
    except Exception as e:
        print(f"Ошибка при получении списка ID пользователей: {e}")
        return []

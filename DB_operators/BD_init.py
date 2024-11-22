import sqlite3
import os

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
                    special_info TEXT
                )
            """)
            print("Таблица успешно создана!")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")

def add_user(name, artefact=None, special_info=None):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Добавляем пользователя
            cursor.execute("""
                INSERT INTO example_table (name, artefact, special_info)
                VALUES (?, ?, ?)
            """, (name, artefact, special_info))
            print(f"Пользователь '{name}' успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")

def get_all_users():
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Получаем всех пользователей
            cursor.execute("SELECT * FROM example_table")
            users = cursor.fetchall()
            return users
    except Exception as e:
        print(f"Ошибка при получении пользователей: {e}")
        return []

# Пример использования
if __name__ == "__main__":
    # Инициализация базы данных
    init_db()

    # Добавление пользователей
    add_user("Alice", "Sword", "Leader of the group")
    add_user("Bob", "Shield", "Protector")

    # Вывод всех пользователей
    users = get_all_users()
    for user in users:
        print(user)

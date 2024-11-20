import psycopg2
from psycopg2 import sql

def init_bd():
    # Параметры подключения к PostgreSQL
    db_params = {
        'dbname': 'postgres',  # Подключаемся к системной базе "postgres"
        'user': 'root',  # Ваше имя пользователя
        'password': '0ze4Sb9hp2QX3HWv',  # Ваш пароль
        'host': 'localhost',  # Адрес сервера (например, localhost)
        'port': 5432  # Порт PostgreSQL (по умолчанию 5432)
    }

    # Имя новой базы данных
    new_db_name = "DB"

    try:
        # Подключение к PostgreSQL
        with psycopg2.connect(**db_params) as conn:
            conn.autocommit = True  # Нужно для операций, которые нельзя делать в транзакции
            with conn.cursor() as cursor:
                # Создаем новую базу данных
                create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name))
                cursor.execute(create_db_query)
                print(f"База данных '{new_db_name}' успешно создана!")
    except Exception as e:
        print(f"Ошибка: {e}")

def init_users_table():
    new_db_params = {
        'dbname': "DB",
        'user': 'root',
        'password': '0ze4Sb9hp2QX3HWv',
        'host': 'localhost',
        'port': 5432
    }

    try:
        with psycopg2.connect(**new_db_params) as conn:
            with conn.cursor() as cursor:
                # Пример создания таблицы
                cursor.execute("""
                    CREATE TABLE example_table (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        inventar TEXT,
                    )
                """)
                print("Таблица успешно создана!")
    except Exception as e:
        print(f"Ошибка: {e}")

class User:
    def __init__(self,idd):
        pass

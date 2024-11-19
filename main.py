import asyncio
import sqlite3
import time
import traceback


from aiogram import Dispatcher, types, Router
from aiogram.filters import Command

from core.time_converter import get_full_current_date

from variables.bot import dp,bot




async def main():
    print("Deploying Leviathan")
    print("Leviathan launched successfully")

    i= int('g')


    await asyncio.create_task(dp.start_polling(bot, skip_updates=True))


# Функция для записи ошибок в файл
def log_error_to_file(message):
    with open("error_log.txt", "a") as file:
        file.write(message + "\n\n\n\n\n")


# Запуск процесса поллинга новых апдейтов

if __name__ == "__main__":
    while True:
        try:
            asyncio.run(main())
        except Exception as error:
            print(f'$ Error {get_full_current_date()} : ', error)
            log_error_to_file(f'Error {get_full_current_date()} : '+ str(error) +"\n\n"+traceback.format_exc())
            time.sleep(5)

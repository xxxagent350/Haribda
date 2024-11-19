import asyncio
import sqlite3
import time

from aiogram import Dispatcher, types, Router
from aiogram.filters import Command

from variables.bot import dp,bot




async def main():
    print("Deploying Leviathan")
    print("Leviathan launched successfully")

    await asyncio.create_task(dp.start_polling(bot, skip_updates=True))


# Функция для записи ошибок в файл
def log_error_to_file(message):
    with open("error_log.txt", "a") as file:
        file.write(message + "\n\n\n")


# Запуск процесса поллинга новых апдейтов

if __name__ == "__main__":
    while True:
        try:
            asyncio.run(main())
        except Exception as error:
            print('Error : ', error)
            log_error_to_file('Error : ', error)
            #time.sleep(5)

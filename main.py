#импорт сторонних библиатек
import asyncio
import time
import traceback

#Инициализируем события
from variables import event_manager

#Запускаем реакторы
from network import call_reaction,text_reaction

#импорт кастомных функций
from core.time_converter import get_full_current_date

#импорт необходимых пременных
from variables.bot import dp,bot



async def main():
    print("Deploying Leviathan")
    print("Leviathan launched successfully")
    await dp.start_polling(bot, skip_updates=True)



# Функция для записи ошибок в файл
def log_error_to_file(message):
    with open("error_log.txt", "a") as file:
        file.write(message + "\n\n\n\n\n")


# Запуск процесса поллинга новых апдейтов

if __name__ == "__main__":
    log_error_to_file(f"\n\n\n\n\n{'-'*30}\n{' '*13}Start\n{'-'*30}")
    while True:
        try:
            asyncio.run(main())
        except Exception as error:
            print(f'$ Error {get_full_current_date()} : ', error)
            log_error_to_file(f'Error {get_full_current_date()} : '+ str(error) +"\n\n"+traceback.format_exc())
            time.sleep(5)

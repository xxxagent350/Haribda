
# Импорт библиотек
import asyncio
import time
import traceback
from core.async_event import AsyncEvent

# Инициализируем события
from variables import event_manager

# Запускаем реакторы
from network import call_reaction, text_reaction

# Импорт кастомных функций
from core.time_converter import get_full_current_date

# Импорт необходимых переменных
from variables.bot import dp,bot


start_event = AsyncEvent()

# Используйте @register_on_start для подписки на событие
def subscribe_on_start(func):
    start_event.subscribe(func)
    return func

async def main():
    print("Deploying Leviathan")
    print("Leviathan launched successfully")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

# Функция для записи ошибок в файл
def log_error_to_file(message):
    with open("error_log.txt", "a") as file:
        file.write(message + "\n\n\n\n\n")


# Запуск main в цикле while true
if __name__ == "__main__":
    log_error_to_file(f"\n\n\n\n\n{'-'*30}\n{' '*13}Start\n{'-'*30}")
    while True:
        try:
            asyncio.run(main())
        except Exception as error:
            print(f'$ Fatal Error {get_full_current_date()} : ', error)
            log_error_to_file(f'Fatal Error {get_full_current_date()} : '+ str(error) +"\n\n"+traceback.format_exc())
            time.sleep(5)

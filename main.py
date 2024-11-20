
# Импорт библиотек
import asyncio
import signal
import time
import traceback

# Инициализируем события
from variables import event_manager

# Запускаем реакторы
from network import call_reaction, text_reaction

# Импорт кастомных функций
from core.time_converter import get_full_current_date
from a_library.log_error import log_error_to_file

# Импорт необходимых переменных
from variables.bot import dp,bot

async def main():
    print("Deploying Leviathan")
    print("Leviathan launched successfully")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


def on_shutdown(dp):
    print("Программа завершается... Ожидаю завершения всех задач.")
    bot.close()


def setup_shutdown():
    signal.signal(signal.SIGINT, lambda sig, frame: on_shutdown(dp))  # Для Ctrl+C
    signal.signal(signal.SIGTERM, lambda sig, frame: on_shutdown(dp))  # Для сигнала завершения процесса



# Запуск main в цикле while true
if __name__ == "__main__":
    setup_shutdown()
    log_error_to_file(f"\n\n\n\n\n{'-'*30}\n{' '*13}Start {get_full_current_date()}\n{'-'*30}")
    while True:
        try:
            asyncio.run(main())
        except Exception as error:
            print(f'$ Fatal Error {get_full_current_date()} : ', error)
            log_error_to_file(f'Fatal Error {get_full_current_date()} : '+ str(error) +"\n\n"+traceback.format_exc())

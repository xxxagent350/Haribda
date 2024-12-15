
import asyncio
import signal
import traceback
from data_operators import maps_operator
from data_operators import db_operator

# Инициализируем события
from variables import event_manager

# Запускаем реакторы
from network import call_reaction, text_reaction

from settings import global_settings

# Импорт функций
from core.time_converter import get_full_current_date
from a_library.log_error import log_error_to_file

# Импорт переменных
from variables.bot import dp,bot
from mechanics.game_core import process_game


async def main():
    # Загружаем данные карт
    maps_operator.load_maps()

    # Инициализируем базу данных и загружаем данные пользователей
    db_operator.init_db()
    db_operator.try_get_user(-1)

    asyncio.create_task(process_game())
    await bot.delete_webhook(drop_pending_updates=True)
    print("Запуск завершён, к бою готов!")
    await dp.start_polling(bot, skip_updates=True)


async def on_shutdown(dp):
    maps_operator.save_maps()
    print("Программа завершается... Ожидаю завершения всех задач.")
    await bot.close()


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


# Импорт библиотек
import asyncio
import signal
import time
import traceback
from DB_operators.maps_saver import save_maps_to_file
from core.map_list import maps

# Инициализируем события
from variables import event_manager

# Запускаем реакторы
from network import call_reaction, text_reaction

# Импорт кастомных функций
from core.time_converter import get_full_current_date
from a_library.log_error import log_error_to_file
from DB_operators.BD_init import init_db

# Импорт необходимых переменных
from variables.bot import dp,bot
from mechanics.game_core import process_game

from core import map_list_operator


async def main():
    asyncio.create_task(process_game())
    await bot.delete_webhook(drop_pending_updates=True)
    print("Leviathan launched successfully")
    await dp.start_polling(bot, skip_updates=True)


async def on_shutdown(dp):
    save_maps_to_file(maps, "maps.json")
    print("Программа завершается... Ожидаю завершения всех задач.")
    await bot.close()


def setup_shutdown():
    signal.signal(signal.SIGINT, lambda sig, frame: on_shutdown(dp))  # Для Ctrl+C
    signal.signal(signal.SIGTERM, lambda sig, frame: on_shutdown(dp))  # Для сигнала завершения процесса


init_db()


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

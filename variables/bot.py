from aiogram import Dispatcher, Bot
from settings.global_settings import token

#инициализируем бота и диспетчер
bot = Bot(token=token, timeout=3)
dp = Dispatcher()
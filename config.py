# config.py
from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
Admins = [738723836, ]

token = config("TOKEN")

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot,storage=storage)
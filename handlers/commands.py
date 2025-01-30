# commands.py
from aiogram import types, Dispatcher
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Добро пожаловать в наш магазин!\n'
                                f' Я помогу тебе с товарами и заказами.')



async def info_handler(message: types.Message):
    info_text = (
        "Привет! Я бот для магазина.\n"
        "Я могу помочь вам добавить товары\n\n"
        "Мои возможности:\n"
        "- Добавление товаров (доступно только сотрудникам)\n"
        "- Оформление заказов\n"
        "- Просмотр всех товаров\n"
        "Если у тебя есть вопросы, просто напиши мне!"
    )
    await message.answer(info_text)

def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])

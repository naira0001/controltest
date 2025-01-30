# buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton('/start'),
        KeyboardButton('/info'),
        KeyboardButton('/store'))

submit = (ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add
          (KeyboardButton('да'), KeyboardButton('нет')))

remove_keyboard = ReplyKeyboardRemove()



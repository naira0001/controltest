# fsm_store.py
from aiogram import types, Dispatcher
from config import Admins
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import main_db


class FsmStore(StatesGroup):
    name = State()
    category = State()
    size = State()
    price = State()
    product_id = State()
    photo = State()
    submit = State()

# Функция для проверки сотрудника
async def is_admin(message: types.Message):
    return message.from_user.id in Admins


async def start_fsm_store(message: types.Message):
    if not await is_admin(message):
        return await message.answer("У вас нет прав для добавления товаров.")

    await FsmStore.name.set()
    await message.answer('Напишите название товара:')

async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer('Напишите категорию:')
    await FsmStore.next()

async def process_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer('Напишите размер:')
    await FsmStore.next()

async def process_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await message.answer('Напишите стоимость:')
    await FsmStore.next()

async def process_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await message.answer('Напишите артикул ')
    await FsmStore.next()

async def process_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = int(message.text)
    await message.answer('Добавьте фото ')
    await FsmStore.next()

async def process_photo (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FsmStore.next()
    await message.answer('Верные ли данные ?')
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название товара - {data["name"]}\n'
                                       f'Размер товара - {data["size"]}\n'
                                       f'Категория - {data["category"]}\n'
                                       f'Цена - {data["price"]}'
                                       f'Артикул - {data["product_id"]}\n',reply_markup=buttons.submit)

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        # Запись в базу
        async with state.proxy() as data:
            await main_db.sql_insert_store(name=data['name'],
                                           size=data['size'],
                                           category=data['category'],
                                           price=data['price'],
                                           photo=data['photo'],
                                           product_id=data['product_id']
                                           )
            await message.answer('Ваши данные в базе', reply_markup=buttons.remove_keyboard)
        await state.finish()
    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()
    else:
        await message.answer('Выберите да или нет')
async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard)

def register_handlers_fsm_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')

    dp.register_message_handler(start_fsm_store, commands='store')
    dp.register_message_handler(process_name, state=FsmStore.name)
    dp.register_message_handler(process_size, state=FsmStore.size)
    dp.register_message_handler(process_category, state=FsmStore.category)
    dp.register_message_handler(process_price, state=FsmStore.price)
    dp.register_message_handler(process_photo, state=FsmStore.photo, content_types=['photo'])
    dp.register_message_handler(process_product_id, state=FsmStore.product_id)
    dp.register_message_handler(submit, state=FsmStore.submit)



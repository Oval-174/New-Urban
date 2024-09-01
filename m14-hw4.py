# m14-hw4.py "Продуктовая база"
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import crud_functions

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
kb.add(button1, button2, button3)

in_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button2 = KeyboardButton(text='Формулы расчёта', callback_data='formulas')
in_kb = InlineKeyboardMarkup(resize_keyboard=True)
in_kb.add(in_button1)
in_kb.add(in_button2)

in_button_p1 = InlineKeyboardButton(text='Product1', callback_data="product_buying")
in_button_p2 = InlineKeyboardButton(text='Product2', callback_data="product_buying")
in_button_p3 = InlineKeyboardButton(text='Product3', callback_data="product_buying")
in_button_p4 = InlineKeyboardButton(text='Product4', callback_data="product_buying")

product_buy_in_kb = InlineKeyboardMarkup(row_width=4, resize_keyboard=True)
product_buy_in_kb.add(in_button_p1, in_button_p2, in_button_p3, in_button_p4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(4):
        await message.answer(f'Название: {products[i][0]} | Описание: {products[i][1]} | Цена: {products[i][2]}')
        with open(f'product{i+1}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer(f'Выберите продукт для покупки:', reply_markup = product_buy_in_kb)

@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer(f'Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer(f'Выберите опцию:', reply_markup = in_kb)

@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer(f'10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer(f'Введите свой возраст (полных лет):')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост в см:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес в кг:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
# 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    norma = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {norma} ккал')
    await state.finish()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет! Я бот Calories, помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler()
async def all_massages(message):
    await message.answer(f'Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    products = crud_functions.get_all_products()
    executor.start_polling(dp, skip_updates=True)

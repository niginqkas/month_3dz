from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer(f'Здравствуйте! {message.from_user.first_name}')
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text = 'Наш инстаграм профиль',
                    url = 'https://instagram.com/geeks_studio'
                )
            ],
            [
                types.InlineKeyboardButton(
                text='Наш сайт',
                url='https://instagram.com/geeks_junior'

               )
            ]
        ]
    )
    await message.answer(msg, reply_markup = kb)
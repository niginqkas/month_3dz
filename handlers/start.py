from aiogram import Router, types
from aiogram.filters import Command

kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Наш инстаграм",
                url="https://instagram.com/geeks"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Оставьте отзыв",
                callback_data="review"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Наш сайт",
                url="https://geeks.kg"
            )
        ]
    ]
)


start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Привет {name}',reply_markup=kb)





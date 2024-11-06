from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f'Привет {name}'
    await message.answer(msg)
    # await bot.send_message(
    #     chat_id = message.from_user.id,
    #     text = msg,
    )


kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наш инстаргам",
                    url="https://instagram.com/geeks"
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

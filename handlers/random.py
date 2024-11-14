from aiogram import Router, types
from aiogram.filters import Command

start_random = Router()

@start_random.message(Command("myinfo"))
async def myinfo(message: types.Message):
    user = message.from_user
    first_name = user.first_name
    last_name = user.last_name
    user_id = user.id
    await message.answer(f"Name: {first_name} Last_name {last_name} Id "
                         f"[{user_id}]")

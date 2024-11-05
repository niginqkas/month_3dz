import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
from aiogram.filters import Command
from random import choice

names = ('bektur', 'alihan', 'aziret', 'gulina')
token = dotenv_values('.env')['TOKEN']
bot = Bot(token = token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}')

@dp.message(Command('myinfo'))
async def my_info(message: types.Message):
    await message.answer (f'Ваши данные:\n'
                         f'id: {message.from_user.id})\n'
                         f'first_name: {message.from_user.first_name}\n'
                         f'user_name: {message.from_user.user_name}\n'
                         )

@dp.message(Command('random'))
async def random(message: types.Message):
    await message.answer(f'{choice(names)}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
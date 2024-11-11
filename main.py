import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
from aiogram.filters import Command

import logging
from handlers.start import start_router

token = dotenv_values('.env')['TOKEN']
bot = Bot(token = token)
dp = Dispatcher()







async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

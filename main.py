import asyncio
from aiogram.filters import Command

from bot_bonfig import bot, dp
from handlers.random import start_random
import logging
from handlers.start import start_kb
from handlers.review_dialog import opros_router



async def main():
    dp.include_router(start_kb)
    dp.include_router(start_random)
    dp.include_router(opros_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

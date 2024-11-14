import asyncio
from aiogram.filters import Command

from bot_bonfig import bot, dp
from handlers.random import start_random
import logging
from handlers.start import start_router


async def main():
    dp.include_router(start_router)
    dp.include_router(start_random)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

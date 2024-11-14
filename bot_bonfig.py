import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values

token = dotenv_values('.env')['TOKEN']
bot = Bot(token = token)
dp = Dispatcher()
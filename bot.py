from aiogram import Bot, Dispatcher
from config import Config

config = Config()

bot = Bot(token=config.bot_token)
dp = Dispatcher()
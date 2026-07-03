import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import settings


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    logging.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import logging

from bot import bot, dp
from handlers.start import router as start_router
from handlers.random_character import router as random_router

logging.basicConfig(level=logging.INFO)


async def main():
    dp.include_router(start_router)
    dp.include_router(random_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
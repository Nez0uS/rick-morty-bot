import asyncio
import logging

from bot import dp, bot
from handlers.start import router as start_router

logging.basicConfig(level=logging.INFO)


async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
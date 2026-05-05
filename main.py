import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from config import bot_token
from handlers.functions import router as commands_router



async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    bot = Bot(token=bot_token)
    dp = Dispatcher()

    dp.include_router(commands_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

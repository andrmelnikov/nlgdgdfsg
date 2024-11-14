import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router




async def main():
    bot = Bot(token = '7708956889:AAHJhcC6Se9x-sw8uivEwA46l2ecpGAWxYk')
    dp = Dispatcher()
    await dp.start_polling(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

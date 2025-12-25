from aiogram import Dispatcher
from asyncio import run

from config import BOT
from app.handlers import rt


DP = Dispatcher()



async def main() -> None:
    DP.include_router(rt)
    print("(V) Бот запущен.")
    await DP.start_polling(BOT)


if __name__ == "__main__":
    try:
        run(main())
    except Exception as e:
        print("(X) " + e + ".")
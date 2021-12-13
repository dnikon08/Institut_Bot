import logging
import asyncio
from aiogram.utils.exceptions import BotBlocked
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher
from os import getenv
from sys import exit
import Responses as R
import time

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

print("PROGRAM START")
# пример обработчика ошибки
@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)  # Здоровый сон на 10 секунд
    await message.reply("Вы заблокированы")

@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True


@dp.message_handler(commands="start") # новый обработчик
async def cmd_test1(message: types.Message):  # await топерь обязателен
    await message.reply("start is working")


@dp.message_handler(commands="help")
async def cmd_test1(message: types.Message):
    await message.reply("help is working")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)




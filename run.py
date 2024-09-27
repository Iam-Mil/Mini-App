import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())  # Добавляем хранилище состояний
router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Открыть приложение', web_app=WebAppInfo(url='https://google.com'))]], resize_keyboard=True)
    await bot.send_message(text="Привет", reply_markup=markup, chat_id=message.chat.id)

async def main():
    logger = logging.getLogger('aiogram')
    logger.setLevel(logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)
    #привет ghgh


if __name__ == '__main__':
    asyncio.run(main())
import os
from aiogram import Dispatcher, Bot, types
import logging
from aiogram.utils.executor import start_polling
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(msg: types.Message, state: FSMContext):
    await msg.answer(f'Hello {msg.from_user.first_name}. Send message')
    await state.set_state('start')


@dp.message_handler(state='start')
async def any_message(msg: types.Message):
    unli = 'aeuioAEUIO'
    count = 0
    for i in msg.text:
        if i in unli:
            count += 1
    if count >= 5:
        await msg.delete()
        await msg.answer("Message deleted")
    else:
        await msg.answer('👋🏻')


if __name__ == '__main__':
    start_polling(dp, skip_updates=True)

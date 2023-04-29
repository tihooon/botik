from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from config import Token
from txtToMsg import *

bot = Bot(Token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать в бота!")
    await bot.send_message(chat_id=message.from_user.id, text="Выберите желаемый товар или категорию:",
                           reply_markup=ikmStart)


@dp.callback_query_handler()
async def callback(callback: types.callback_query):
    if callback.data == 'scheme2023':
        await callback.message.edit_text('Выберите схему заработка или курс из списка ниже 👇',
                                         reply_markup=ikm2023)
    elif callback.data == 'arbuz1':
        await callback.message.edit_text(Abuz1, reply_markup=ikmarbuz)
    elif callback.data == 'opl':
        await callback.message.edit_text("деняк суда: и тут короче кошелёк, я ебу?", reply_markup=ikmbc)
    elif callback.data == 'promo':
        await callback.message.edit_text("никаких промо, иди нахуй", reply_markup=ikmbc)
    elif callback.data == 'start':
        await callback.message.edit_text("Выберите желаемый товар или категорию:", reply_markup=ikmStart)
    else:
        await  callback.answer("Неготоволеньбыло")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

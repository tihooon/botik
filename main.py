from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from config import Token
from Texts.txtToMsg import *

bot = Bot(Token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать в бота!")
    await bot.send_message(chat_id=message.from_user.id, text="Выберите желаемый товар или категорию:",
                           reply_markup=ikmStart)


@dp.callback_query_handler()
async def callback(data: types.callback_query):
    if data.data == 'scheme2023':
        await data.message.edit_text('Выберите схему заработка или курс из списка ниже 👇',
                                     reply_markup=ikm2023)
    elif data.data == 'arbuz1':
        await data.message.edit_text(Abuz1, reply_markup=ikmarbuz)
    elif data.data == 'opl':
        await data.message.edit_text("Переводы сюда: ТУТ НОМЕР КАРТЫ ", reply_markup=ikmbc)
    elif data.data == 'promo':
        await data.message.edit_text("Отправьте боту ваш промокод для скидки.", reply_markup=ikmbc)
    elif data.data == 'start':
        await data.message.edit_text("Выберите желаемый товар или категорию:", reply_markup=ikmStart)
    else:
        await data.answer("Неготоволеньбыло")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

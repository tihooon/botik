from aiogram import Bot, Dispatcher, executor, types
from keyboards import ikmStart, ikm2023, ikmarbuz, ikmbc

Token = "5720687382:AAEBzoXQzLnL4QYFad70te3sZHIM7h28D-o"

bot = Bot(Token)
dp = Dispatcher(bot)

text = """АБУЗ ПАРТНЕРКИ 30К/КРУГ
Цена: 500 руб
Новая складчина! АБУЗ ПАРТНЕРКИ 30К/КРУГ!

Продавец согласен на гаранта до профита.  Этот абуз партнёрки свежий и очень интресный.

💰 Заработок: До 30к. рублей за круг.
⚪️ Цвет: Белый.  
💸 Вложения: Без вложений.
⏳ Срок жизни: Будет жить долго.
⛰ Гео: Нет ограничений. 
🤼‍♀️ Конкуренция: Нет.

Описание от автора:  
🌼 АБУЗ ПАРТНЕРКИ 30К/КРУГ

Искал топовую тему, а вокруг только инфоцыгане ? Ты нашел!

➖ Продам ЛИЧНУЮ полностью белую схему абуза "щели" партнерской программы, откуда мы будем вытаскивать до 30К за круг!

➖ В комплекте к схеме я обучу тебя фин. арбитражу и расскажу тебе как получить доступ в одну приватную партнерку (где профиты гораздо выше!)

💰 Доход: 30К/круг (1-2 дня) 💰
🔸 Цвет: белый
🔸 Полупассив
🔸 Нет конкуренции
🔸 Без вложений ❗️
🔸 Без общения с людьми
🔸 Освоит любой
🔸 Работа с пк/телефона
🔸 Поддержка 24/7
🔸 ГЕО нет значения

Причина продажи: я сам буду работать по этой схеме, и мне нужно отобрать адекватных ребят, которые купят схему и заработают свои легкие деньги. С ними я создам команду и буду работать по другим проектам.
Освоение этой схемы будет как бы испытанием)

⚠️ Готов работать через гаранта! ⚠️

Продажник: https://t.me/prodajnikk/30?single

💰Цена у автора: 5 000₽
🔥Цена места у нас: 500₽

Занять место в складчине можно только в автоматическом режиме, по кнопке "Занять место"!"""

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
        await callback.message.edit_text(text, reply_markup=ikmarbuz)
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

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikmStart = InlineKeyboardMarkup(row_width=1)
startButtons = [InlineKeyboardButton(text='Схемы заработка 2023', callback_data='scheme2023'),
                InlineKeyboardButton(text='Курсы по крипте', callback_data='courses'),
                InlineKeyboardButton(text='Схемы заработка 2022', callback_data='scheme2022'),
                InlineKeyboardButton(text='ебал я это писать', callback_data='fuck')]


ikm2023 = InlineKeyboardMarkup(row_width=1)
buttons1 = [InlineKeyboardButton(text='арбуз партнурки', callback_data='arbuz1'),
            InlineKeyboardButton(text='ебеёший скам вайлдберриса', callback_data='arbuz2'),
            InlineKeyboardButton(text='ещё какая-то хуетень', callback_data='arbuz3'),
            InlineKeyboardButton(text='ебал я это писать x2', callback_data='arbuz4'),
            InlineKeyboardButton(text='назад', callback_data='start')]

ikmarbuz = InlineKeyboardMarkup(row_width=1)
arbuz1Buttons = [InlineKeyboardButton(text='оплата', callback_data='opl'),
                 InlineKeyboardButton(text='промокодик)', callback_data='promo'),
                 InlineKeyboardButton(text='назад', callback_data='scheme2023')]

ikmbc = InlineKeyboardMarkup(row_width=1)
bc = InlineKeyboardButton(text='назад', callback_data='arbuz1')

ikmbc.add(bc)

for btn in startButtons:
    ikmStart.add(btn)

for btn in buttons1:
    ikm2023.add(btn)


for btn in arbuz1Buttons:
    ikmarbuz.add(btn)


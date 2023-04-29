from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikmStart = InlineKeyboardMarkup(row_width=1)
btnStart1 = InlineKeyboardButton(text='Схемы заработка 2023', callback_data='scheme2023')
btnStart2 = InlineKeyboardButton(text='Курсы по крипте', callback_data='courses')
btnStart3 = InlineKeyboardButton(text='Схемы заработка 2022', callback_data='scheme2022')
btnStart4 = InlineKeyboardButton(text='ебал я это писать', callback_data='fuck')

ikmStart.add(btnStart1, btnStart2, btnStart3, btnStart4)

ikm2023 = InlineKeyboardMarkup(row_width=1)
btn20231 = InlineKeyboardButton(text='арбуз партнурки', callback_data='arbuz1')
btn20232 = InlineKeyboardButton(text='ебеёший скам вайлдберриса', callback_data='arbuz2')
btn20233 = InlineKeyboardButton(text='ещё какая-то хуетень', callback_data='arbuz3')
btn20234 = InlineKeyboardButton(text='ебал я это писать x2', callback_data='arbuz4')
btn20234 = InlineKeyboardButton(text='назад', callback_data='start')

ikm2023.add(btn20231, btn20232, btn20233, btn20234)

ikmarbuz = InlineKeyboardMarkup(row_width=1)
btnarbuz1 = InlineKeyboardButton(text='оплата', callback_data='opl')
btnarbuz2 = InlineKeyboardButton(text='промокодик)', callback_data='promo')
btnarbuz3 = InlineKeyboardButton(text='назад', callback_data='scheme2023')

ikmarbuz.add(btnarbuz1, btnarbuz2, btnarbuz3)

ikmbc = InlineKeyboardMarkup(row_width=1)

bc = InlineKeyboardButton(text='назад', callback_data='arbuz1')

ikmbc.add(bc)
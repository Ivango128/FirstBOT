from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = AsyncTeleBot('6286035570:AAGUyK_aRQaZdERTc3ZDYB5fqY-mcH6UWQM')

def generate_reply_keyboard(list_buttons, row):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_buttons, row_width=row)
    return markup


def create_keyboard_markup(button_dict):
    markup = InlineKeyboardMarkup()
    for button_text, callback_data in button_dict.items():
        button = InlineKeyboardButton(button_text, callback_data=callback_data)
        markup.add(button)

    return markup

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    chat_id = message.from_user.id
    button_dict = {'Первая кнопка': 'first',
                   'Вторая кнопка': 'second',
                   'Третья кнопка' : 'three'
                   }
    await bot.send_message(chat_id, 'Первый вариант кнопок', reply_markup=create_keyboard_markup(button_dict))


@bot.callback_query_handler(func=lambda call: True)
async def handle_callback(call):
    chat_id = call.message.chat.id
    button_call = call.data
    if button_call == 'first':
        await bot.send_message(chat_id, 'Вы нажали кнопку 1')
    elif button_call == 'second':
        await bot.send_message(chat_id, 'Вы нажали кнопку 2')
    elif button_call == 'three':
        await bot.send_message(chat_id, 'Вы нажали кнопку 3')




@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text
    text_message = text_message.lower()
    if 'дела' in text_message  or 'настроение' in text_message:
        await bot.reply_to(message, 'Хорошо, а у тебя?')
    elif 'шутка' in text_message or 'анекдот' in text_message:
        await bot.reply_to(message, 'Колобок повесился')
    else:
        await bot.reply_to(message, 'Извините я вас не понял?')

import asyncio
asyncio.run(bot.polling())


session = {
    'first_name': 'Иванов Иван',
    'old':16
}

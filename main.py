from telebot.async_telebot import AsyncTeleBot
import wikipedia, re
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN, parse_mode='HTML')

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:4000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
#Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
async def start(m, res=False):
    await bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
#Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
async def handle_text(message):
    await bot.send_message(message.chat.id, getwiki(message.text))
#Запускаем бота


async def main():
    await bot.polling()

import asyncio
asyncio.run(main())



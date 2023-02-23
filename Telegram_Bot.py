from aiogram import Bot, Dispatcher ,executor, types

import requests
import datetime
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN_API='5909256359:AAF_ERx3U_dIhvMrrIHpeirEhTzxXGUgr-s'
API='85b4238efd01857c933287e532def16b'
bot=Bot(token=TOKEN_API)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.reply('Привет, напиши город')              # написать сообщение

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API}&lang=ru&units=metric')
        date=r.json()
        name=date['name']
        country=date['sys']['country']
        cur_weather=date['main']['temp']
        humidity=date['main']['humidity']
        pressure = date['main']['pressure']
        wind = date['wind']['speed']
        sunrise_time=datetime.datetime.fromtimestamp(date['sys']['sunrise'])
        sunset_time=datetime.datetime.fromtimestamp(date['sys']['sunset'])

        await message.reply(f'Город:{name}\nСтрана:{country}\nТемпература:{cur_weather}℃\n'
              f'Влажность:{humidity}%\nДавление:{pressure}мм.рт.ст.\n'
              f'Ветер:{wind}м/c\nВосход:{sunrise_time}\nЗакат:{sunset_time}\n'
              f'Путин:\U00002620 пока не сдох \U00002620')

    except:
        await message.reply('no information, try again')



if __name__ == '__main__':
    executor.start_polling(dp)

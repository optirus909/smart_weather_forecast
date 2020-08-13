import time
import telepot
from telepot.loop import MessageLoop
import sqlite3

from client import WeatherClient


class WeatherBot:

    def __init__(self, telegram_api_token, weather_api_key):
        self._bot = telepot.Bot(telegram_api_token)
        self._weather = WeatherClient(weather_api_key)

    def _handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type != 'text':
            self._bot.sendMessage(chat_id, 'Please, enter only text.')
            return
        if msg['text'] == '/getweather':
            self._bot.sendMessage(chat_id, 'Please, enter your city')
        elif msg['text'] == '/start':
            self._bot.sendMessage(chat_id, 'Hello, {}!\n'
                                           'I\'m smart weather bot.\n'
                                           'I can tell you about the weather in your city.\n'
                                           'To find out the weather just write /getweather or enter the city name.'
                                  .format(msg['from']['first_name']))
        else:
            self._bot.sendMessage(chat_id, self._weather.get_weather(msg['text']))

    def run(self):
        MessageLoop(self._bot, self._handle).run_as_thread()
        print('Listening ...')

        while 1:
            time.sleep(10)

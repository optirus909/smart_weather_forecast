import sys
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import requests

import bot_config


class WeatherBot:

    _api_url = 'http://api.openweathermap.org/'
    GET = 0
    POST = 1

    def __init__(self, api_key):
        self._api_key = api_key

    def _request(self, path, params, request_type):
        params.update({'appid': self._api_key})

        if request_type == self.GET:
            return requests.get(self._api_url + path, params=params)
        elif request_type == self.POST:
            return requests.post(self._api_url + path, params=params)

    def get_weather(self, city):
        params = {'q': city}
        return self._request('data/2.5/weather', params, self.GET).json()




def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)

    if content_type != 'text':
        bot.sendMessage(chat_id, 'Please, enter only text.')
        return

    if msg['text'] == '/getweather':

        bot.sendMessage(chat_id, weather.get_weather('Saint Petersburg'))

if __name__ == '__main__':
    weather = WeatherBot(bot_config.WEATHER_API_KEY)

    bot = telepot.Bot(bot_config.BOT_TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    print ('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)
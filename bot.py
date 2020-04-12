import time
import telepot
from telepot.loop import MessageLoop
import sqlite3

from client import WeatherClient


class WeatherBot:

    def __init__(self, telegram_api_token, weather_api_key):
        self._bot = telepot.Bot(telegram_api_token)
        self._weather = WeatherClient(weather_api_key)
        self._current_state = 'country'
        with sqlite3.connect('users_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("create table if not exists loc (id text, country text, city text)")
            conn.commit()




    def _handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        # print(msg)

        if content_type != 'text':
            self._bot.sendMessage(chat_id, 'Please, enter only text.')
            return

        if msg['text'] == '/getweather':
            self._bot.sendMessage(chat_id, self._weather.get_weather(self._get_location(chat_id)))
        elif msg['text'] == '/setlocation' or self._current_state != 'country':
            self._set_location(chat_id, msg['text'])
        elif msg['text'] == '/start':
            self._bot.sendMessage(chat_id, 'Hello, {} {}!\n'
                                           'Type /setlocation to start.'.format(msg['from']['first_name'], msg['from']['last_name']))

    def _get_location(self, chat_id):
        with sqlite3.connect('users_data.db') as conn:
            cursor = conn.cursor()
            print(chat_id)
            try:
                cursor.execute("SELECT * FROM loc WHERE id=?", (str(chat_id),))
            except Exception as e:
                self._bot.sendMessage(chat_id, 'Please, set correct city name.')
            data = cursor.fetchall()
            print(data)
            return data[0][2]

    def _set_location(self, chat_id, text):
        if self._current_state == 'country':
            self._bot.sendMessage(chat_id, 'Please, enter your country:')
            self._current_state = 'city'
        elif self._current_state == 'city':
            self._temp_data = {'country': text}
            self._bot.sendMessage(chat_id, 'Please, enter your city:')
            self._current_state = 'finish'
        elif self._current_state == 'finish':
            self._temp_data.update({'city': text})
            self._bot.sendMessage(chat_id, 'Your location: {}, {}'.format(self._temp_data['city'],
                                                                          self._temp_data['country']))
            print(self._temp_data)
            with sqlite3.connect('users_data.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT EXISTS( SELECT * FROM loc WHERE id = ? LIMIT 1)", (str(chat_id),))
                flag = cursor.fetchall()
                try:
                    if flag[0][0]:
                        cursor.execute("UPDATE loc SET country=?, city=? WHERE id=?", (self._temp_data['country'],
                                 self._temp_data['city'], str(chat_id)))
                    else:
                        cursor.execute("INSERT INTO loc VALUES (?, ?, ?)", (str(chat_id), self._temp_data['country'],
                                 self._temp_data['city']))
                    conn.commit()
                except Exception as e:
                    self._bot.sendMessage(chat_id, 'Please, set correct data.')
                self._current_state = 'country'


    def run(self):
        MessageLoop(self._bot, self._handle).run_as_thread()
        print('Listening ...')

        # Keep the program running.
        while 1:
            time.sleep(10)

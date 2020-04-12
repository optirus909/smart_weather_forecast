# Умный сервис прогноза погоды
# Средний уровень сложности

## Проектирование сервиса
  - Использованный стек технологий: Python 3, Sqlite, Telegram Bot API, OpenWeather API
  - Пользовательский интерфейс: чат-бот в Telegram
  - Данные о погоде, полученные с API, подставляются в тестовый шаблон 'Weather in {city} now: Temperature: {temp}°C [{min_temp}°C...{max_temp}°C] Feels like: {fl_temp}°C Pressure: {pressure} mmHg Humidity: {humidity}% Wind: {windspeed} m/s ({winddirection})' и отправляются пользователю.
## Процесс работы программы
  
  Данные приходят от пользователя через интерфейс мессенджера
  - формируется и отправляется запрос в базу данных
  - полученный ответ из базы используется для формирования ответа пользователю
  - ответ отправляется пользователю
  
## Демонстрация работы сервиса
 Посмотрите, как работает сервис, перейдя [по ссылке.](https://youtu.be/ke0G2mtqqlc)
 
### Запуск программы:
   Введите ваши ключи от [Telegram Bot API](https://core.telegram.org/bots/api), [OpenWeather API](https://openweathermap.org/api) в файл bot_config.py
 ```
 [bot_config.py]
 #Telegram
 BOT_TOKEN = 'Place your token here'

 #Weather api
 WEATHER_API_KEY = 'Place your token here'
 ```
  Активируйте venv.
  
 ```
 source venv/bin/activate 
 ```
   Запустите бота из его директории.
 ```
 python3 main.py
 ```

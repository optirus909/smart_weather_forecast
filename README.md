### Название задачи
Умный сервис прогноза погоды

### Уровень сложности 
Задача со звездочкой

## Проектирование сервиса
  - **Использованный стек технологий:** Python 3, [Telegram Bot API](https://core.telegram.org/bots/api), [OpenWeather API](https://openweathermap.org/api)
  - **Пользовательский интерфейс:** чат-бот в Telegram
  - **Формат ответа:**
  Данные о погоде, полученные с API, подставляются в текстовый шаблон и отправляются пользователю. Рекомендации{recommendations} формируются на основе температуры и поля 'main' из API response.
   ```
  📍 {city}, {country} : {emoji} {weather}
  
  🌡 {temp}°C
  Feels Like: {fl_temp}°C
  
  💨 {windspeed} m/s ({winddirection})
  
  💧 {humidity}%
  ⏱ {pressure} mmHg
  
  ✅️ {recommendations}
   ```
  
## Процесс работы программы
  1. Данные о населенном пункте запрашиваются у пользователя через интерфейс Telegram бота.
  2. По этим данным формируется API запрос на сервер OpenWeather для получения погодных данных.
  3. Полученные данные о погоде обрабатываются.
  4. Обработанные данные отправляются пользователю.
  
## Демонстрация работы сервиса
 Посмотрите, как работает сервис, перейдя [по ссылке.](https://youtu.be/uK6JyQkJEpg)
 
## Установка и запуск программы:
Скачайте репозиторий 

 ```console
foo@bar:~$ git clone https://github.com/optirus909/smart_weather_forecast.git
 ```

Введите ваши ключи от [Telegram Bot API](https://core.telegram.org/bots/api), [OpenWeather API](https://openweathermap.org/api) в файл bot_config.py
 ```
 [bot_config.py]
 #Telegram
 BOT_TOKEN = 'Place your token here'

 #Weather api
 WEATHER_API_KEY = 'Place your token here'
 ```
  Активируйте venv.
 ```console
foo@bar:smart_weather_forecast$ source venv/bin/activate 
 ```
   Запустите бота из его директории.
 ```console
foo@bar:smart_weather_forecast$ python3 main.py 
```

import requests


class WeatherClient:

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

    def _get_wind_direction(self, deg):
        if 0.0 <= deg < 22.5 or 337.5 < deg <= 360.0:
            return 'North'
        if 22.5 <= deg < 67.5:
            return 'North-East'
        if 67.5 <= deg < 112.5:
            return 'East'
        if 112.5 <= deg < 157.5:
            return 'South-East'
        if 157.5 <= deg < 202.5:
            return 'South'
        if 202.5 <= deg < 247.5:
            return 'South-West'
        if 247.5 <= deg < 292.5:
            return 'West'
        if 292.5 <= deg < 337.5:
            return 'North-West'

    def _get_pretty_temperature(self, temp):
        temp = int(temp)
        return temp if temp <= 0 else '+' + str(temp)

    def _get_weather_emoji(self, description):
        if description == "Rain":
            return "🌧"
        elif description == "Clear":
            return "☀️"
        elif description == "Thunderstorm":
            return "⛈"
        elif description == "Clouds":
            return "☁️"
        elif description == "Tornado":
            return "🌪"
        elif description == "Snow":
            return "❄️"
        else:
            return "🌫"

    def _get_recommendations(self, weather):
        resp = ''

        temperature = weather['main']['temp']
        description = weather['weather'][0]['main']

        if temperature > 20:
            resp += 'The weather is fine!\n Wear a t-shirt and shorts.'
        elif temperature > 10:
            resp += 'A little chilly. Put on a shirt or sweater\n and the day will be comfortable!'
        elif temperature > 0:
            resp += 'Put on your jacket, it\'s cold enough today!'
        else:
            resp += 'It\'s very cold today, don\'t forget your scarf and hat!'

        if description == "Rain":
            resp += '\n The weather is rainy, take an umbrella with you.'
        elif description == "Clear":
            resp += '\n The sky is clear, take your sunglasses with you.'

        return resp

    def _format_weather(self, res):
        return '📍 {city}, {country} : {emoji} {weather}\n\n' \
               '🌡 {temp}°C \n' \
               'Feels Like: {fl_temp}°C\n\n' \
               '💨 {windspeed} m/s ({winddirection})\n\n' \
               '💧 {humidity}%\n' \
               '⏱ {pressure} mmHg\n\n' \
               '✅️ {recommendations}' \
               ''.format(city=res['name'],
                         country=res['sys']['country'],
                         weather=res['weather'][0]['description'].title(),
                         emoji=self._get_weather_emoji(res['weather'][0]['main']),
                         temp=self._get_pretty_temperature(res['main']['temp']),
                         fl_temp=self._get_pretty_temperature(res['main']['feels_like']),
                         pressure=res['main']['pressure'],
                         humidity=res['main']['humidity'],
                         windspeed=int(res['wind']['speed']),
                         winddirection=self._get_wind_direction(res['wind']['deg']),
                         recommendations=self._get_recommendations(res))

    def get_weather(self, city):
        params = {'q': city, 'units': 'metric'}
        try:
            res = self._request('data/2.5/weather', params, self.GET).json()
            return self._format_weather(res)
            #return res

        except Exception as err:
            print(err)
            return 'Please, enter correct city name.'

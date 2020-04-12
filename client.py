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

    def _format_weather(self, res):
        return 'Weather in {city} now:\n' \
               'Temperature: {temp}°C ' \
               '[{min_temp}°C...{max_temp}°C]\n' \
               'Feels like: {fl_temp}°C\n' \
               'Pressure: {pressure} mmHg\n' \
               'Humidity: {humidity}%\n' \
               'Wind: {windspeed} m/s ({winddirection})' \
               ''.format(city=res['name'],
                         temp=self._get_pretty_temperature(res['main']['temp']),
                         min_temp=self._get_pretty_temperature(res['main']['temp_min']),
                         max_temp=self._get_pretty_temperature(res['main']['temp_max']),
                         fl_temp=self._get_pretty_temperature(res['main']['feels_like']),
                         pressure=res['main']['pressure'],
                         humidity=res['main']['humidity'],
                         windspeed=int(res['wind']['speed']),
                         winddirection=self._get_wind_direction(res['wind']['deg']))

    def get_weather(self, city):
        params = {'q': city, 'units': 'metric'}

        try:
            res = self._request('data/2.5/weather', params, self.GET).json()
            return self._format_weather(res)
            #return res

        except Exception as err:
            print(err)
            return 'Please, enter correct city name using /setlocation command.'

from bot import WeatherBot
import bot_config


if __name__ == '__main__':
    bot = WeatherBot(bot_config.BOT_TOKEN, bot_config.WEATHER_API_KEY)
    bot.run()

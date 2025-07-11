"""Entry point for running the internet speed Twitter bot."""

from Speedtwitterbot import InternetSpeedTwitterBot
from config import Settings

settings = Settings()

bot = InternetSpeedTwitterBot(headless=settings.headless, wait_timeout=settings.wait_timeout)
bot.get_internet_speed()

if bot.down < settings.promised_down or bot.up < settings.promised_up:
    message = (
        f"Hey Internet Provider, why is my internet speed {bot.down}down/{bot.up}up "
        f"when I pay for {settings.promised_down}down/{settings.promised_up}up?"
    )
    bot.tweet_at_provider(
        user=settings.twitter_username,
        password=settings.twitter_password,
        message=message,
    )

bot.close()

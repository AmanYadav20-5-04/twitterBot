import time
import os
from dotenv import load_dotenv
from Speedtwitterbot import InternetSpeedTwitterBot

# Load environment variables
load_dotenv()

PROMISED_UP = 1000
PROMISED_DOWN = 1000
TWITTER_USERNAME = os.getenv("USERNAME")
TWITTER_PASSWORD = os.getenv("PASSWORD")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    message = f"Hey Internet Provider, why is my internet speed {bot.down}down/{bot.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    bot.tweet_at_provider(user=TWITTER_USERNAME, password=TWITTER_PASSWORD, message=message)

bot.close()

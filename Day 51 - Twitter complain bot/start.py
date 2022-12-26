from internetspeed import InternetSpeedTwitterBot

URL = 'https://twitter.com/home'
URL_SPEEDTEST = 'https://www.speedtest.net/'

bot = InternetSpeedTwitterBot()
bot.get_internet_speed(URL_SPEEDTEST)
bot.tweet_at_provider(URL)

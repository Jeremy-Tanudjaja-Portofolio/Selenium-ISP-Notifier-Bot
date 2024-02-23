from internet_bot import InternetBot

PROMISED_INTERNET_SPEED = 100

internet_bot = InternetBot()
print(internet_bot.download_speed)
if internet_bot.download_speed < PROMISED_INTERNET_SPEED:
    internet_bot.contact_provider_twitter()
# pip install pyowm==2.4.0
# pip install pyTelegramBotAPI
# pip install --upgrade Pillow
from PIL import Image
import telebot
from telebot import types
import pyowm
image = 'https://iconstore.co/assets/img/set/cover/weather-featured-2.png'
token = "1800339477:AAHLp5gj2HIOZjbwQbduiTaXU56pa5gB47s"
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def get_text_messages(message):

    city = (message.text)
    owm = pyowm.OWM('f269eae02c9ea8ff52358c84defaedd7')
    observation = owm.weather_at_place(city)
    w = observation.get_weather()

    status = w.get_status()
    if status == 'Clear':
        status = 'ясно'
        image =
    elif status == 'Clouds':
        status = 'облачно'
    elif status == 'Rain':
        status = "дождь"
    elif status == 'Haze':
        status = "туманно"

    temprmax = w.get_temperature('celsius')['temp_max']
    tempr = w.get_temperature('celsius')['temp']
    temprmin = w.get_temperature('celsius')['temp_min']
    humid = w.get_humidity()
    windspeed = w.get_wind()['speed']
    pressure = w.get_pressure()['press']
    bot.send_message(message.from_user.id , "Сегодня в городе " + (str(city)) + " " + (str(status)))
    bot.send_message(message.from_user.id , 'В указанном городе, текущая температура за день, составляет ' + str(int(tempr)) + " по цельсию. Максимальная и минимальная температура составляет " + str(int(temprmax)) + " и " + str(int(temprmin)) + " градусов соответственно")
    bot.send_message(message.from_user.id , "Влажность воздуха - " + str(int(humid)) + "%. Скорость ветра - " + str(int(windspeed)) + " км/час.")
    bot.send_message(message.from_user.id , "Атмосферное давление равно " + str(int(pressure)) + " Па.")
    bot.send_photo(message.from_user.id, 'https://www.kidszine.co.uk/wp-content/uploads/2017/03/clouds-in-the-sky-750x450.jpg')
bot.polling(none_stop=True, interval=0)

#Вступление
    # if message.text == "sdfgsdfgsdfgsdfgsdfgsdrgd7ыврЫЫ№;":
    #      bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    # elif message.text == "/city":
    #      bot.send_message(message.from_user.id, "Введите город")
    # else:
    #     bot.send_message(message.from_user.id, "Приветствую вас! чтобы запустить бота введите /city")
import telebot
from telebot import types
import pyowm
from translate import Translator as tr
tr = tr(to_lang='Russian')
token = "1800339477:AAHLp5gj2HIOZjbwQbduiTaXU56pa5gB47s"
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def get_text_messages(message):

    city = (message.text)
    owm = pyowm.OWM('f269eae02c9ea8ff52358c84defaedd7')
    observation = owm.weather_at_place(city)
    w = observation.get_weather()

    status = w.get_status()
    if status == 'clear':
        status = 'ясно'
    if status == 'clouds':
        status = 'облачно'
    if status == 'rain':
        status = "дождь"
    temprmax = w.get_temperature('celsius')['temp_max']
    tempr = w.get_temperature('celsius')['temp']
    temprmin = w.get_temperature('celsius')['temp_min']
    humid = w.get_humidity()
    windspeed = w.get_wind()['speed']
    pressure = w.get_pressure()['press']
    bot.send_message(message.from_user.id , "Сегодня в " + (str(city)) + " " + (str(status)))
    bot.send_message(message.from_user.id , 'В указанном городе, текущая температура составляет ' + str(int(tempr)) + " по цельсию. Максимальная и минимальная температура составляет " + str(int(temprmax)) + " и " + str(int(temprmin)) + " градусов соответственно")
    bot.send_message(message.from_user.id , "Влажность воздуха - " + str(int(humid)) + "%. Скорость ветра - " + str(int(windspeed)) + " км/час.")
    bot.send_message(message.from_user.id , "Атмосферное давление равно " + str(int(pressure)) + " Па.")
bot.polling(none_stop=True, interval=0)

#Вступление
    # if message.text == "sdfgsdfgsdfgsdfgsdfgsdrgd7ыврЫЫ№;":
    #      bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    # elif message.text == "/city":
    #      bot.send_message(message.from_user.id, "Введите город")
    # else:
    #     bot.send_message(message.from_user.id, "Приветствую вас! чтобы запустить бота введите /city")
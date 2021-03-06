from pythonping import ping
import socket
import telebot

bot = telebot.TeleBot('-Тут нужно вписать ТОКЕН-')


def echo(message) -> object:
    try:
        ip = socket.gethostbyname(message.text)
        reStr = str(ping(ip, count=1, payload=bytes(10)))
        bot.reply_to(message, reStr)
        print('Запрос --> ' + message.text)
        print('Ответь --> \n' + reStr)
    except socket.error:
        bot.reply_to(message, message.text + ' - Не удается получить IP адрес...')
        print(message.text + ' - Не удается получить IP адрес...')
    return


@bot.message_handler(content_types=['text'])
def send_text(message):
    echo(message)


bot.polling()

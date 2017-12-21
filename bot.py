import telebot
TOKEN = '506872809:AAF2mRfM2sMjkKGW8MBjeF_cwfiMUhPqgeA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

bot.polling()

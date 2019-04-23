import telebot;

API_TOKEN = "673205922:AAG7f84ENFM7jYi-znqPLpmyv5i6qegIsSE"

bot = telebot.TeleBot(API_TOKEN);

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
 bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)
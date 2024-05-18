import os
import telebot



API_TOKEN = '6597715687:AAE-LjeggzIJ3NcyjPswc1CG7iuyxqU_n10'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text=message.chat.id)

def send_pdf(chat_id, file_name):
    pdf_filename = f'../pdfs/{file_name}'
    if os.path.exists(pdf_filename):
        with open(pdf_filename, 'rb') as pdf_file:
            bot.send_document(chat_id, document=pdf_file)
    else:
        return

def start_bot():
    bot.infinity_polling()


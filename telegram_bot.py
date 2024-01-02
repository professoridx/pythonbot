import telebot
from qrbot import *
import os

API_TOKEN = '6495322558:AAGkkAdzQMGPbt3EktAZ5a-jNMhQGz7MN74'

bot = telebot.TeleBot(API_TOKEN)
bot_username="@thepr0fessor_bot"


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
        
Hi there, I am TheProfessor Bot.
I have some spacifaction 
✅ I can find Weather ❄️\n
✅ I can Convert Money 💷\n
✅ Temp email \n
✅ Email Scrapper \n
✅ Translator\n
✅ +===========loding
""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
    """hello \n
    1.for Create Qr code after send /Qrcode yourlink 
    2.for Create animated Qrcode send /Aqrcode yourlink
    """
    )
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['Qrcode'])

def Qrbot(message):
    textc=message.text[8:]
    userID=message.chat.id
    print(textc)
    create_qrcode(textc)
    
    output_folder=f"pythonbot/output/image.png"
    
    with open(output_folder,"rb") as photo:
        bot.send_photo(
            userID,
            photo,
            caption=f"""#️⃣{textc}\n
            {bot_username}""", 
            
           )
        
        

bot.infinity_polling()
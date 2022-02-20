import telebot
import config
from datetime import date
import schedule, time
from send_doc import send_html_email

bot= telebot.TeleBot(config.API_KEY, parse_mode=None)

@bot.message_handler(commands=["start"])
# def send_basic_message(msg):
  # bot.reply_to(msg, "Hello!")
  # bot.send_dice(chat_id=msg.chat.id)
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Welcome! What's your name?")
    bot.register_next_step_handler(sent_msg, name_handler)
    
def name_handler(pm):
    name = pm.text
    sent_msg = bot.send_message(pm.chat.id, f"👋🏻 {name}.\nShare what did you take away from WE this week!")
    bot.register_next_step_handler(sent_msg, save_message_and_end, name)

def save_message_and_end(pm, name):
    message = pm.text
    print("* Message from " + name + ": " + message)
    text_file = open("Service Feedback – Boldest for Christ 2 – 05022022.txt", "a")
    text_file.write(name + '\n' + message + '\n')
    text_file.close()
    bot.send_message(pm.chat.id, "Got your service feedback! \n\nHave a great week ahead with what you've learned! 🥰🥰🥰 \n\nHere's the number of >1KM runs you have to complete from eating too many pineapple tarts 🌚🌚🌚")
    bot.send_dice(chat_id=pm.chat.id)

bot.polling()

def action():
    send_html_email(config.EMAIL_SUBJECT_PREFIX + " " + 
                    date.today().strftime("%d %b %Y"))

schedule.every().sunday.at(config.TIME_TO_SEND_EMAIL).do(action)

while True:
    schedule.run_pending()
    time.sleep(1)
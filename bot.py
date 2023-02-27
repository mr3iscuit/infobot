import telebot
from telebot import types
import datetime
date_of_birth = 2003

# create a new bot instance
bot = telebot.TeleBot('1711167074:AAG6KWdPZ_iAQ7pQkJc5y_Q2mdxWJ2-pUYM')

first_name = "Eyvaz"
last_name = "Bayramov"
date_of_birth = datetime.datetime(2003, 11, 20) 


# handler function for the /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
    # create an inline keyboard with options for the user
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    name_button = types.InlineKeyboardButton('My name', callback_data='name')
    age_button = types.InlineKeyboardButton('My age', callback_data='age')
    keyboard.add(name_button, age_button)

    # send a message to the user with the keyboard
    bot.send_message(message.chat.id, 'Hello! What information would you like to know?', reply_markup=keyboard)

# handler function for inline keyboard callbacks
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'name':
        # respond with the user's name
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"Your name is {first_name} {last_name}")
    elif call.data == 'age':
        # calculate the user's age based on the date of birth in their profile and respond with it
        bot.answer_callback_query(call.id)
        age = calculate_age(date_of_birth)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"You are {age} years old.")

def calculate_age(born):
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age

# start the bot
bot.polling()


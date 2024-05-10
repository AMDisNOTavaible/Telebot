import telebot
import time
from telebot import types
import random
import environ

env = environ.Env()
environ.Env.read_env()
token = env('token', )
bot = telebot.TeleBot(token=token)



@bot.message_handler(func= lambda message: message.text == 'привет' or message.text == 'Привет')
@bot.message_handler(commands=['start','restart'])
def start(message):
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(text="/run")
    button2 = types.KeyboardButton(text="/restart")

    numbut1 = types.KeyboardButton(text='2')
    numbut2 = types.KeyboardButton(text='3')
    numbut3 = types.KeyboardButton(text='4')
    numbut4 = types.KeyboardButton(text='5')
    

    keyboards.add(button1,button2)
    keyboards.add(numbut1,numbut2,numbut3,numbut4)
    
    

    start = bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}' )

    time.sleep(0.5)

    bot.send_message(message.chat.id, 'Загружаю ваши кнопки...', reply_markup=keyboards)
    
    time.sleep(0.5)

    bot.send_message(message.chat.id, "Я готов принять кол-во переменных")

    bot.register_next_step_handler(start, zxc)

def zxc(message): 
    global colichestvo
    colichestvo = []

    peremennie = message.text

    colichestvo.append(peremennie)

    colvo_peremennih = bot.send_message(message.chat.id, f'Вы выбрали {peremennie} переменных, напишите "/run" что бы запустить код')

@bot.message_handler(commands='run')

def qwe(message):
    
    peremennie = colichestvo[0]

    if peremennie == "2":

        fperem = bot.send_message(message.chat.id, 'Напишите первую переменную')

        bot.register_next_step_handler(fperem, peremen)

    elif peremennie == '3':

        fperem = bot.send_message(message.chat.id, 'Напишите первую переменную')

        bot.register_next_step_handler(fperem, apelsin)

    elif peremennie == '4':

        fperem = bot.send_message(message.chat.id, 'Напишите первую переменную')

        bot.register_next_step_handler(fperem, mandarinka)

    elif peremennie == '5':
        
        fperem = bot.send_message(message.chat.id, 'Напишите первую переменную')

        bot.register_next_step_handler(fperem, papaya)

    else:
        bot.send_message(message.chat.id, 'Неа, надо написать от 2 до 5, перезапуск /restart')


def peremen(message):
    global massiv

    massiv = []

    perem1 = message.text

    massiv.append(perem1)

    sperem = bot.send_message(message.chat.id, 'Напишите вторую переменную')

    bot.register_next_step_handler(sperem, peremen2)

def peremen2(message):

    a = random.randint(1,2)

    perem1 = massiv[0]

    perem2 = message.text

    massiv.append(perem2)

    if a == 1:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem1}.")
    elif a == 2:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem2}.")

    bot.send_message(message.chat.id, 'Что бы перевыбрать кол-во переменных напишите /restart')

def apelsin(message):
    global massiv

    massiv = []

    perem1 = message.text

    massiv.append(perem1)

    sperem = bot.send_message(message.chat.id, 'Напишите вторую переменную')

    bot.register_next_step_handler(sperem, apelsin2)

def apelsin2(message):

    perem1 = massiv[0]

    perem2 = message.text

    massiv.append(perem2)

    tperem = bot.send_message(message.chat.id, 'Напишите третью переменную')

    bot.register_next_step_handler(tperem, apelsin3)

def apelsin3(message):

    a = random.randint(1,3)

    perem1 = massiv[0]

    perem2 = massiv[1]

    perem3 = message.text

    massiv.append(perem3)

    if a == 1:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem1}")
    elif a == 2:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem2}")
    elif a == 3:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem3}")

    bot.send_message(message.chat.id, 'Что бы перевыбрать кол-во переменных напишите /restart')

def mandarinka(message):
    global massiv

    massiv = []

    perem1 = message.text

    massiv.append(perem1)

    sperem = bot.send_message(message.chat.id, 'Напишите вторую переменную')

    bot.register_next_step_handler(sperem, mandarinka2)

def mandarinka2(message):

    perem1 = massiv[0]

    perem2 = message.text

    massiv.append(perem2)

    tperem = bot.send_message(message.chat.id, 'Напишите третью переменную')

    bot.register_next_step_handler(tperem, mandarinka3)

def mandarinka3(message):
    
    perem1 = massiv[0]

    perem2 = massiv[1]

    perem3 = message.text

    massiv.append(perem3)

    fperem = bot.send_message(message.chat.id, 'Напишите четвертую переменную')

    bot.register_next_step_handler(fperem, mandarinka4)

def mandarinka4(message):

    a = random.randint(1,4)

    perem1 = massiv[0]

    perem2 = massiv[1]

    perem3 = massiv[2]

    perem4 = message.text

    massiv.append(perem4)

    if a == 1:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem1}")
    elif a == 2:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem2}")
    elif a == 3:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem3}")
    elif a == 4:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem4}")

    bot.send_message(message.chat.id, 'Что бы перевыбрать кол-во переменных напишите /restart')

def papaya(message):

    global massiv

    massiv = []

    perem1 = message.text

    massiv.append(perem1)

    sperem = bot.send_message(message.chat.id, 'Напишите вторую переменную')

    bot.register_next_step_handler(sperem, papaya2)

def papaya2(message):

    perem1 = massiv[0]

    perem2 = message.text

    massiv.append(perem2)

    tperem = bot.send_message(message.chat.id, 'Напишите третью переменную')

    bot.register_next_step_handler(tperem, papaya3)

def papaya3(message):
    
    perem1 = massiv[0]

    perem2 = massiv[1]

    perem3 = message.text

    massiv.append(perem3)

    fperem = bot.send_message(message.chat.id, 'Напишите четвертую переменную')

    bot.register_next_step_handler(fperem, papaya4)

def papaya4(message):

    perem1 = massiv[0]

    perem2 = massiv[1]

    perem3 = massiv[2]

    perem4 = message.text

    massiv.append(perem4)

    ffperem = bot.send_message(message.chat.id, 'Напишите пятую переменную')

    bot.register_next_step_handler(ffperem, papaya5)

def papaya5(message):

    a = random.randint(1,5)

    perem1 = massiv[0]

    perem2 = massiv[1]

    perem3 = massiv[2]

    perem4 = massiv[3]

    perem5 = message.text

    massiv.append(perem5)

    if a == 1:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem1}")
    elif a == 2:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem2}")
    elif a == 3:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem3}")
    elif a == 4:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem4}")
    elif a == 5:
        bot.send_message(message.chat.id, f"Мне нравится вариант: {perem5}")

    bot.send_message(message.chat.id, 'Что бы перевыбрать кол-во переменных напишите /restart')








bot.polling(none_stop=True)
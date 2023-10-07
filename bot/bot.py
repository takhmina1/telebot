import telebot 
import webbrowser



   


bot = telebot.TeleBot('6321289483:AAGu81uMJu5jpYCJstG5MCp3s0iQi7ovnPw')

@bot.message_handler(commands=['start','hello'])
def star(message):
    bot.send_message(message.chat.id,f'Hello {message.from_user.first_name}')
    
    
    
   
   
@bot.message_handler(commands=['site','website'])
def star(message):
    webbrowser.open('https://www.google.com/search?q=youtube&oq=youtube&aqs=chrome.0.0i271j46i131i199i433i465i512j69i59j0i131i433i512j0i512j0i131i433i512j69i60l2.11670j1j7&sourceid=chrome&ie=UTF-8')
    
        
    
    
    
    

@bot.message_handler()
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id,"Hello you")

    
    
    
    
    
    
    
bot.polling(none_stop=True) 
    
    
    
    

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
   
    
    

# 'homework'
    
    
# import telebot
# from telebot import types
# import random




    


# keyboard = types.ReplyKeyboardMarkup()

# button1 = types.KeyboardButton('Играть')
# button2 = types.KeyboardButton('Нет')

# keyboard.add(button1, button2)

# @bot.HelpBot(commands=['start', 'hello', 'hi'])


# def check_answer(message):

#   if message.text == 'Играть':

#     bot.send_message(message.chat.id, 'Ок, тогда вот правила, нужно угадать число от 1 до 10 за 3 попытки')
  
#     random_number = random.choice(range(1, 11))
    
#     print(random_number)
 
#     game(message, 3, random_number)


#   else:
#     bot.send_message(message.chat.id, 'Окей, до встречи')

# def game(message, attempts, random_number):
#   msg = bot.send_message(message.chat.id, 'Выберите число')

#   bot.register_next_step_handler(msg, check_number, attempts - 1, random_number)

# def check_number(message, attempts, random_number):

#   if message.text == str(random_number):
  
#     bot.send_message(message.chat.id, 'Вы победили')
  
#   elif attempts == 0:
#     bot.send_message(message.chat.id, f'Извините, у вас закончились попытки, число было {random_number}')
  
#   else:
#     bot.send_message(message.chat.id, f'Попробуйте еще раз, у вас осталось {attempts} попыток')
  
#     game(message, attempts, random_number)


    
    





    
    
    

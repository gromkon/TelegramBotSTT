import telebot
from datetime import datetime

#имя бота
#@testcrtgrombot

#bot - переменная, с помощью которой можно обращаться к боту
bot = telebot.TeleBot('928505119:AAEvgM9FJnuItQ7gxNwYryLYjmyB2O15-ng')

#список пользователей
usersId = []

#список мест
camerasLocation = ['Ашан Ивантеевская ул. 25А', 'Ашан Бойцовская ул. 2к30', 'ТРК Атриум', 'Метро Бауманская', 'МГТУ им. Баумана ГЗ', 'МГТУ им. Баумана УЛК', 'Назад']
#список камер
cameras_location_0 = ['у главного входа', 'у входа № 1', 'у входа № 2', 'у входа № 3', 'я не знаю', 'назад']
cameras_location_1 = ['у главного входа', 'у входа № 1', 'у входа № 2', 'Я не знаю', 'назад']
cameras_location_2 = ['у главного входа', 'у входа cо стороны вокзала', 'у дополнительного входа', 'Я не знаю', 'назад']
cameras_location_3 = ['у входа в метро', 'у выхода из метро', 'Я не знаю', 'назад']
cameras_location_4 = ['у входа с Яузы', 'у входа с главного КПП', 'у входа с дополнительного КПП', 'Я не знаю', 'назад']
cameras_location_5 = ['у входа с Яузы', 'у главного входа', 'Я не знаю', 'назад']

#словарь составления сообщений
composingMessages = {}

#текущий номер преступника
iterCriminals = 1
#список преступников
criminals = {1: 'Иванов Иван Иванович, дата рождения 12.03.1957, преступник', 2: 'Синичкин Василий Андреевич , дата рождения 07.12.1985, преступник',
             3: 'Уткин Дмитрий Сергеевич, дата рождения 27.08.1991, хулиган', 4: 'Курнешова Мария Викторовна, дата рождения 20.09.1970, преступница'}



#добавления пользователя в список пользователей
def add_id(check_id):
    if check_id in usersId:
        bot.send_message(check_id, 'Ты уже подписан на мои уведомления')
    else:
        bot.send_message(check_id, 'Привет, я бот для отслеживания преступников. Если кого-то увидишь, пиши!',
                         reply_markup=keyboard_terror)
        usersId.append(check_id)



#удаления пользователя из списка пользователей
def del_id(check_id):
    try:
        usersId.remove(check_id)
        bot.send_message(check_id, 'Я больше не буду тебя беспокоить, если захочешь подписаться на мою рассылку, введи /start')
    except:
        print(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' функция del_id, пользователь '
              + str(check_id) + ' отправил запрос на удаление, но не был найден в списке подписчиков')
        print(usersId)
        bot.send_message(check_id, 'Ты не подписан на мои уведомления')



#отправляет сообщение всем пользователям
def send_text_to_all(message):
    global iterCriminals
    for id in usersId:
        bot.send_message(id, message)
        bot.send_message(id, criminals[iterCriminals % 4])
        nameImage = 'photo' + str(iterCriminals % 4) + '.jpg'
        img = open(nameImage, 'rb')
        bot.send_photo(id, img)
    if iterCriminals == 4:
        iterCriminals = 1
    else:
        iterCriminals += 1



#отправляет сообщение всем пользователям кроме одного
def send_text_to_all_but(message, check_id):
    global iterCriminals
    for id in usersId:
        if id != check_id:
            bot.send_message(id, message)
            bot.send_message(id, criminals[iterCriminals % 4])
            nameImage = 'photo' + str(iterCriminals % 4) + '.jpg'
            img = open(nameImage, 'rb')
            bot.send_photo(id, img)
    if iterCriminals == 4:
        iterCriminals = 1
    else:
        iterCriminals += 1



#ответ на команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    add_id(message.chat.id)



#ответ на команду /stop
@bot.message_handler(commands=['stop'])
def stop_message(message):
    del_id(message.chat.id)



#ответ на текст
@bot.message_handler(content_types=['text'])
def send_text_who(message):

    if message.text == 'Преступник!!!':
        bot.send_message(message.chat.id, 'Где ты его видел?', reply_markup=keyboard_cameras_location)
        composingMessages[message.chat.id] = 'Внимание! Замечен преступник по адресу '
    elif message.text == 'Простой человек':
        bot.send_message(message.chat.id, 'Не волнуйся, все в порядке')



    elif message.text == camerasLocation[0]:
        bot.send_message(message.chat.id, 'У какого входа ты его видел?', reply_markup=keyboard_cameras_location_0)
        composingMessages[message.chat.id] = composingMessages[message.chat.id] + camerasLocation[0]
    elif message.text == camerasLocation[1]:
        bot.send_message(message.chat.id, 'У какого входа ты его видел?', reply_markup=keyboard_cameras_location_1)
        composingMessages[message.chat.id] = composingMessages[message.chat.id] + camerasLocation[1]
    elif message.text == camerasLocation[2]:
        bot.send_message(message.chat.id, 'У какого входа ты его видел?', reply_markup=keyboard_cameras_location_2)
        composingMessages[message.chat.id] = composingMessages[message.chat.id] + camerasLocation[2]
    elif message.text == camerasLocation[3]:
        bot.send_message(message.chat.id, 'У какого входа ты его видел?', reply_markup=keyboard_cameras_location_3)
        composingMessages[message.chat.id] = composingMessages[message.chat.id] + camerasLocation[3]
    elif message.text == camerasLocation[4]:
        bot.send_message(message.chat.id, 'У какого входа ты его видел?', reply_markup=keyboard_cameras_location_4)
        composingMessages[message.chat.id] = composingMessages[message.chat.id] + camerasLocation[4]
    elif message.text == camerasLocation[5]:
        bot.send_message(message.chat.id, 'У какого входа ты его видел?', reply_markup=keyboard_cameras_location_5)
        composingMessages[message.chat.id] = composingMessages[message.chat.id] + camerasLocation[5]
    elif message.text == camerasLocation[len(camerasLocation) - 1]:
        bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
        del composingMessages[message.chat.id]



    elif composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + camerasLocation[0]:
        if message.text == cameras_location_0[0]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_0[0]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_0[1]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_0[1]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_0[2]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_0[2]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_0[3]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_0[3]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_0[4]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не известна'
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_0[5]:
            bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
            del composingMessages[message.chat.id]
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')


    elif composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + camerasLocation[1]:
        if message.text == cameras_location_1[0]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_1[0]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_1[1]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_1[1]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_1[2]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_1[2]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_1[3]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не известна'
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_1[4]:
            bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
            del composingMessages[message.chat.id]
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')


    elif composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + camerasLocation[2]:
        if message.text == cameras_location_2[0]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_2[0]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_2[1]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_2[1]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_2[2]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_2[2]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_2[3]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не известна'
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_2[4]:
            bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
            del composingMessages[message.chat.id]
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')


    elif composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + camerasLocation[3]:
        if message.text == cameras_location_3[0]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_3[0]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_3[1]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_3[1]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_3[2]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не известна'
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_3[3]:
            bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
            del composingMessages[message.chat.id]
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')


    elif composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + camerasLocation[4]:
        if message.text == cameras_location_4[0]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_4[0]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_4[1]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_4[1]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_4[2]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_4[2]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_4[3]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не известна'
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_4[4]:
            bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
            del composingMessages[message.chat.id]
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')


    elif composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + camerasLocation[5]:
        if message.text == cameras_location_5[0]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_5[0]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_5[1]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location_5[1]
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_5[2]:
            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не известна'
            send_text_to_all(composingMessages[message.chat.id])
            del composingMessages[message.chat.id]
        elif message.text == cameras_location_5[3]:
            bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
            del composingMessages[message.chat.id]
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')




    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')




# ---------------------- клавиатуры ----------------------


# эта функция вызывает клавиатуру
keyboard_terror = telebot.types.ReplyKeyboardMarkup()
# эта функция добавляет кнопки в ряд
keyboard_terror.row('Преступник!!!')
keyboard_terror.row('Простой человек')



keyboard_cameras_location = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location.row(camerasLocation[0], camerasLocation[1])
keyboard_cameras_location.row(camerasLocation[2])
keyboard_cameras_location.row(camerasLocation[3])
keyboard_cameras_location.row(camerasLocation[4], camerasLocation[5])
keyboard_cameras_location.row(camerasLocation[len(camerasLocation) - 1])



keyboard_cameras_location_0 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_0.row(cameras_location_0[0])
keyboard_cameras_location_0.row(cameras_location_0[1], cameras_location_0[2], cameras_location_0[3])
keyboard_cameras_location_0.row(cameras_location_0[4])
keyboard_cameras_location_0.row(cameras_location_0[5])


keyboard_cameras_location_1 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_1.row(cameras_location_1[0])
keyboard_cameras_location_1.row(cameras_location_1[1], cameras_location_1[2])
keyboard_cameras_location_1.row(cameras_location_1[3])
keyboard_cameras_location_1.row(cameras_location_1[4])


keyboard_cameras_location_2 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_2.row(cameras_location_2[0])
keyboard_cameras_location_2.row(cameras_location_2[1])
keyboard_cameras_location_2.row(cameras_location_2[2])
keyboard_cameras_location_2.row(cameras_location_2[3])
keyboard_cameras_location_2.row(cameras_location_1[4])


keyboard_cameras_location_3 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_3.row(cameras_location_3[0])
keyboard_cameras_location_3.row(cameras_location_3[1])
keyboard_cameras_location_3.row(cameras_location_3[2])
keyboard_cameras_location_3.row(cameras_location_1[3])


keyboard_cameras_location_4 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_4.row(cameras_location_4[0])
keyboard_cameras_location_4.row(cameras_location_4[1])
keyboard_cameras_location_4.row(cameras_location_4[2])
keyboard_cameras_location_4.row(cameras_location_4[3])
keyboard_cameras_location_4.row(cameras_location_1[4])


keyboard_cameras_location_5 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_5.row(cameras_location_5[0])
keyboard_cameras_location_5.row(cameras_location_5[1])
keyboard_cameras_location_5.row(cameras_location_5[2])
keyboard_cameras_location_5.row(cameras_location_5[3])






#interval - показывает раз во сколько секунд бот будет проверять пришли ли ему сообщения (?)
bot.polling(none_stop=True, interval=0)


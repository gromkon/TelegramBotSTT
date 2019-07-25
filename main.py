import telebot

# имя бота
# @testcrtgrombot

# bot - переменная, с помощью которой можно обращаться к боту
bot = telebot.TeleBot('928505119:AAEvgM9FJnuItQ7gxNwYryLYjmyB2O15-ng')

# список пользователей
usersId = []

# список мест
addresses = ['Ашан Ивантеевская ул. 25А', 'Ашан Бойцовская ул. 2к30', 'ТРК Атриум', 'Метро Бауманская',
             'МГТУ им. Баумана ГЗ', 'МГТУ им. Баумана УЛК', 'Назад']
# список камер
cameras_location_0 = ['у главного входа', 'у входа № 1', 'у входа № 2', 'у входа № 3', 'я не знаю', 'назад']
cameras_location_1 = ['у главного входа', 'у входа № 1', 'у входа № 2', 'я не знаю', 'назад']
cameras_location_2 = ['у главного входа', 'у входа cо стороны вокзала', 'у дополнительного входа', 'я не знаю', 'назад']
cameras_location_3 = ['у входа в метро', 'у выхода из метро', 'я не знаю', 'назад']
cameras_location_4 = ['у входа с Яузы', 'у входа с главного КПП', 'у входа с дополнительного КПП', 'я не знаю', 'назад']
cameras_location_5 = ['у входа с Яузы', 'у главного входа', 'я не знаю', 'назад']

cameras_location = [cameras_location_0, cameras_location_1, cameras_location_2, cameras_location_3, cameras_location_4,
                    cameras_location_5]

# словарь составления сообщений
composingMessages = {}

# словарь количества ошибок
errorMessages = {}

# текущий номер преступника
iterCriminals = 1
# список преступников
criminals = {1: 'Иванов Иван Иванович, дата рождения 12.03.1957, преступник',
             2: 'Синичкин Василий Андреевич , дата рождения 07.12.1985, преступник',
             3: 'Уткин Дмитрий Сергеевич, дата рождения 27.08.1991, хулиган',
             4: 'Курнешова Мария Викторовна, дата рождения 20.09.1970, преступница'}

# ---------------------- клавиатуры ----------------------


# эта функция вызывает клавиатуру
keyboard_terror = telebot.types.ReplyKeyboardMarkup()
# эта функция добавляет кнопки в ряд
keyboard_terror.row('Преступник!!!')
keyboard_terror.row('Простой человек')

keyboard_cameras_location = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location.row(addresses[0], addresses[1])
keyboard_cameras_location.row(addresses[2])
keyboard_cameras_location.row(addresses[3])
keyboard_cameras_location.row(addresses[4], addresses[5])
keyboard_cameras_location.row(addresses[len(addresses) - 1])

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
keyboard_cameras_location_2.row(cameras_location_2[4])

keyboard_cameras_location_3 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_3.row(cameras_location_3[0])
keyboard_cameras_location_3.row(cameras_location_3[1])
keyboard_cameras_location_3.row(cameras_location_3[2])
keyboard_cameras_location_3.row(cameras_location_3[3])

keyboard_cameras_location_4 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_4.row(cameras_location_4[0])
keyboard_cameras_location_4.row(cameras_location_4[1])
keyboard_cameras_location_4.row(cameras_location_4[2])
keyboard_cameras_location_4.row(cameras_location_4[3])
keyboard_cameras_location_4.row(cameras_location_4[4])

keyboard_cameras_location_5 = telebot.types.ReplyKeyboardMarkup()
keyboard_cameras_location_5.row(cameras_location_5[0])
keyboard_cameras_location_5.row(cameras_location_5[1])
keyboard_cameras_location_5.row(cameras_location_5[2])
keyboard_cameras_location_5.row(cameras_location_5[3])

# массив клавиатур размещения камер (адрес)
keyboard_cameras_location_mas = [keyboard_cameras_location_0, keyboard_cameras_location_1,
                                 keyboard_cameras_location_2, keyboard_cameras_location_3,
                                 keyboard_cameras_location_4, keyboard_cameras_location_5]


# добавления пользователя в список пользователей
def add_id(check_id):
    if check_id in usersId:
        bot.send_message(check_id, 'Ты уже подписан на мои уведомления')
    else:
        bot.send_message(check_id, 'Привет, я бот для отслеживания преступников. Если кого-то увидишь, пиши!', reply_markup=keyboard_terror)
        usersId.append(check_id)


# удаления пользователя из списка пользователей
def del_id(check_id):
    try:
        usersId.remove(check_id)
        bot.send_message(check_id, 'Я больше не буду тебя беспокоить, если захочешь подписаться на мою рассылку, введи /start')
    except:
        bot.send_message(check_id, 'Ты не подписан на мои уведомления')


# отправляет сообщение всем пользователям
def send_text_to_all(message):
    global iterCriminals
    for id in usersId:
        nameImage = 'photo' + str(iterCriminals) + '.jpg'
        img = open(nameImage, 'rb')
        bot.send_photo(id, img)
        bot.send_message(id, message)
        bot.send_message(id, criminals[iterCriminals])
    if iterCriminals == 4:
        iterCriminals = 1
    else:
        iterCriminals += 1


# отправляет сообщение всем пользователям кроме одного
def send_text_to_all_but(message, check_id):
    global iterCriminals
    for id in usersId:
        if id != check_id:
            nameImage = 'photo' + str(iterCriminals) + '.jpg'
            img = open(nameImage, 'rb')
            bot.send_photo(id, img)
            bot.send_message(id, message)
            bot.send_message(id, criminals[iterCriminals])
    if iterCriminals == 4:
        iterCriminals = 1
    else:
        iterCriminals += 1



# удаление пользователя из списка количества ошибок
def del_errorMessages(check_id):
    flag_del = 0
    for id in errorMessages:
        if check_id == id:
            flag_del = 1
            break
    if flag_del == 1:
        del errorMessages[check_id]



# проверка пользователя на наличие в списке количества ошибок
def check_in_errorMessages(check_id):
    flag_err = 0
    for errMes in errorMessages:
        if errMes == check_id:
            flag_err = 1
            break
    return flag_err



# ответ на команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    add_id(message.chat.id)


# ответ на команду /stop
@bot.message_handler(commands=['stop'])
def stop_message(message):
    del_id(message.chat.id)


# ответ на текст
@bot.message_handler(content_types=['text'])
def send_text_who(message):
    print(composingMessages)
    flagUnderstend = 0

    delList = []

    flag_del = 0

    for chat_id in composingMessages:
        if message.chat.id == chat_id:
            for addressesNum in range(len(addresses) - 1):
                if composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + str(addresses[addressesNum]):
                    len_cameras_location = len(cameras_location[addressesNum])
                    for cameras_num in range(len_cameras_location):
                        if message.text == cameras_location[addressesNum][len(cameras_location[addressesNum]) - 2]:
                            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
                            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не указана'
                            send_text_to_all(composingMessages[message.chat.id])
                            flagUnderstend = 1
                            flag_del = 1
                            break
                        elif message.text == cameras_location[addressesNum][len(cameras_location[addressesNum]) - 1]:
                            bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
                            flagUnderstend = 1
                            flag_del = 1
                            break
                        elif message.text == cameras_location[addressesNum][cameras_num]:
                            bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
                            composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера ' + cameras_location[addressesNum][cameras_num]
                            send_text_to_all(composingMessages[message.chat.id])
                            flagUnderstend = 1
                            flag_del = 1
                            break
        if flag_del == 1:
            del composingMessages[message.chat.id]
        break

    flag_del = 0

    for chat_id in composingMessages:
        if message.chat.id == chat_id:
            for mesNum in range(len(addresses)):
                if message.text == addresses[len(addresses) - 1]:
                    bot.send_message(message.chat.id, 'Возвращаю в главное меню', reply_markup=keyboard_terror)
                    flag_del = 1
                    flagUnderstend = 1
                    break
                elif message.text == addresses[mesNum]:
                    bot.send_message(message.chat.id, 'У какого входа ты его видел?', reply_markup=keyboard_cameras_location_mas[mesNum])
                    composingMessages[message.chat.id] = composingMessages[message.chat.id] + addresses[mesNum]
                    flagUnderstend = 1
                    break

        if flag_del == 1:
            del composingMessages[message.chat.id]
        break


    if message.text == 'Преступник!!!':
        flagUnderstend = 1
        bot.send_message(message.chat.id, 'Где ты его видел?', reply_markup=keyboard_cameras_location)
        composingMessages[message.chat.id] = 'Внимание! Замечен преступник по адресу '
    elif message.text == 'Простой человек':
        flagUnderstend = 1
        bot.send_message(message.chat.id, 'Не волнуйся, все в порядке')


    if flagUnderstend == 0:
        if check_in_errorMessages(message.chat.id) == 0:
            errorMessages[message.chat.id] = 1
        else:
            errorMessages[message.chat.id] += 1

        if errorMessages[message.chat.id] >= 3:
            bot.send_message(message.chat.id, 'Кажется что-то пошло не так, попробуй заново, возвращаю в главное меню', reply_markup=keyboard_terror)
            del_errorMessages(message.chat.id)
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй воспользоваться меню')
    else:
        del_errorMessages(message.chat.id)


# interval - показывает раз во сколько секунд бот будет проверять пришли ли ему сообщения (?)
bot.polling(none_stop=True, interval=0)

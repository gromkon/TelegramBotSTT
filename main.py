import telebot
from bot_token import *
import glob, os
from datetime import datetime
import random

# имя бота
# @testcrtgrombot

# bot - переменная, с помощью которой можно обращаться к боту
bot = telebot.TeleBot(bot_token)

# список пользователей
usersId = []

# список мест
addresses = ['Ашан Ивантеевская ул. 25А', 'Ашан Бойцовская ул. 2к30', 'ТРК Атриум',
             'Метро Бауманская', 'МГТУ им. Баумана ГЗ', 'МГТУ им. Баумана УЛК', 'Назад']
# список камер
cameras_location_0 = ['у главного входа', 'у входа № 1', 'у входа № 2', 'у входа № 3', 'я не знаю', 'назад']
cameras_location_1 = ['у главного входа', 'у входа № 1', 'у входа № 2', 'я не знаю', 'назад']
cameras_location_2 = ['у главного входа', 'у входа cо стороны вокзала', 'у дополнительного входа', 'я не знаю', 'назад']
cameras_location_3 = ['у входа в метро', 'у выхода из метро', 'я не знаю', 'назад']
cameras_location_4 = ['у входа с Яузы', 'у входа с главного КПП', 'у входа с дополнительного КПП', 'я не знаю', 'назад']
cameras_location_5 = ['у входа с Яузы', 'у главного входа', 'я не знаю', 'назад']

cameras_location = [cameras_location_0, cameras_location_1, cameras_location_2,
                    cameras_location_3, cameras_location_4, cameras_location_5]

# словарь составления сообщений
composingMessages = {}

# словарь количества ошибок
errorMessages = {}

# словарь может ли человек писать
canWriteMessages = {}

# словарь, прислал ли человек фото
photoMessages = {}

# словарь, в котором написан путь до фотографии загруженной пользователем
pathPhotoMessages = {}

# словарь, в котором указаны проценты совпадения с фотографиями
procentPhotoMessages = {}


# список преступников
criminals = {0: 'Иванов Иван Иванович, дата рождения 12.03.1957, преступник',
             1: 'Синичкин Василий Андреевич , дата рождения 07.12.1985, преступник',
             2: 'Уткин Дмитрий Сергеевич, дата рождения 27.08.1991, хулиган',
             3: 'Курнешова Мария Викторовна, дата рождения 20.09.1970, преступница',
             4: 'Гусев Андрей Александрович, дата рождения 08.05.1993, хулиган',
             5: 'Оглы Алан Ашотович, дата рождения 13.09.1996, вор',
             6: 'Федотов Андрей Михайлов, дата рождения 29.12.1975, преступник',
             7: 'Жукова Ирина Николаевна, дата рождения 27.01.1980, хулиганка',
             8: 'Курнешова Наталья Кирилловна, дата рождения 01.02.1995, вор',
             9: 'Зубенко Михаил Петрович, дата рождения 09.02.1973, преступник'}

# ---------------------- клавиатуры ----------------------


# эта функция вызывает клавиатуру
keyboard_terror = telebot.types.ReplyKeyboardMarkup()
# эта функция добавляет кнопки в ряд
keyboard_terror.row('Преступник!!!')
keyboard_terror.row('Простой человек')

keyboard_empty = telebot.types.ReplyKeyboardMarkup()

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


# список фотографий
photos = []

# получение списка фотографий из "БД"
cwd = os.getcwd()
for file in glob.glob('*.jpg'):
    photos.append(cwd + '/' + file)


# добавления пользователя в список пользователей
def add_id(check_id):
    if check_id in usersId:
        bot.send_message(check_id, 'Ты уже подписан на мои уведомления')
    else:
        bot.send_message(check_id, 'Привет, я бот для отслеживания преступников. Если кого-то увидишь, пиши!', reply_markup=keyboard_terror)
        usersId.append(check_id)
        canWriteMessages[check_id] = 1


# удаления пользователя из списка пользователей
def del_id(check_id):
    try:
        usersId.remove(check_id)
        bot.send_message(check_id, 'Я больше не буду тебя беспокоить, если захочешь подписаться на мою рассылку, введи /start')
    except:
        bot.send_message(check_id, 'Ты не подписан на мои уведомления')


# отправляет сообщение всем пользователям
def send_text_to_all(message, chat_id):
    canWriteMessages[chat_id] = 0

    for id in usersId:

        print(procentPhotoMessages[chat_id])

        key1 = int(str(procentPhotoMessages[chat_id][0])[1:str(procentPhotoMessages[chat_id][0]).find(',')])
        value1 = str(procentPhotoMessages[chat_id][0])[str(procentPhotoMessages[chat_id][0]).find(',') + 2:len(str(procentPhotoMessages[chat_id][0])) - 1]

        key2 = int(str(procentPhotoMessages[chat_id][1])[1:str(procentPhotoMessages[chat_id][1]).find(',')])
        value2 = str(procentPhotoMessages[chat_id][1])[str(procentPhotoMessages[chat_id][1]).find(',') + 2:len(str(procentPhotoMessages[chat_id][1])) - 1]

        key3 = int(str(procentPhotoMessages[chat_id][2])[1:str(procentPhotoMessages[chat_id][2]).find(',')])
        value3 = str(procentPhotoMessages[chat_id][2])[str(procentPhotoMessages[chat_id][2]).find(',') + 2:len(str(procentPhotoMessages[chat_id][2])) - 1]

        nameImage1 = photos[key1]
        nameImage2 = photos[key2]
        nameImage3 = photos[key3]

        img_criminal_bd1 = open(nameImage1, 'rb')
        img_criminal_bd2 = open(nameImage2, 'rb')
        img_criminal_bd3 = open(nameImage3, 'rb')

        img_criminal_user = open(pathPhotoMessages[chat_id], 'rb')

        bot.send_message(id, message)
        bot.send_message(id, 'Фото с камеры')
        bot.send_photo(id, img_criminal_user)

        bot.send_message(id, 'Предполагаемые преступники:')

        bot.send_photo(id, img_criminal_bd1)
        bot.send_message(id, 'Cовпадение ' + value1 + '%')
        bot.send_message(id, criminals[key1])

        bot.send_photo(id, img_criminal_bd2)
        bot.send_message(id, 'Cовпадение ' + value2 + '%')
        bot.send_message(id, criminals[key2])

        bot.send_photo(id, img_criminal_bd3)
        bot.send_message(id, 'Cовпадение ' + value3 + '%')
        bot.send_message(id, criminals[key3])

    canWriteMessages[chat_id] = 1



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


# проверка пользователя на наличие в списке составления сообщений
def check_in_composingMessages(check_id):
    flag = 0
    for composingMessage in composingMessages:
        if composingMessage == check_id:
            flag = 1
            break
    return flag

# проверка пользователя на наличие в списке составления сообщений
def check_in_photoMessages(check_id):
    flag = 0
    for photoMessage in photoMessages:
        if photoMessage == check_id:
            flag = 1
            break
    return flag

# проверка пользователя на наличие в списке количества ошибок
def check_in_canWriteMessages(check_id):
    flag_err = 0
    for canWriteMessage in canWriteMessages:
        if canWriteMessage == check_id:
            flag_err = 1
            break
    return flag_err


# проверка пользователя на наличие в списке путей присланных фотографий
def check_in_pathPhotoMessages(check_id):
    flag = 0
    for pathPhotoMessage in pathPhotoMessages:
        if pathPhotoMessage == check_id:
            flag = 1
            break
    return flag

# проверка наличия сравнения фотографии пользователя с "БД"
def check_in_procentPhotoMessages(check_id):
    flag = 0
    for procentPhotoMessage in procentPhotoMessages:
        if procentPhotoMessage == check_id:
            flag = 1
            break
    return flag



# проверка двух фотографий
def compare_photos(src1, src2):
    return round(random.random() * 100, 2)


# проверка фотографии по "БД"
def check_photo_in_database(src, id):
    comparsion_percentages = {}
    for i in range(len(photos)):
        comparsion_percentages[i] = compare_photos(src, photos[i])
    comparsion_percentages = sorted(comparsion_percentages.items(), key=lambda kv: kv[1])

    #3 совпадения с наибольшими значениями
    top_three_coincidence = []
    for i in range(3):
        top_three_coincidence.append(comparsion_percentages[len(comparsion_percentages) - i - 1])

    procentPhotoMessages[id] = top_three_coincidence


# ответ на команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    add_id(message.chat.id)


# ответ на команду /stop
@bot.message_handler(commands=['stop'])
def stop_message(message):
    del_id(message.chat.id)

# ответ на команду /changefoto
@bot.message_handler(commands=['changefoto'])
def change_foto(message):
    if check_in_pathPhotoMessages(message.chat.id) == 1:
        del pathPhotoMessages[message.chat.id]
    if check_in_photoMessages(message.chat.id) == 1:
        del photoMessages[message.chat.id]

    composingMessages[message.chat.id] = 'Внимание! Замечен преступник по адресу '

    bot.send_message(message.chat.id, 'Пришли новое фото!', reply_markup=keyboard_terror)

# ответ на текст
@bot.message_handler(content_types=['text'])
def send_text_who(message):

    if check_in_canWriteMessages(message.chat.id) == 1:
        if canWriteMessages[message.chat.id] == 1:
            flagUnderstend = 0

            flag_del = 0

            for chat_id in composingMessages:
                if message.chat.id == chat_id:
                    # 3 меню
                    for addressesNum in range(len(addresses) - 1):
                        if composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ' + str(addresses[addressesNum]):
                            len_cameras_location = len(cameras_location[addressesNum])
                            for cameras_num in range(len_cameras_location):
                                if message.text == cameras_location[addressesNum][len(cameras_location[addressesNum]) - 2]:
                                    bot.send_message(message.chat.id, 'Мы проверим информацию, спасибо!', reply_markup=keyboard_terror)
                                    composingMessages[message.chat.id] = composingMessages[message.chat.id] + ', камера не указана'
                                    send_text_to_all(composingMessages[message.chat.id], message.chat.id)
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
                                    send_text_to_all(composingMessages[message.chat.id], message.chat.id)
                                    flagUnderstend = 1
                                    flag_del = 1
                                    break

                    # 2 меню
                    if check_in_photoMessages(message.chat.id) == 1:
                        if photoMessages[message.chat.id] == 1:
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
                    else:
                        flagUnderstend = 1
                        bot.send_message(message.chat.id, 'Сначала пришли фото')

                if flag_del == 1:
                    if check_in_composingMessages(message.chat.id) == 1:
                        del composingMessages[message.chat.id]
                    if check_in_photoMessages(message.chat.id) == 1:
                        del photoMessages[message.chat.id]
                    if check_in_pathPhotoMessages(message.chat.id) == 1:
                        del pathPhotoMessages[message.chat.id]
                    if check_in_procentPhotoMessages(message.chat.id) == 1:
                        del procentPhotoMessages[message.chat.id]
                break

            # 1 меню
            if message.text == 'Преступник!!!':
                flagUnderstend = 1
                bot.send_message(message.chat.id, 'Пришли его фото')

                # bot.send_message(message.chat.id, 'Где ты его видел?', reply_markup=keyboard_cameras_location)
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
        else:
            bot.send_message(message.chat.id, 'Подожди, я обрабатываю Твой предыдущий запрос')
    else:
        bot.send_message(message.chat.id, 'Введи /start')






# ответ на фото
@bot.message_handler(content_types=['photo'])
def send_image_who(message):
    if check_in_composingMessages(message.chat.id) == 1:
        if check_in_photoMessages(message.chat.id) == 1:
            bot.send_message(message.chat.id, 'Если хочешь заменить фото напиши /changefoto')
        elif composingMessages[message.chat.id] == 'Внимание! Замечен преступник по адресу ':

            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            time_now = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
            src = cwd + '/download_photos/' + 'photo' + str(message.chat.id) + str(time_now) + '.jpg'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)

            photoMessages[message.chat.id] = 1
            pathPhotoMessages[message.chat.id] = src

            check_photo_in_database(src, message.chat.id)

            bot.send_message(message.chat.id, 'Где ты его видел?', reply_markup=keyboard_cameras_location)

    else:
        bot.send_message(message.chat.id, 'Если ты хочешь прислать мне фото преступника, сначала напиши "Преступник!!!"')






# interval - показывает раз во сколько секунд бот будет проверять пришли ли ему сообщения (?)
bot.polling(none_stop=True, interval=0)

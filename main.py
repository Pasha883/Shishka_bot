import telebot
import time
import random

#ID администраторов бота в ТГ
a = 0
b = 0
c = 0
e = 0

d = 1

dz = str("В данный момент дз не установлено")

chat_ID = 0

link = 1






# Создаем объект бота и токен
bot = telebot.TeleBot('Токен')



# Словарь для хранения статистики чата
stats = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Версия 3.00.0 - последнее обновление бота, поддержка бота завершится в 2024 году (Сразу после выхода APOLLO BOT). Нужна помощь? Пиши /help")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/dz - получить дз\n/dz_config -зменить дз\n/rules - правила\n/meme - мем\n/pin - закрепить сообщение\n/unpin - открепить сообщение\n/del - удалить сообщение\n/kick - кикнуть пользователя\n/mute - замутить пользователя на определенное время\n/unmute - размутить пользователя\n/stats - показать статистику чата\n/selfstat - показать свою статистику\n/future - узнать о планах развития\n/QTE - ответы на вопросы\n/about - информация\n/BanWords - список запрещённых слов\n/WhatsNew - список изменений в новой версии\n/Purchases - магазин\n/Buy - купить что-то из магазина\n/music1 - мелодия 1\n/music2 - мелодия 2\n/music3 - мелодия 3")

@bot.message_handler(commands=['future'])
def future(message):
    bot.reply_to(message, "Поддержака бота завершается в 2024 году")

@bot.message_handler(commands=['WhatsNew'])
def WN(message):
    bot.reply_to(message, "Текущая версия: 3.00.0\nВерсия с которой произошло обнавление 2.79.9\nНововведения: добавлена команда /dz")

@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, "Имя: ШишкаБот\nВерсия: 3.00.0\nРазработчик: PashaCO.ru")

@bot.message_handler(commands=['Buy'])
def buy(message):
    bot.reply_to(message, "Битки кидать сюда - 15bQ91RBgE36N34Kwx1j22i3XpZo2CWTcs")

@bot.message_handler(commands=['rules'])
def rules(message):
    bot.reply_to(message, "Читы - бан. Кэмперство - бан. Оскорбления - бан. Оскорбления администрации - расстрел, потом бан.")

@bot.message_handler(commands=['Purchases'])
def Shop(message):
    bot.reply_to(message, "Админка в боте - 52 биткоина")


@bot.message_handler(commands=['dz_config'])
def DzConfig(message):
    if message.from_user.id == a or message.from_user.id == b or message.from_user.id == c:
        global dz
        dz = str(message.text)
        bot.reply_to(message, 'Дз сохранено' )
    else:
        bot.reply_to(message, 'Если вы также присылаете ДЗ, напишите Маше, и она скажет мне добавить вас в группу людей, что может отправлять ДЗ' )

@bot.message_handler(commands=['dz'])
def Dz(message):
    bot.reply_to(message, dz)


@bot.message_handler(commands=['BanWords'])
def BanWords(message):

    bot.reply_to(message, 'Бан ворды упразднены, их больше нет, но не забывайте, они могут появиться в любой момент, так что не шалите!' )



#@bot.message_handler(commands=['meme'])
#def meme(message):
#    num = random.randint(1, 185)
#    tex = random.randint(1, 14)



@bot.message_handler(commands=['QTE'])
def QTE(message):
    bot.reply_to(message, "Почему шишка бот? Сами догадайтесь\nПочему такая ава? Аватарка была сгенерирована нейросетью\nПочему я сделал этого бота? Заняться мне было нечем, вот и решил, что надо сделать бота, всё равно на питоне давно не кодил, а тут новая беседа, так ещё и стандартные боты не робят\nМожно ли добавлять этого бота в другие беседы? Да конечно можно, мне насрать, вроде все команды были оптимизированы под работу в любой беседе")

@bot.message_handler(commands=['алгоритм_в_последний_путь'])
def lastway(message):
    bot.reply_to(message, "Для активации алгоритма в последний путь ещё нет везких причин. Данное суждение бяло сформулировано на основе анализа последних пятиста сообщений. Если это не так, введите идентификатор активации.")



@bot.message_handler(commands=['modules_link_on'])
def goodbue(message):

 if message.from_user.id == a:
     bot.send_message(-1001627205786, "Ссылки включены")
     global link
     link = 1
 else:
     bot.send_message(-1001627205786, "У ВАС НЕТ ПРАВ")

@bot.message_handler(commands=['modules_link_off'])
def goodbue(message):

 if message.from_user.id == a:
     bot.send_message(-1001627205786, "Ссылки отключены")
     global link
     link = 0
 else:
     bot.send_message(-1001627205786, "У ВАС НЕТ ПРАВ")

# Обработчик команды /kick
@bot.message_handler(commands=['kick'])
def kick_user(message):


 if message.from_user.id == a or message.from_user.id == b or message.from_user.id == c:

    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно кикнуть администратора.")
        elif user_id == a:
            bot.reply_to(message, "Я не кикну своего создателя! >:(")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был кикнут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")
 else:

     bot.reply_to(message, "Только отдельный круг лиц может сделать это")


@bot.message_handler(commands=['del'])
def deli(message):


 if message.from_user.id == a or message.from_user.id == b or message.from_user.id == c or message.from_user.id == e:

    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status



       # bot.pin_chat_message(chat_id, message_id)
        bot.delete_message(message.chat.id, message_id)
        bot.send_message(-1001627205786, "Сообщение удалено")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение, которое вы хотите закрепить.")
 else:

     bot.reply_to(message, "Только отдельный круг лиц может сделать это")

@bot.message_handler(commands=['pin'])
def pin(message):


 if message.from_user.id == a or message.from_user.id == b or message.from_user.id == c or message.from_user.id == e:

    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status



        bot.pin_chat_message(chat_id, message_id)
        bot.reply_to(message.reply_to_message, "Сообщение закреплено.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение, которое вы хотите закрепить.")
 else:

     bot.reply_to(message, "Только отдельный круг лиц может сделать это")


@bot.message_handler(commands=['unpin'])
def unpin(message):


 if message.from_user.id == a or message.from_user.id == b or message.from_user.id == c or message.from_user.id == e:

    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        bot.unpin_chat_message(chat_id, message_id)
        bot.reply_to(message.reply_to_message, "Сообщение откреплено.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение, которое вы хотите открепить.")
 else:

     bot.reply_to(message, "Только отдельный круг лиц может сделать это")


# Обработчик команды /mute
@bot.message_handler(commands=['mute'])
def mute_user(message):

 if message.from_user.id == a or message.from_user.id == b or message.from_user.id == c or message.from_user.id == e:

    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить администратора.")
        elif user_id == a:
            bot.reply_to(message, "Вы не заставите моего создателя молчать! >:(")
        else:
            duration = 1 # Значение по умолчанию - 1 минута
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день.")
                    return
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time()+duration*60)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")

 else:

     bot.reply_to(message, "Только отдельный круг лиц может сделать это")

# Обработчик команды /unmute
@bot.message_handler(commands=['unmute'])
def unmute_user(message):

 if message.from_user.id == a :

    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размучен.")
    elif user_id == a:
            bot.reply_to(message, "Мой создатель всегда говорит, что думает! >:(")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")

 else:

   bot.reply_to(message, "У ВАС НЕТ ПРАВ")


# Обработчик команды /stats
@bot.message_handler(commands=['stats'])
def chat_stats(message):
    chat_id = -1001627205786
    if chat_id not in stats:
        bot.reply_to(message, "Статистика чата пуста.")
    else:
        total_messages = stats[chat_id]['total_messages']
        unique_users = len(stats[chat_id]['users'])
        bot.reply_to(message, f"Статистика чата:\nВсего сообщений: {total_messages}\nУникальных пользователей: {unique_users}")

# Обработчик команды /selfstat
@bot.message_handler(commands=['selfstat'])
def user_stats(message):
    chat_id = -1001627205786
    user_id = message.from_user.id
    username = message.from_user.username
    if chat_id not in stats:
        bot.reply_to(message, "Статистика чата пуста.")
    else:
        if user_id not in stats[chat_id]['users']:
            bot.reply_to(message, "Вы еще не отправляли сообщений в этом чате.")
        else:
            user_messages = stats[chat_id]['users'][user_id]['messages']
            total_messages = stats[chat_id]['total_messages']
            percentage = round(user_messages / total_messages * 100, 2)
            bot.reply_to(message, f"Статистика для пользователя @{username}:\nВсего сообщений: {user_messages}\nПроцент от общего количества сообщений: {percentage}%")





@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == chat_ID)
def delete_links(message):
    for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
        # url - обычная ссылка, text_link - ссылка, скрытая под текстом
        if entity.type in ["url", "text_link"] and link == 0:
            # Мы можем не проверять chat.id, он проверяется ещё в хэндлере

         bot.delete_message(message.chat.id, message.message_id)
        else:
           return

bad_words = [ ]

mat = ['блин', 'гей', 'амогус', 'блять', 'бля', 'сука', 'суkа' , 'пенис', 'хуй', 'залупа', 'еблан', 'ебанат', 'пидор', 'ебанутый', 'ебать', 'соси' , 'пиздак', 'пидорасик', 'мудак' , 'ебанат', 'уебан', 'хуя', 'пососите' , 'хуйня', 'нахуй', 'уебан', 'хуесос', 'пиздец', 'пизда', 'пиз', 'хае', 'ебаный' , 'ёбаный', 'ебанный', 'ёбанный', 'распизделся', 'член', 'членосос']

# функция для проверки наличия запрещенных слов в сообщении
def check_message(message):
    for word in bad_words:
        if word in message.text.lower():
            return True
    return False

def check_message1(message):
    for word in mat:
        if word in message.text.lower():
            return True
    return False


# обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # проверяем сообщение на наличие запрещенных слов
 if check_message(message):
        # если есть хотя бы одно запрещенное слово, кикаем пользователя
        # bot.kick_chat_member(message.chat.id, message.from_user.id)
        if message.from_user.id == a:
            bot.reply_to(message, "Мой создатель не прав, не повторяйте за ним! >:(")
        elif message.from_user.id != a:
         duration = 1
         bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time()+duration*60)
         bot.send_message(message.chat.id, f"Пользователь {message.from_user.username} был замучен на одну минуту за использование запрещенных слов")


    # проверяем сообщение на наличие запрещенных слов
 elif check_message1(message):
        # если есть хотя бы одно запрещенное слово, кикаем пользователя
        # bot.kick_chat_member(message.chat.id, message.from_user.id)
        if message.from_user.id == a:
            bot.reply_to(message, "Мой создатель не прав, не повторяйте за ним! >:(")
        elif message.from_user.id != a:
         duration = 1
         #bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time()+duration*60)
         #bot.send_message(message.chat.id, f"Пользователь {message.from_user.username} был замучен на одну минуту за использование запрещенных слов")
         bot.reply_to(message, "Ну не матерись, нас дети смотрят")
 else:
        # если запрещенных слов нет, обрабатываем сообщение дальше
        print(message.text)




# Запускаем бота
bot.infinity_polling(none_stop=True)



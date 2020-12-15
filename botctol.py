# - *- coding: utf- 8 - *-
import telebot



bot = telebot.TeleBot('1490595332:AAFzZ3LrL8vaBvmxgvlRlqUf8q5UQi1Ve3o')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('GO', 'close')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row("Казахстан", "Россия")
keyboard2.row("Китай", "Узбекистан", "Азербайджан")
keyboard2.row("Армения", "Белорусия", "Молдавия")
keyboard2.row("Таджикистан", "Украина", "Франция")
keyboard2.row("Испания", "Германия", "Италия")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот который дает информацию о стран СНГ и других известных стран, нажми на GO чтобы начать или close чтобы выйти', reply_markup=keyboard1)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'GO':
          bot.reply_to(message,'Выберите страну о которой хотите узнать', reply_markup=keyboard2)
    elif message.text == 'Казахстан':
        bot.reply_to(message,('Столица - Нур-Султан, Население - 18,28 миллиона, Президент- Касым-Жомарт Токаев)'))
    elif message.text == 'Россия':
        bot.reply_to(message, 'Столица - Москва, Президент - Владимир Путин, Население - 144,5 миллиона, Правление: Федеративная республика, Республика, Смешанная республика ')
    elif message.text == 'Китай':
        bot.reply_to(message, 'Президент - Си Цзиньпин, Столица - Пекин, Форма правления - однопартийная парламентская республика, Население - 1,393 миллиарда,')
    elif message.text == 'Киргизия':
        bot.reply_to(message, 'Столица - Бишкек, Форма правления - смешанная республика Население - 6,316 миллиона Президент - Садыр Жапаров ')
    elif message.text == 'Узбекистан':
        bot.reply_to(message, 'Столица - Ташкент Население - 32,96 миллиона Президент - Шавкат Миромонович Мирзиёев Валюта - Узбекский сум')
    elif message.text == 'Азербайджан':
        bot.reply_to(message, 'Президент - Ильхам Алиев Столица - Баку Форма правления - президентская республика ')
    elif message.text == 'Армения':
        bot.reply_to(message, 'Столица - Ереван Площадь - 29 743 км² Население - 2,965 миллиона Президент - Армен Саркисян Форма правления - парламентская республика')
    elif message.text == 'Белорусия':
        bot.reply_to(message, 'Столица - Минск Президент - Александр Лукашенко Население - 9,485 миллиона')
    elif message.text == 'Молдавия':
        bot.reply_to(message, 'Столица - Кишинёв Президент - Игорь Николаевич Додон Население - 3,546 миллиона Форма правления - парламентская республика Правление - Республика, Парламентаризм, Унитарное государство, Парламентская республика')
    elif message.text == 'Таджикистан':
        bot.reply_to(message, 'Столица - Душанбе Форма правления - президентская республика Президент - Эмомали Рахмон Население - 9,101 миллиона')
    elif message.text == 'Украина':
        bot.reply_to(message, 'Столица - Киев Президент - Владимир Зеленский Население - 41,98 миллиона Валюта - Украинская гривна')
    elif message.text == 'close':
        bot.reply_to(message, 'Спасибо что возпользовались до свидания :)')
    elif message.text == 'Франция':
        bot.reply_to(message,'Президент: Эмманюэль Макрон Столица: Париж Население: 66,99 миллиона Форма правления: смешанная демократическая республика')
    elif message.text == 'Испания':
        bot.reply_to(message,
                     'Столица - Мадрид Форма правления - конституционная монархия Население - 46,94 миллиона Правление - Монархия, Парламентаризм, Унитарное государство, Конституционная монархия')
    elif message.text == 'Германия':
        bot.reply_to(message,
                     'Население - 83,02 миллиона Столица - Берлин Президент - Франк-Вальтер Штайнмайер Названия жителей - немец, немка, немцы')
    elif message.text == 'Италия':
        bot.reply_to(message,
                     'Столица - Рим Президент - Серджо Маттарелла Форма правления - парламентская республика Население - 60,36 миллиона')
    elif message.text == 'США':
        bot.reply_to(message,
                     'Столица - Вашингтон Президент - Джо Байден Форма правления - федеративная президентская республика Гос. религия - светское государство')






bot.polling(none_stop=True)
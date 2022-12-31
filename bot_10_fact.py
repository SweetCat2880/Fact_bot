import telebot
import random
import requests
import googletrans
from bs4 import BeautifulSoup as bs
import os

my_dir = os.path.dirname(__file__)

try:
    os.mkdir("plant_pic")
    os.mkdir("book_pic")
    os.mkdir("food_chicken_pic")
except FileExistsError:
    pass

token = '5939083926:AAGUz9g1bb1Z3Y7Sw3hr0iIxhhHidq8KJsA'

# Как написать кому-то по id: bot2.send_message(1722912573, 'Привет')

# https://https://t.me/F_Q_YN_bot

translate = googletrans.Translator()

langua_use = ""
number = 0
u = ''
t = {

}
plant_rub = ""


rub_0 = 0
rub_2 = 0
rub_1 = 0
url_0_d = []
url_0_d_ex = []
url = []
m_r = 0
url_0_d_ex_1 = []
tpo = 0
plant_rub = ''


pred_l = ["As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
          "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
          'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
          'Concentrate and ask again',
          'Don’t count on it', "My reply is no", "Outlook not so good", "Very doubtful", "	My sources say no"]

bot2 = telebot.TeleBot(token)


@bot2.message_handler(commands=["start"])
def start_m(message):
    with open("TestBot_2.txt", "a", encoding="utf-8") as fl:
        print(message.text, file=fl)
        print(message.from_user.id, file=fl)
        print(message.from_user.username, " - username", file=fl)
        print(message.from_user.first_name, " - name", file=fl)

    #bot2.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGjKZjgR2N--dY-mVvPx8YiFSAk9-WRwAC9xMAAga9IEi0_o-JHAGCTCsE")

    bot2.send_message(message.chat.id, f"Привет, {message.from_user.first_name}\n"
                                       f"Введите /help, чтобы получить список команд\n"
                                       f"Код написан на языке программирования python\n"
                                       f"Версия: 1.1\n")

    print(message.from_user.username, " - username")
    print(message.from_user.first_name, " - name")
    print(message.chat.id, " - ID")


@bot2.message_handler(commands=["help"])
def help_m(message):
    bot2.send_message(message.chat.id, "/fact - факт\n"
                                       "/fact_num - факт о числе\n"
                                       "/wisdom - мудрость\n"
                                       "/question - вопрос из викторины\n"
                                       "/prediction - аналог шара предсказаний\n"
                                       "/translate - перевести сообщение\n"
                                       "/food - выдает блюдо\n"
                                       "/book - выдает книгу\n"
                                       "/plant - выдает растение")
    print("help")
    print(message.from_user.first_name, "\n")


@bot2.message_handler(commands=['translate_helper_1'])
# 4 - конечное действие; получает запрос от 2
def repl_k_tr(call, lo):
    bot2.send_message(call.message.chat.id, "Напишите сообщение")

    # Ru - конечный
    if lo > 20:
        bot2.register_next_step_handler(call.message, repl_k_tr_1)

    # En - конечный
    if lo < 20:
        bot2.register_next_step_handler(call.message, repl_k_tr_2)

    # свой язык
    if lo == 20:
        bot2.register_next_step_handler(call.message, repl_k_tr_use_lan)


# 2.0 - ответ(выше) Ru
def repl_k_tr_1(message):
    message_trnslate = message.text
    mes_tr_ed = translate.translate(message_trnslate, dest="ru")
    bot2.send_message(message.chat.id, mes_tr_ed.text)

    print(mes_tr_ed)


# 2.1 - ответ(выше) En
def repl_k_tr_2(message):
    message_trnslate = message.text
    mes_tr_ed = translate.translate(message_trnslate, dest="en")
    bot2.send_message(message.chat.id, mes_tr_ed.text)

    print(mes_tr_ed)


# 2.2.0 - ответ(выше) На свое - какой язык
def repl_k_tr_use_lan(message):
    global langua_use
    langua_use = message.text
    bot2.register_next_step_handler(message, repl_k_tr_use)


# 2.2.1 - продолжение ответа(выше) на свое
def repl_k_tr_use(message):
    global langua_use
    message_trnslate = message.text

    try:
        mes_tr_ed = translate.translate(message_trnslate, dest=langua_use)
        bot2.send_message(message.chat.id, mes_tr_ed.text)
        print(mes_tr_ed)

    except ValueError:
        bot2.send_message(message.chat.id, "Вы ввели несуществующий язык")


# 0 - клавиатура; применяется к 1
def keyboard_jan():
    keyboard_jan_repl = telebot.types.InlineKeyboardMarkup()


    key_ru = telebot.types.InlineKeyboardButton(text="Перевести на русский", callback_data="entoru")
    key_en = telebot.types.InlineKeyboardButton(text="Перевести на английский", callback_data="rutoen")
    key_one = telebot.types.InlineKeyboardButton(text="Свой язык", callback_data="one")
    key_g_list = telebot.types.InlineKeyboardButton(text="Получить список кодов языков", callback_data="code_list")


    keyboard_jan_repl.row(key_ru)
    keyboard_jan_repl.row(key_en)
    keyboard_jan_repl.row(key_one)
    keyboard_jan_repl.row(key_g_list)


    return keyboard_jan_repl


# 1 - кнопка start; отправляет запрос к 0
@bot2.message_handler(commands=["translate"])
def jan_repl(message):
    bot2.send_message(message.chat.id, "Выберите язык", reply_markup=keyboard_jan())

    print("translate")
    print(message.from_user.first_name, "\n")


# 2 - промежуток - что именно вызывать; отправляет запрос к 4; получает data от 0
@bot2.callback_query_handler(func=lambda call: True)
def genre_reply_butt(call):
    if call.data == "entoru":
        bot2.send_message(call.message.chat.id, "Напишите сообщение, которое желаете перевести на русский", reply_markup=repl_k_tr(call, 100))
        print("Конечное - ru")

    if call.data == "rutoen":
        bot2.send_message(call.message.chat.id, "Напишите сообщение, которое желаете перевести на английский", reply_markup=repl_k_tr(call, 10))
        print("Конечное - en")

    if call.data == "one":
        bot2.send_message(call.message.chat.id, "Напишите на какой язык перевести через кодировку 'ISO 639-1'", reply_markup=repl_k_tr(call, 20))
        print("Конечное - x")

    if call.data == "code_list":
        bot2.send_message(call.message.chat.id, "Список кодировки 'ISO 639-1' - https://snipp.ru/handbk/iso-639-1")
        print("list")


@bot2.message_handler(commands=['question'])
def quest_st(message):

    r = requests.get("http://jservice.io/api/random?count=1")

    def quest_repl(message_0):
        global t
        nonlocal r

        for i in r.json():
            t = dict(i)
            print(t)

            pi = (t["question"])
            pi_tr = translate.translate(pi, dest="ru")

            bot2.send_message(message_0.chat.id, fr"Question: {pi}")
            bot2.send_message(message_0.chat.id, fr"Вопрос: {pi_tr.text}")

            bot2.send_message(message_0.chat.id, fr"Напишите 'show', чтобы показать ответ")
            bot2.register_next_step_handler(message_0, answer_mess)

            print("translate")
            print(message.from_user.first_name, "\n")

    def answer_mess(message_1):
        nonlocal r
        global t

        tr = message_1.text

        if str(tr).lower() == "show":
            for i in r.json():
                t = dict(i)
                print(t)

            pi = (t["answer"])
            pi_tr = translate.translate(pi, dest="ru")

            bot2.send_message(message_1.chat.id, fr"Answer: {pi}")
            bot2.send_message(message_1.chat.id, fr"Ответ: {pi_tr.text}")

    quest_repl(message)
    answer_mess(message)


@bot2.message_handler(commands=["fact"])
def fact_mes(message):
    r = requests.get("https://randstuff.ru/fact/").text
    soup = bs(r, features="html.parser")
    t_f = soup.find_all("table", class_="text")

    for i in t_f:
        bot2.send_message(message.chat.id, i.text)

        print(i.text)
    print("fact")
    print(message.from_user.first_name, "\n")


@bot2.message_handler(commands=["fact_num"])
def fact_num_mes(message):
    bot2.send_message(message.chat.id, "Введите число(арабской цифрой)")
    bot2.register_next_step_handler(message, num)


def num(message):
    global number
    number = message.text
    head = {"Content-Type": "application/json"}

    r = requests.get(f"http://numbersapi.com/{number}", headers=head)
    r1 = r.json()

    result = translate.translate(r1['text'], dest='ru')
    bot2.send_message(message.chat.id, (r1['text'], " - en"))
    bot2.send_message(message.chat.id, (result.text, " - ru"))

    print("number_fact")
    print(r1['text'])
    print(result.text)
    print(message.from_user.first_name, "\n")


@bot2.message_handler(commands=["wisdom"])
def wisdom_m(message):
    r = requests.get("https://randstuff.ru/saying/").text
    soup = bs(r, features="html.parser")
    t_w = soup.find_all("table", class_="text")

    for i in t_w:
        bot2.send_message(message.chat.id, i.text)

        print(i.text)
    print("wisdom")
    print(message.from_user.first_name, '\n')


@bot2.message_handler(commands=["prediction"])
def pred_m(message):
    r = random.randint(0, 19)
    if r >= 15:
        bot2.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGlGdjg69-0FRjgthPJRR71_9buZ2MTQACWAADrWW8FAv2smoo5exVKwQ")

    if r < 15 and r > 10:
        bot2.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGlxVjhLTso9o1x8hDV8tvQlDo23ekfAACSgADrWW8FIl7DV4Ij3qSKwQ")

    if r <= 9:
        bot2.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGlGljg6-uJBoJ_R8n6jYOdTM0e268NAACTgADrWW8FCFszl8rK9s8KwQ")

    bot2.send_message(message.chat.id, pred_l[r])
    print(pred_l[r])
    print(message.from_user.first_name, '\n')


@bot2.message_handler(commands=["food"])
def start_message(message):
    bot2.send_message(message.chat.id, "Напишите рубрикатор(писать цифрами):\n"
                                       "1] 'супы'\n"
                                       "2] 'выпечка'\n"
                                       "3] 'вторые блюда'\n"
                                       "4] 'напитки'\n"
                                       "5] 'салаты'\n"
                                       "6] 'десерты'\n")

    bot2.register_next_step_handler(message, ch)

    print("food")
    print(message.from_user.first_name)


def ch(message):
    global u
    tr2 = str(message.text).lower()
    print(tr2)
    try:
        if tr2 == "1" or tr2 == "суп" or tr2 == "супы":
            u = "1"
            food_pres(message, "https://www.iamcook.ru/showsubsection/other-soups")

        if tr2 == "3" or tr2 == "вторые блюда":
            u = "3"
            food_pres(message, "https://www.iamcook.ru/showsubsection/main-dishes")

        if tr2 == "2" or tr2 == "выпечка":
            u = "2"
            food_pres(message, "https://www.iamcook.ru/event/baking")

        if tr2 == "4" or tr2 == "напитки":
            u = "4"
            food_pres(message, "https://www.iamcook.ru/showsubsection/bezalcoholnie_napitki")

        if tr2 == "5" or tr2 == "салаты" or tr2 == "салат":
            u = "5"
            food_pres(message, "https://www.iamcook.ru/showsubsection/salads")

        if tr2 == "6" or tr2 == "десерты" or tr2 == "десерт":
            u = "6"
            food_pres(message, "https://www.iamcook.ru/showsubsection/other-desert")
    except IndexError:
        bot2.send_message(message.chat.id, "Повторите попытку")


def food_pres(message, url_text):
    # получение сайта и его кода
    abc_murders = random.randint(1, 25)
    t442 = requests.get(f"{url_text}/{abc_murders}")
    soup_text = bs(t442.content, "lxml")
    soup_pict = bs(t442.text, "lxml")

    # получение частей кода
    rec_name_re = soup_text.find_all("div", class_="header")  # получение названия el121844
    rec_time_re = soup_text.find_all("div", class_="description")  # получение времени готовки
    rec_des_re = soup_text.find_all("div", class_="ingredients")  # получение описания

    # константы
    n_h1_r = random.randint(0, len(rec_name_re))


    # # # Название # # #

    # вспомогательные константы
    n_end = ""
    n_h2 = 0

    # конечное название
    for i in rec_name_re:
        if n_h2 == n_h1_r:
            print("Название: ")
            n_end = i.text
            print(n_end, "\n")
            gt = n_end, "\n"
            bot2.send_message(message.chat.id, "Название: ")
            bot2.send_message(message.chat.id, gt)

        n_h2 += 1


    # # # Описание # # #

    # константы
    t_h1 = 0

    # получение
    for j in rec_time_re:
        if t_h1 == n_h1_r:
            time_end = f"{j.text}\n"
            print("Описание:")
            print(time_end, "\n")
            gt1 = time_end, "\n"
            bot2.send_message(message.chat.id, "Описание:")
            bot2.send_message(message.chat.id, gt1)
        t_h1 += 1


    # # # Ингридиенты # # #

    # константы
    des_h1 = 0

    # получение
    for z in rec_des_re:
        if des_h1 == n_h1_r:
            des_end = z.text
            print("Ингридиенты: ")
            print(des_end[12::], "\n")
            gt2 = des_end[12::], "\n"
            bot2.send_message(message.chat.id, "Ингридиенты: ")
            bot2.send_message(message.chat.id, gt2)
        des_h1 += 1
    tyur = n_h1_r


    # # # Картинка # # #

    find_block = soup_pict.find_all("div", class_="recblockwideleft")

    list_link = []
    gtre = ''
    for ii in find_block:
        pr = str(ii("img"))[45:-4:]

        if u != "2":
            list_link.append(f"https://i{pr}")

        elif u == "2":
            list_link.append(f"https:{pr}")


    print(list_link)
    end_pic = list_link[n_h1_r]
    print(end_pic)
    for pi in end_pic:
        if pi == ' ':
            break
        gtre += pi
    if u != "2":
        end_pic_1 = gtre[:-1:]
        end_pic_l = requests.get(end_pic_1).content
        with open(fr"C:\pythonProjectFBot\food_chicken_pic\pic_{n_end}.jpeg", "wb") as fl:
            fl.write(end_pic_l)
    if u == "2":
        end_pic_1 = gtre
        end_pic_l = requests.get(end_pic_1).content
        with open(fr"{my_dir}\food_chicken_pic\pic_{n_end}.jpeg", "wb") as fl:
            fl.write(end_pic_l)

    poiu = open(fr"{my_dir}/food_chicken_pic\pic_{n_end}.jpeg", "rb")
    bot2.send_photo(message.chat.id, poiu)
    poiu.close()


    # # # URL # # #

    find_block = soup_pict.find_all("div", class_="header")

    list_link_res = []

    for ii1 in find_block:
        pr2 = str(ii1("a"))[10:28]
        if pr2[-1::] == ">":
            pr2 = pr2[:-1]
        if pr2[-2::] == "><":
            pr2 = pr2[:-2]
        pr2 = pr2[:-1]
        list_link_res.append(f"https:{pr2}")
    end_res_link = list_link_res[tyur]
    print(end_res_link)
    bot2.send_message(message.chat.id, end_res_link[0:6] + "//www.iamcook.ru" + end_res_link[6::])


@bot2.message_handler(commands=['book'])
def start_message(message):
    bot2.send_message(message.chat.id, "Напишите рубрикатор(писать цифрами):\n"
                                       "1] 'Детективы и триллеры'\n"
                                       "2] 'Компьютеры и интернет'\n"
                                       "3] 'Дом и дача'\n"
                                       "4] 'Техника'\n"
                                       "5] 'Научно-образовательная'\n"
                                       "6] 'Фантастика и фентези'\n"
                                       "7] 'Зарубежная лит-ра'\n"
                                       "8] 'Документальная лит-ра'\n"
                                       "9] 'Приключение'\n"
                                       "10] 'Прочее'\n"
                                       "11] 'Знание и навыки'")

    bot2.register_next_step_handler(message, ch1)

    print("book")
    print(message.from_user.first_name)


def ch1(message):
    tr2 = str(message.text).lower()
    print(tr2)
    if tr2 == "1":
        book_pres(message, "https://www.litmir.me/bs?g=g2&p")

    if tr2 == "2":
        book_pres(message, "https://www.litmir.me/bs?g=g10&p")

    if tr2 == "3":
        book_pres(message, "https://www.litmir.me/bs/?g=g25&p")

    if tr2 == "4":
        book_pres(message, "https://www.litmir.me/bs?g=g18&p")

    if tr2 == "5":
        book_pres(message, "https://www.litmir.me/bs?g=g9&p")

    if tr2 == "6":
        book_pres(message, "https://www.litmir.me/bs?g=g1&p")

    if tr2 == "7":
        book_pres(message, "https://www.litmir.me/bs/?g=g26&p")

    if tr2 == "8":
        book_pres(message, "https://www.litmir.me/bs/?g=g12&p")

    if tr2 == "9":
        book_pres(message, "https://www.litmir.me/bs/?g=g5&p")

    if tr2 == "10":
        book_pres(message, "https://www.litmir.me/bs/?g=g19&p")

    if tr2 == "11":
        book_pres(message, "https://www.litmir.me/bs/?g=g27&p")


def book_pres(message, url_text):
    nt = ''
    am_list = 0
    if url_text == "https://www.litmir.me/bs?g=g2&p":
        am_list = 675

    elif url_text == 'https://www.litmir.me/bs?g=g10&p':
        am_list = 27

    elif url_text == 'https://www.litmir.me/bs/?g=g25&p':
        am_list = 52

    elif url_text == "https://www.litmir.me/bs?g=g18&p":
        am_list = 33

    elif url_text == "https://www.litmir.me/bs?g=g9&p":
        am_list = 879

    elif url_text == "https://www.litmir.me/bs?g=g1&p":
        am_list = 4000

    elif url_text == "https://www.litmir.me/bs/?g=g26&p":
        am_list = 1094

    elif url_text == "https://www.litmir.me/bs/?g=g12&p":
        am_list = 1094

    elif url_text == "https://www.litmir.me/bs/?g=g5&p":
        am_list = 472

    elif url_text == "https://www.litmir.me/bs/?g=g19&p":
        am_list = 661

    elif url_text == "https://www.litmir.me/bs/?g=g27&p":
        am_list = 1096

    # получение сайта и его кода

    abc_murders = random.randint(1, am_list)
    t442 = requests.get(f"{url_text}={abc_murders}")
    soup_text = bs(t442.content, "lxml")
    soup_pict = bs(t442.text, "lxml")


    # получение частей кода

    rec_name_re = soup_text.find_all("span", itemprop="name")  # получение названия el121844
    rec_data_re = soup_text.find_all("div", class_="desc_container")  # получение времени готовки
    rec_descript_re = soup_text.find_all("div", class_="description")


    # константы

    n_h1_r = random.randint(1, 25)
    print(n_h1_r)


    # # # Название # # #

    name_c = 0
    ipi = []
    ipip = 0
    name_cell1 = []
    for name in rec_name_re:
        if name_c > 1:
            name_cell1.append(name.text)
        name_c += 1
    print(name_cell1[n_h1_r])
    bot2.send_message(message.chat.id, name_cell1[n_h1_r])


    # # # Инфо # # #


    # константы/переменные
    data_h_5 = 0
    data_h_4 = 0
    data_h_3 = 0
    data_h_2 = 0
    data_h_1 = 0
    io = 0
    data_h_0 = 0
    data_seria = ''
    data_athor = ''
    data_genre = ''
    data_year = ''
    data_language = ''
    p = ''


    # получение строки
    for data in rec_data_re:
        if data_h_0 == n_h1_r:
            p = data.text
        data_h_0 += 1


    # всего данных
    for i in range(len(p)):
        if p[i] == ":":
            data_h_1 += 1


    # складывание, преобразование и распределение
    for i in range(len(p)):
        if p[i] == ":":
            io += 1


            # автор
            if io == 2:
                data_athor = p[:i - 4:]
                data_h_2 = i


            # если все 6 есть
            if data_h_1 == 6:


                # Жанр
                if io == 3:
                    data_genre = p[data_h_2 - 4:i - 5]
                    data_h_3 = i


                # cерия
                if io == 4:
                    data_seria = p[data_h_3 - 5:i - 3]
                    data_h_4 = i


                # год
                if io == 5:
                    data_year = p[data_h_4 - 3:i - 10]
                    data_h_5 = i


                # язык и страницы
                if io == 6:
                    data_language = p[data_h_5 - 10:i - 7]


            # если 5
            if data_h_1 == 5:

                # Жанр
                if io == 3:
                    data_genre = p[data_h_2 - 4:i - 3]
                    data_h_3 = i

                # год
                if io == 4:
                    data_year = p[data_h_3 - 3:i - 10]
                    data_h_5 = i

                # язык и страницы
                if io == 5:
                    data_language = p[data_h_5 - 7:i - 7]


            # если 4
            if data_h_1 == 4:
                # Жанр
                if io == 3:
                    data_genre = p[data_h_2 - 4:i - 10]
                    data_h_3 = i


                # язык и страницы
                if io == 4:
                    data_language = p[data_h_3 - 7:i - 7]


    if data_h_1 == 6:
        data_athor = data_athor[7::]
        data_genre = data_genre[6::]
        data_seria = data_seria[7::]
        data_year = data_year[5::]
        data_language = data_language[12::]

        end_ = (f"Автор - {data_athor}\n"
                f"Жанр - {data_genre}\n"
                f"Серия - {data_seria}\n"
                f"Год - {data_year}\n"
                f"Язык книги - Русский\n")

        print(end_)
        bot2.send_message(message.chat.id, end_)

    if data_h_1 == 5:

        data_athor = data_athor[7::]
        if data_genre[-2] == "С":
            print("::::::")
            data_genre = data_genre[:-2:]
            data_genre = data_genre[6::]
            data_language = data_language[12::]
            data_language = f'Рус{data_language}'
            data_year = data_year[5::]
            end_ = (f"Автор - {data_athor}\n"
                    f"Жанр - {data_genre}\n"
                    f"Серия - {data_year}\n"
                    f"Язык книги - Русский\n")
        else:
            print("::::::!+C")
            data_genre = data_genre[6::]
            data_language = data_language[12::]
            end_ = (f"Автор - {data_athor}\n"
                    f"Жанр - {data_genre}\n"
                    f"Год - {data_year}\n"
                    f"Язык книги - Русский\n")

        print(end_)
        bot2.send_message(message.chat.id, end_)

    if data_h_1 == 4:
        data_athor = data_athor[7::]
        data_genre = data_genre[6::]
        data_language = data_language[12::]

        end_ = (f"Автор - {data_athor}\n"
                f"Жанр - {data_genre}\n"
                f"Язык книги - Русский\n")

        print(end_)
        bot2.send_message(message.chat.id, end_)



    # # # Описание # # #


    for desc in rec_descript_re:
        if ipip % 2 != 0:
            print(desc.text, "\n")
            ipi.append(desc.text)
        ipip += 1
    try:
        bot2.send_message(message.chat.id, ipi[n_h1_r])
    except Exception:
        bot2.send_message(message.chat.id, "Описание отсутствует")

    # # # # # # # # # # # # # # # # # # # # # try # # # # # # # # # # # # # # # # # #  # # #

    # # # Картинка # # #

    find_block = soup_pict.find_all("img", class_="lt32 lazy")

    koij = 0
    op = 0

    for ii in find_block:
        iop1 = str(ii)
        if op == n_h1_r:
            for ii1 in range(len(iop1)):
                if iop1[ii1] == '"':
                    koij += 1
                    if koij == 5:
                        end_alpha_pic = iop1[ii1:ii1+45]
                        end_beta_pic = end_alpha_pic[1:-3:]
                        if end_beta_pic[-1] == "j":
                            nt = f"https://www.litmir.me{end_beta_pic}pg"
                        else:
                            nt = f"https://www.litmir.me{end_beta_pic}"
        op += 1

    print(nt)

    if nt[-1] == "/":
        print('/img/')
        nt = nt[:-25:]
        print(nt)

    if nt[-1].isdigit():
        print('.jpg')
        nt = f'{nt}.jpg'
        print(nt)

    try:
        if nt[59] == '"':
            print('59')
            nt = nt[:59:]
            print(nt)
    except IndexError:
        print('')

    if nt[-1] == ".":
        print('jpg')
        nt = f'{nt}jpg'
        print(nt)

    '''if nt[-1] == "/" or nt[-1] == '.' or nt[-1] == 'g' or nt[-1] == '"':
        print('Us')
        nt = f'{nt}.jpg'
        print(nt)'''

    if nt[-4::] == ".jpg" or nt[-4::] == ".png":
        print("OK")
        pass

    name_pic = name_cell1[n_h1_r].replace('"', '')
    name_pic = name_pic.replace("?", "")
    name_pic = name_pic.replace("/", "")
    name_pic = name_pic.replace(">", "")
    name_pic = name_pic.replace("<", "")

    end_pic_l = requests.get(nt).content
    with open(fr"{my_dir}\book_pic\pic_{name_pic}.jpeg", "wb") as fl:
        fl.write(end_pic_l)

    poiu = open(fr"{my_dir}\book_pic\pic_{name_pic}.jpeg", "rb")
    bot2.send_photo(message.chat.id, poiu)
    poiu.close()


    # # # URL # # #

    find_block = soup_pict.find_all("div", class_="book_name")

    list_link_res = []

    for ii1 in find_block:
        pr2 = str(ii1("a"))
        pr2 = pr2[10:23:]
        list_link_res.append(f"https:/{pr2}")
    end_res_link = list_link_res[n_h1_r]
    print(end_res_link)
    bot2.send_message(message.chat.id, end_res_link[0:6] + "//www.litmir.me" + end_res_link[6::])


@bot2.message_handler(commands=["plant"])
def feedback_p(message):
    bot2.send_message(message.chat.id, "Выберете рубрикатор(цифра):\n"
                                      "1] Семена овощей, пряных культур, ягод\n"
                                      "2] Семена цветов\n"
                                      "3] Tрава для домашних животных\n"
                                      "4] Семена овощей серии «Урожайная грядка»\n"
                                      "5] Сидераты\n")

    bot2.register_next_step_handler(message, feed_p_1)


def feed_p_1(message):
    global plant_rub
    plant_rub = message.text

    if plant_rub == '1':
        plant_core_1(message, 'https://www.sedek.ru/catalog/semena-ovoshchey-pryanykh-kultur-yagod/', 1)

    if plant_rub == '2':
        plant_core_1(message, 'https://www.sedek.ru/catalog/semena-tsvetov/', 2)

    if plant_rub == '3':
        plant_core_1(message, 'https://www.sedek.ru/catalog/trava-dlya-domashnikh-zhivotnykh/', 3)

    if plant_rub == '4':
        plant_core_1(message, 'https://www.sedek.ru/catalog/semena-ovoshchey-serii-urozhaynaya-gryadka-ovoshchi-optom/',
                     4)

    if plant_rub == '5':
        plant_core_1(message, 'https://www.sedek.ru/catalog/sideraty/', 5)


def plant_core_1(message, url_main, rubric):
    # отправление запросов на страницы
    global url
    global m_r
    m_r = rubric
    if m_r == 3 or m_r == 5:
        print("::::")
        plant_core_2_ex(message, url_main)
    else:
        r = requests.get(url_main)

        # добыча кода страницы каталога

        soup = bs(r.content, features="html.parser")
        urls = soup.find_all("a", class_='catalog-list__i-link')


        # константы каталога

        p_0 = 0
        p_2 = 0
        name = []
        url = []
        p_4 = -1
        c = 0


        # " main " - каталог

        for u in urls:
            print(str(u.text).strip())
            name.append(str(u.text).strip())

        for i in urls:
            p = 0
            o = str(i)
            print(o, '\n')
            p_4 += 1

            for i1 in range(len(o)):
                if o[i1] == '"':
                    p += 1

                    if p == 3:
                        p_0 = i1

                    if p == 4:
                        p_1 = i1

                        print(f'https://www.sedek.ru{o[p_0+1:p_1]}')
                        url.append(f'https://www.sedek.ru{o[p_0+1:p_1]}')
                        bot2.send_message(message.chat.id, f'{p_4}] {name[p_4]}')

                    if p == 9:
                        p_2 = i1
                    if p == 10:
                        p_3 = i1
                        print(f'https://www.sedek.ru{o[p_2+1:p_3]}')

                        pic_plant = requests.get(f'https://www.sedek.ru{o[p_2+1:p_3]}').content

                        with open(fr"C:\pythonProjectFBot\plant_pic\pic_{name[c]}.jpeg", "wb") as fl:
                            fl.write(pic_plant)

                        poiu = open(fr"C:\pythonProjectFBot\plant_pic\pic_{name[c]}.jpeg", "rb")
                        bot2.send_photo(message.chat.id, poiu)

            c += 1


        print(name, ' - название из каталога')
        print(url, ' - ссылки из каталога')
        bot2.send_message(message.chat.id, 'напишите цифру')
        bot2.register_next_step_handler(message, feed_p_2)


def feed_p_2(message):
    global url
    global rub_0
    global m_r
    rub_0 = int(message.text)
    print(rub_0)
    plant_core_2(message, url[rub_0])


def plant_core_2_ex(message, url_):
    global url_0_d_ex_1
    r_down_d = requests.get(url_)
    print("OK")
    soup_down_d = bs(r_down_d.content, features='html.parser')
    soup_f_0_d = soup_down_d.find_all('span', class_='related-products__i-txt')
    soup_f_1_d = soup_down_d.find_all('a', class_='content-list__i-link')

    p_2_down4_d = 0
    p_0_down2_d = 0
    p_down_4_d = 0
    c_down_d = 0
    name_down_d = []

    for i_down_d in soup_f_0_d:
        print(i_down_d.text)
        name_down_d.append(i_down_d.text)

    for i_down_d_1 in soup_f_1_d:
        print(i_down_d_1)
        o_do_d = str(i_down_d_1)

        p_down1_d = 0

        for i2_down_d_1 in range(len(o_do_d)):
            if o_do_d[i2_down_d_1] == '"':
                p_down1_d += 1

                if p_down1_d == 3:
                    p_0_down2_d = i2_down_d_1
                if p_down1_d == 4:
                    p_1_down3_d = i2_down_d_1
                    print()
                    print(f'https://www.sedek.ru{o_do_d[p_0_down2_d + 1:p_1_down3_d]}')
                    url_0_d_ex_1.append(f'https://www.sedek.ru{o_do_d[p_0_down2_d + 1:p_1_down3_d]}')
                    bot2.send_message(message.chat.id, f'{p_down_4_d}] {name_down_d[p_down_4_d]}')

                if p_down1_d == 13:
                    p_2_down4_d = i2_down_d_1
                if p_down1_d == 14:
                    p_3_down5_d = i2_down_d_1
                    print(f'https://www.sedek.ru{o_do_d[p_2_down4_d + 1:p_3_down5_d]}')

                    end_pic_pl = requests.get(f'https://www.sedek.ru{o_do_d[p_2_down4_d + 1:p_3_down5_d]}').content

                    with open(fr"C:\pythonProjectFBot\plant_pic\pic2e_{name_down_d[c_down_d]}.jpeg", "wb") as fl:
                        fl.write(end_pic_pl)

                    poiu = open(fr"C:\pythonProjectFBot\plant_pic\pic2e_{name_down_d[c_down_d]}.jpeg", "rb")
                    bot2.send_photo(message.chat.id, poiu)

        c_down_d += 1
        p_down_4_d += 1

    bot2.register_next_step_handler(message, feed_ex)


def feed_ex(message):
    global tpo
    global url_0_d_ex_1
    tpo = int(message.text)
    plant_ex_2(message, url_0_d_ex_1[tpo])
    url_0_d_ex_1 = []


def plant_ex_2(message, url_):
    r_down_d = requests.get(url_)
    soup_down_d = bs(r_down_d.content, features='html.parser')
    soup_f_0_d = soup_down_d.find_all('div', class_='col-12 col-md-7')

    for i_down_d in soup_f_0_d:
        bot2.send_message(message.chat.id, i_down_d.text)


def plant_core_2(message, url_):
    global url_0_d
    r_down_d = requests.get(url_)

    soup_down_d = bs(r_down_d.content, features='html.parser')

    soup_f_0_d = soup_down_d.find_all('span', class_='related-products__i-txt')
    soup_f_1_d = soup_down_d.find_all('a', class_='content-list__i-link')

    p_2_down4_d = 0
    p_0_down2_d = 0
    p_down_4_d = 0
    c_down_d = 0


    url_0_d = []
    name_down_d = []

    for i_down_d in soup_f_0_d:
        print(i_down_d.text)
        name_down_d.append(i_down_d.text)

    for i_down_d_1 in soup_f_1_d:
        print(i_down_d_1)
        o_do_d = str(i_down_d_1)

        p_down1_d = 0

        for i2_down_d_1 in range(len(o_do_d)):
            if o_do_d[i2_down_d_1] == '"':
                p_down1_d += 1


                if p_down1_d == 3:
                    p_0_down2_d = i2_down_d_1
                if p_down1_d == 4:
                    p_1_down3_d = i2_down_d_1
                    print()
                    print(f'https://www.sedek.ru{o_do_d[p_0_down2_d + 1:p_1_down3_d]}')
                    url_0_d.append(f'https://www.sedek.ru{o_do_d[p_0_down2_d + 1:p_1_down3_d]}')
                    bot2.send_message(message.chat.id, f'{p_down_4_d}] {name_down_d[p_down_4_d]}')


                if p_down1_d == 13:
                    p_2_down4_d = i2_down_d_1
                if p_down1_d == 14:
                    p_3_down5_d = i2_down_d_1
                    print(f'https://www.sedek.ru{o_do_d[p_2_down4_d + 1:p_3_down5_d]}')


                    end_pic_pl = requests.get(f'https://www.sedek.ru{o_do_d[p_2_down4_d + 1:p_3_down5_d]}').content

                    with open(fr"{my_dir}\plant_pic\pic2_{name_down_d[c_down_d]}.jpeg", "wb") as fl:
                        fl.write(end_pic_pl)

                    poiu = open(fr"{my_dir}\plant_pic\pic2_{name_down_d[c_down_d]}.jpeg", "rb")
                    bot2.send_photo(message.chat.id, poiu)


        c_down_d += 1
        p_down_4_d += 1


    bot2.send_message(message.chat.id, 'напишите цифру')
    bot2.register_next_step_handler(message, feed_p_3)


def feed_p_3(message):
    global url_0_d
    global rub_2
    rub_2 = int(message.text)

    if m_r == 1 and rub_2 == 47:
        plant_core_3_ex(message, url_0_d[rub_2])
    elif m_r == 2 and rub_2 == 0:
        plant_core_3_ex(message, url_0_d[rub_2])
    elif m_r == 2 and rub_2 == 1:
        plant_core_3_ex(message, url_0_d[rub_2])
    else:
        plant_core_3(message, url_0_d[rub_2])


def plant_core_3_ex(message, url_):
    global url_0_d_ex
    r_down_d = requests.get(url_)

    soup_down_d = bs(r_down_d.content, features='html.parser')

    soup_f_0_d = soup_down_d.find_all('span', class_='related-products__i-txt')
    soup_f_1_d = soup_down_d.find_all('a', class_='content-list__i-link')

    p_2_down4_d = 0
    p_0_down2_d = 0
    p_down_4_d = 0
    c_down_d = 0

    url_0_d_ex = []
    name_down_d = []

    for i_down_d in soup_f_0_d:
        print(i_down_d.text)
        name_down_d.append(i_down_d.text)

    for i_down_d_1 in soup_f_1_d:
        print(i_down_d_1)
        o_do_d = str(i_down_d_1)

        p_down1_d = 0

        for i2_down_d_1 in range(len(o_do_d)):
            if o_do_d[i2_down_d_1] == '"':
                p_down1_d += 1

                if p_down1_d == 3:
                    p_0_down2_d = i2_down_d_1
                if p_down1_d == 4:
                    p_1_down3_d = i2_down_d_1
                    print()
                    print(f'https://www.sedek.ru{o_do_d[p_0_down2_d + 1:p_1_down3_d]}')
                    url_0_d_ex.append(f'https://www.sedek.ru{o_do_d[p_0_down2_d + 1:p_1_down3_d]}')
                    bot2.send_message(message.chat.id, f'{p_down_4_d}] {name_down_d[p_down_4_d]}')

                if p_down1_d == 13:
                    p_2_down4_d = i2_down_d_1
                if p_down1_d == 14:
                    p_3_down5_d = i2_down_d_1
                    print(f'https://www.sedek.ru{o_do_d[p_2_down4_d + 1:p_3_down5_d]}')

                    end_pic_pl = requests.get(f'https://www.sedek.ru{o_do_d[p_2_down4_d + 1:p_3_down5_d]}').content

                    with open(fr"{my_dir}\plant_pic\pic2e_{name_down_d[c_down_d]}.jpeg", "wb") as fl:
                        fl.write(end_pic_pl)

                    poiu = open(fr"{my_dir}\plant_pic\pic2_{name_down_d[c_down_d]}.jpeg", "rb")
                    bot2.send_photo(message.chat.id, poiu)

        c_down_d += 1
        p_down_4_d += 1


def plant_core_3(message, url_):
    r_down_d = requests.get(url_)
    soup_down_d = bs(r_down_d.content, features='html.parser')
    soup_f_0_d = soup_down_d.find_all('div', class_='col-12 col-md-7')

    for i_down_d in soup_f_0_d:
        bot2.send_message(message.chat.id, i_down_d.text)



bot2.infinity_polling()
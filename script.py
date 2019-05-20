
from app.model.vk.vk import Vk
from settings import *
from app.db.db import DB


db_obj = DB(
    "dbname='masya' "
    f"user='{config['db_user']}' "
    f"host='{config['db_host']}' "
    f"password='{config['db_password']}'"
)

vk_obj = Vk(config['token'])


def get_data():
    return db_obj.get_all()


def send_auto_rasp():
    data = get_data()
    for person_data in data:
        try:
            a = str(person_data[0]).replace("(","").replace(")","").replace(",","")
            person_id = a
            vk_obj.send_message(person_id, "Уже в этот четверг и пятницу в "
                                           "нашем колледже произойдет "
                                           "инновационная конференция - "
                                           "MRCConf!\nСкорее успей "
                                           "зарегистрироваться! "
                                           "Полностью бесплатно, "
                                           "осталось немного времени\n"
                                           "MRCConf - это инновационная "
                                           "конференция в стенах колледжа "
                                           "по frontend & backend разработке, "
                                           "data science, машинному обучению, "
                                           "тестированию и маркетингу.\n "
                                           "😎Наша миссия - помочь учащимся МРК "
                                           "войти в IT и построить крутую "
                                           "карьеру.\n 👍🏻Лучшие кейсы на любой "
                                           "вкус из опыта наших учащихся!\n "
                                           "💪🏻Не просто конференция, но еще и "
                                           "мощный заряд мотивации, новые "
                                           "возможности и полезные "
                                           "знакомства.\n Даты: 23-24 мая\n "
                                           "Место: МРК\n Всем быть: "
                                           "mrcconf.github.io ", '')
        except:
            pass


def main():
    send_auto_rasp()


if __name__ == '__main__':
    main()

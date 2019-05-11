
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
<<<<<<< HEAD
          person_id = person_data[0],
          vk_obj.send_message(person_id, "MRCConf - это инновационная конференция в стенах колледжа по frontend & backend разработке, data science, машинному обучению, тестированию и маркетингу.\n 😎Наша миссия - помочь учащимся МРК войти в IT и построить крутую карьеру.\n 👍🏻Лучшие кейсы на любой вкус из опыта наших учащихся!\n 💪🏻Не просто конференция, но еще и мощный заряд мотивации, новые возможности и полезные знакомства.\n Даты: 23-24 мая\n Место: МРК\n Всем быть: mrcconf.github.io ", '')
=======
        a = str(person_data[0]).replace("(","").replace(")","").replace(",","")
        person_id = a
        vk_obj.send_message(person_id, "MRCConf - это инновационная "
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
>>>>>>> b520e8059c33ef07c9a24f618af06bf092bb7b3a

def main():
    send_auto_rasp()


if __name__ == '__main__':
    main()

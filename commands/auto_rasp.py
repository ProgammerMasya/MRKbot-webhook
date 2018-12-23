import command_system
import psycopg2
import pprint

conn = psycopg2.connect(
    "dbname='Masya' "
    "user='postgres' "
    "host='localhost' "
    "password='vlad3052001'"
)

cursor = conn.cursor()


def autorasp(user_id, content):

    if content in [
        '8к1191', '8к1591', '8к1391', '8к1111', '7к1191', '7к1591',
        '7к1391', '61391', '8к2491', '8к2492', '8к2493', '7к2491',
        '7к2492', '7к2493', '8к2411', '7к2411', '62491', '8к3791',
        '8к3291', '7к3791', '7к3291', '7к1111', '61191', '61591',
        '61111', '51191', '51591', '51592', '51391', '51392',
        '62492', '62493', '62411', '52491', '52492', '52493',
        '63791', '63291', '53791', '53291', '53292'
    ]:
        cursor.execute(""" SELECT * FROM mrk WHERE vk_id=%s""", (user_id,))
        user_data = cursor.fetchone()
        if not user_data:
            cursor.execute(""" INSERT INTO mrk(vk_id, grupe) VALUES (%s, %s)""",
                           (user_id, content))
            conn.commit()
            message = "Подписка оформлена!"
        else:
            message = "Вы уже подписались на автоматическое расписание"

    elif content == 'stop':
        cursor.execute(""" DELETE FROM mrk WHERE vk_id=%s """, (user_id,))
        conn.commit()
        message = "Подписка отменена"
        print(user_id)


    else:
        message = "Указанной вами группы не существует"

    cursor.execute(""" SELECT * FROM mrk """)
    rows = cursor.fetchall()
    print(rows)

    return message, "",


rasp_command = command_system.Command()

rasp_command.keys = ['/autorasp']
rasp_command.description = "Подписка на автоматическое расписание"
rasp_command.process = autorasp

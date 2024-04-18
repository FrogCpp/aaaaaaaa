# bot.send_message(message.from_user.id, "Привет")
# C:\\Users\\aleks\\Desktop\\frog_file\\config.txt
# 1775492300
import telebot
import time
from my_projekt.Telegram_bot.First_bot import get_http

bot = telebot.TeleBot('6941701570:AAHp7l4D4edCVHvh7-UdDKT5mD5rZXnQ54s')

way_to_file = input()
now_time = time.time()
conf = open(way_to_file, 'r')
my_conf = conf.read()
my_conf = my_conf.split('%')
conf.close()
find_to = my_conf[0]
n = int(my_conf[1])
if len(my_conf) <= 2: my_id = -1002133849518
else: my_id = my_conf[2]
count = 0
mass_to_send = get_http.get(find_to)
colcost = len(mass_to_send)

while True:
    time.sleep(1)

    if mass_to_send:
        if time.time() - n > now_time:
            now_time = time.time()
            bot.send_photo(my_id, mass_to_send[count])
            count += 1
            conf = open(way_to_file, 'r')
            my_conf = conf.read()
            my_conf = my_conf.split('%')
            conf.close()
            find_to = my_conf[0]
            n = int(my_conf[1])
            print(n, count, colcost)
            if len(my_conf) <= 2: my_id = -1002133849518
            else: my_id = my_conf[2]
        if count == colcost:
            mass_to_send = get_http.get(find_to)
            count = 0
            colcost = len(mass_to_send)
    else:
        f = open(way_to_file, 'w')
        my_conf[0] = ' '.join(my_conf[0].split()[1:])
        f.write('%'.join(my_conf))
        f.close()
import telebot
import os
import winreg

class Bot:
    def __init__(self, bot=telebot.TeleBot('6941701570:AAHp7l4D4edCVHvh7-UdDKT5mD5rZXnQ54s')):
        self.bot = bot
        self.code = '123'
        self.trash = '645FF040-5081-101B-9F08-00AA002F954E'

    def rename(self, name):
        location = winreg.HKEY_CURRENT_USER
        soft = winreg.OpenKey(location, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CLSID\\')

        key_1 = winreg.CreateKey(soft, '{645FF040-5081-101B-9F08-00AA002F954E}')
        winreg.SetValueEx(key_1, '', 0, winreg.REG_SZ, name)

    def command(self, command, message):
        command = f'{command}'
        command = command.split('/')
        command[1] = command[1].split(':')
        if command[0] != self.code: return False
        else:
            if command[1][0] == 'help':
                bot.send_message(message.chat.id, "1:переименовать мусорку: rename_trash\n 2:создать текстовый файл на рабочем столе: creat_txt")
                return True
            if command[1][0] == 'rename_trash':
                self.rename(command[1][1])
                return True
            if command[1][0] == 'creat_txt':
                dir_name = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
                f = open(os.path.join(dir_name, f'{command[1][1]}.txt'), 'w')
                f.close()
                return True
bot_bot = Bot()
bot = bot_bot.bot


@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.chat.id, "connect")
    if bot_bot.command(message.text, message=message):
        bot.send_message(message.chat.id,"sucsess")
bot.infinity_polling()

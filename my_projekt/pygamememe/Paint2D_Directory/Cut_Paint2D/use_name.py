import pygame
def generate():
    arr = {}
    step = 125
    count = 0
    for i in range(0, 255, step):
        for j in range(0, 255, step):
            for k in range(0, 255, step):
                arr[count] = (i, j, k)
                count += 1
    return arr


WIDTH = 1500
HEIGHT = 800
FPS = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINCK = (255, 102, 102)
ELLOW = (255, 255, 0)
FIOLETOVY = (153, 0, 153)
GRAY = (211, 211, 211)
GRAY_sustem = (221, 220, 220)
colors_setup = generate()
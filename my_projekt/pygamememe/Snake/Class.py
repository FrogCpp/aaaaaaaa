import pygame
import random
pygame.init

FPS = 60
WIDTH = 600
HIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 102, 102)
YELLOW = (255, 255, 0)
VIOLET = (153, 0, 153)
GRAY = (211, 211, 211)
GRAY_system = (221, 220, 220)
screen = pygame.display.set_mode((WIDTH, HIGHT))
class Object:
    def __init__(self, color=RED, width=0, x=WIDTH/2, y=HIGHT/2, size=(30, 30)):
        self.color = color
        self.width = width
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def Draw(self):
        pygame.draw.rect(surface=screen,
                         color=self.color,
                         width=self.width,
                         rect=(self.x, self.y, self.size[0], self.size[1]))

class Snake(Object):
    def __init__(self, x=WIDTH/2, y=HIGHT/2):
        super().__init__(x=x, y=y)
        self.color = GREEN
        self.Plus = False

    def WalkTo(self, coord=[0, -1]):
        self.x += self.size[0] * coord[0]
        self.y += self.size[1] * coord[1]
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y > HIGHT:
            self.y = 0
        if self.y < 0:
            self.y = HIGHT

    def colled(self, sprite): # подовай в спрайт голову змеи
        sprite.rect = pygame.Rect(sprite.x, sprite.y, sprite.size[0], sprite.size[1])
        rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        return rect.colliderect(sprite.rect)

class Apples(Object):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, HIGHT)
        self.y = random.randint(0, WIDTH)

    def colled(self, sprite): # подовай в спрайт голову змеи
        sprite.rect = pygame.Rect(sprite.x, sprite.y, sprite.size[0], sprite.size[1])
        rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        if rect.colliderect(sprite.rect):
            self.x = random.randint(0, HIGHT)
            self.y = random.randint(0, WIDTH)
            sprite.Plus = True
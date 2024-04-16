import pygame
import random
pygame.init

FPS = 60
WIDTH = 1000
HIGHT = 800
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

class obj():
    def __init__(self):
        self.color = WHITE
        self.x = 500
        self.y = 500
        self.size = [50, 50]
        self.width = 0
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def colled(self, sprite):
        sprite.rect = pygame.Rect(sprite.x, sprite.y, sprite.size[0], sprite.size[1])
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        return self.rect.colliderect(sprite.rect) # collidepoint(point)
class Platform(obj):
    def __init__(self):
        super().__init__()
        self.size = (100, 15)
        self.color = RED
        self.y = random.randint(0, HIGHT - self.size[1])
        self.x = random.randint(0, WIDTH - self.size[0])

    def move(self):
        global jump
        self.y += jump - 10
        if self.y >= HIGHT:
            self.y = random.randint(-15, 0)
            self.x = random.randint(0, WIDTH - self.size[0])

def draw_screen(sprits):
    screen.fill(BLACK)
    for sprit in sprits:
        pygame.draw.rect(surface=screen,
                         color=sprit.color,
                         width=sprit.width,
                         rect=(sprit.x, sprit.y, sprit.size[0], sprit.size[1]))

main_game = True
while main_game:
    game = True
    all_sprites = []
    my_obj = obj()
    my_obj.size = (25, 25)
    all_sprites.append(my_obj)
    platform1 = Platform()
    platform1.x = my_obj.x
    platform1.y = my_obj.y + my_obj.size[1] - 1
    all_sprites.append(platform1)
    for i in range(10): all_sprites.append(Platform())
    jump = 0
    clock = pygame.time.Clock()
    while game:
        clock.tick(FPS)

        if my_obj.y > int(HIGHT * 0.25): my_obj.y -= jump
        if jump > 0: jump -= 1

        coll_with_pl = my_obj.colled(platform1)
        for i in all_sprites[2:]: coll_with_pl = coll_with_pl or i.colled(my_obj)
        if coll_with_pl: ready_to_jump = True

        if my_obj.y < int(HIGHT * 0.25):
            platform1.move()
            for i in all_sprites[2:]: i.move()

        if my_obj.y >= HIGHT: game = False

        if my_obj.y < HIGHT and not coll_with_pl:
            my_obj.y += 10

        if pygame.key.get_pressed():
            keys = pygame.key.get_pressed()
            if keys[97]:
                my_obj.x -= 10
            if keys[100]:
                my_obj.x += 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                main_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and coll_with_pl:
                    jump += 35

        draw_screen(all_sprites)
        pygame.display.flip()

pygame.QUIT
exit()
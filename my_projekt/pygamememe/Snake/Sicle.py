import pygame
import Class
pygame.init()

screen = pygame.display.set_mode((Class.WIDTH, Class.HIGHT))
Game = True
Snake = []
Apples = []
clock = pygame.time.Clock()
player = Class.Snake()
Apple = Class.Apples()
Snake.append(player)
Apples.append(Apple)
fps_counter = 0
GoTo = [0, -1]

while Game:
    clock.tick(Class.FPS)
    if fps_counter < 30: fps_counter += 1
    else:
        fps_counter = 0
        old_pos = [Snake[0].x, Snake[0].y]
        Super_old_pos = [0, 0]
        for i in range(1, len(Snake)):
            sn = Snake[i]
            Super_old_pos = [sn.x, sn.y]
            sn.x = old_pos[0]
            sn.y = old_pos[1]
            old_pos = Super_old_pos
        Snake[0].WalkTo(GoTo)

    for i in Snake[1:]:
        if Snake[0].colled(i):
            Game = False

    if Snake[0].Plus:
        Snake[0].Plus = False
        sn = Snake[-1]
        Snake.append(Class.Snake(x=sn.x - sn.size[0] * GoTo[0], y=sn.y - sn.size[1] * GoTo[1]))

    for i in Apples: i.colled(Snake[0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and GoTo != (0, 1):
                GoTo = (0, -1)
            if event.key == pygame.K_s and GoTo != (0, -1):
                GoTo = (0, 1)
            if event.key == pygame.K_d and GoTo != (-1, 0):
                GoTo = (1, 0)
            if event.key == pygame.K_a and GoTo != (1, 0):
                GoTo = (-1, 0)

    screen.fill(Class.BLACK)
    for i in Snake: i.Draw()
    for i in Apples: i.Draw()
    pygame.display.flip()


pygame.QUIT
exit()
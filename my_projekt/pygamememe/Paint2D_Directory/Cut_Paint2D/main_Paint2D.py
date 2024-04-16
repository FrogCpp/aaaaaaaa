from tkinter import Tk
from tkinter.simpledialog import askstring
import pygame
import classes
import use_name


def draw(mass):
    for i in range(len(mass)):

        pygame.draw.line(screen, mass[i][1], mass[i+1][1], mass[i][0], 10)


def ascing(n='User input:'):
    root = Tk()
    root.withdraw()

    return askstring("Title", n)

pygame.init()

screen = pygame.display.set_mode((use_name.WIDTH, use_name.HEIGHT))
pygame.display.set_caption("Paint2D")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True
draw_poz = []
color_01 = 0
screen.fill(use_name.WHITE)
prev_pos = (0, 0)

panel = classes.obj(pozx=use_name.WIDTH - use_name.WIDTH / 16, pozy=0, size_inp=(
    use_name.WIDTH / 8, use_name.WIDTH * 2), col=use_name.GRAY_sustem)
color_indicate = classes.indication(indicate_color=use_name.BLUE, indikate_pos=(use_name.WIDTH - 60, 20))
all_sprites.add(panel)
all_sprites.add(color_indicate)
flag = False
size_draw = 10
counter_by_input_size = 0
counter_by_input_color = 0

color_indicate.move(move_color=use_name.colors_setup[color_01], move_pos=(use_name.WIDTH - 60, 20), size_idn=(size_draw, size_draw))

while running:
    clock.tick(use_name.FPS)
    if size_draw < 1: size_draw = 1

    if pygame.key.get_pressed():
        counter_by_input_size += 1
        counter_by_input_color += 1
        keys = pygame.key.get_pressed()
        if keys[1073741906] and counter_by_input_size == 15 and size_draw <= 110:
            size_draw += 1

        if keys[1073741905] and counter_by_input_size == 15 and size_draw > 1:
            size_draw -= 1

        if keys[1073741904] and counter_by_input_color == 30:
            color_01 += 1

        if keys[1073741903] and counter_by_input_color == 30:
            color_01 -= 1

        if counter_by_input_size == 15: counter_by_input_size = 0

        if counter_by_input_color == 30: counter_by_input_color = 0

        if color_01 < 0: color_01 = len(use_name.colors_setup) - 1

        if color_01 > len(use_name.colors_setup) - 1: color_01 = 0

        color_indicate.move(move_color=use_name.colors_setup[color_01], move_pos=(
            use_name.WIDTH - use_name.WIDTH / 16 - (size_draw / 2), use_name.HEIGHT * 0.1 - (size_draw / 2)), size_idn=(size_draw, size_draw))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen, color=use_name.colors_setup[color_01], center=event.pos, radius=(size_draw / 2))
                prev_pos = event.pos
                flag = True

        if event.type == pygame.MOUSEBUTTONUP:
            flag = False

        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and flag:
            pygame.draw.circle(screen, color=use_name.colors_setup[color_01], center=event.pos, radius=(size_draw / 2 - 1))
            pygame.draw.line(screen, color=use_name.colors_setup[color_01], start_pos=event.pos, end_pos=prev_pos, width=size_draw)
            prev_pos = event.pos

        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                way_to_save = ascing()
                rect = pygame.Rect(0, 0, use_name.WIDTH - use_name.WIDTH / 8, use_name.HEIGHT)
                sub = screen.subsurface(rect)
                pygame.image.save(sub, f"{way_to_save}.jpeg")
                print('saved')

        if event.type == pygame.KEYUP:
            counter_by_input_color = 0
            counter_by_input_size = 0

    all_sprites.draw(surface=screen)
    pygame.display.flip()
    all_sprites.update()
pygame.quit()
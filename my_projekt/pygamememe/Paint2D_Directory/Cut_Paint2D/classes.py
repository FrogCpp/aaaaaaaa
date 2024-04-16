import pygame
import use_name
class obj(pygame.sprite.Sprite):
    x = 0
    y = 0
    color = use_name.BLUE
    size = [10, 10]

    def __init__(self, pozx=use_name.WIDTH / 2, pozy=use_name.HEIGHT / 2, col=use_name.BLUE, size_inp=(10, 10)):
        self.x = pozx
        self.y = pozy
        self.color = col
        self.size = size_inp

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def run(self, axis='x', numb=0):
        if axis == 'x':
            self.rect.x += numb
        else:
            self.rect.y += numb

    def goto(self, mass_poz={0, 0}):
        self.rect.x = mass_poz[0]
        self.rect.y = mass_poz[1]


class indication(obj):
    def __init__(self, indikate_pos=(0, 0), indicate_color=use_name.BLACK):
        super().__init__(size_inp=(60, 60))
        self.move(move_pos=indikate_pos)
        self.color = indicate_color

    def move(self, move_color=obj.color, move_pos=(obj.x, obj.y), size_idn=(60, 60)):
        self.rect.x = move_pos[0]
        self.rect.y = move_pos[1]
        self.color = move_color
        self.image.fill(self.color)
        self.image = pygame.transform.scale(self.image, size_idn)
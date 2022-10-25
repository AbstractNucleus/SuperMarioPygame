import pygame
from pygame.locals import *
from pygame.color import Color
import sys


pygame.init()
screen = pygame.display.set_mode((640, 480))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((16, 32))
        self.image.fill(Color('red'))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.vel = (0, 0)
        self.acc = (0, 0)

    def update(self):
        self.rect.y += self.vel[1]
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.center = (screen.get_width() / 2, screen.get_height() / 2)

    def move(self, keys):
        movement = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}
        if keys:

            if keys[K_LEFT]:
                self.rect.move_ip(movement[K_LEFT])

    def check_collision(self, sprite):
        if self.rect.colliderect(sprite.rect):
            print("Collision")
            self.reset()


class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((screen.get_width(), screen.get_height()/8))
        self.image.fill(Color('green'))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, screen.get_height()-self.rect.height/2)

    def update(self):
        screen.blit(self.image, self.rect)


class Game():
    def __init__(self):
        self.player = Player()
        self.generate_map()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                pressed_keys = pygame.key.get_pressed()
                self.player.move(pressed_keys)

            self.update()

    def update(self):
        screen.fill((20, 20, 20))
        self.player.update()
        self.map.update()
        self.player.check_collision(self.map)
        pygame.display.update()

    def generate_map(self):
        self.map = Map()


if __name__ == '__main__':
    game = Game()
    game.run()

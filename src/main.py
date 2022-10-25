import pygame


pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    for i in pygame.event.get():
        print(i)

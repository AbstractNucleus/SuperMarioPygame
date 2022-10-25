import pygame
#from pygame.locals import *
import sys
from characters import movment
from characters import characters
from maps import bana_0
from characters.characters import players
from characters import movment

pygame.init()
screen = pygame.display.set_mode((640, 480))

x = 200
y = 200

bana_0.draw(pygame, screen)
while True:
    if y > 460:
        y -= 1
    if y <= 460:
        y += 0.1
    keys = pygame.key.get_pressed()
    for i in pygame.event.get():
        screen.fill((0,0,0))
        y = movment.movment_y(pygame,keys,y)
        x = movment.movment_x(pygame,keys,x)
        print(y)
        spelare = players(pygame, screen,x,y)
        pygame.display.update()
        #print(i)

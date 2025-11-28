import pygame
from pygame.locals import*

pygame.init()
screen_width=600
screen_height=500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("__Pong Game__")

#define colors
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
white=(255,255,255)

def Background():
    screen.fill(black)


running=True
while running:
    Background()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()
pygame.quit()

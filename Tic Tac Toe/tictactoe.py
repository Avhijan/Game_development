import pygame
import numpy as np
from pygame.locals import *

pygame.init()

screen_width=600
screen_height=600
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("--TIC TAC TOE--")

def grid():
    bg=(0,0,0)
    line_colour=(255,255,255)
    screen.fill(bg)
    for i in range(1,3):
        pygame.draw.line(screen, line_colour, (5, i*200), (screen_width-5, i*200),7 )
        pygame.draw.line(screen, line_colour, (i*200, 5), (i*200, screen_height-5),7 )

flags=np.array([[0,0,0],[0,0,0],[0,0,0]])
print(flags)
running=True
while running:
    grid()
    # to handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    pygame.display.update()
       
pygame.quit()
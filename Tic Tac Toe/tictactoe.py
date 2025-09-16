import pygame
import numpy as np
from pygame.locals import *

pygame.init()

screen_width=600
screen_height=600
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("--TIC TAC TOE--")
White=(255,255,255)
Red=(255,0,0)
Green=(0,255,0)
def grid():
    grid_width=7
    bg=(0,0,0)
    screen.fill(bg)
    for i in range(1,3):
        pygame.draw.line(screen, White, (5, i*200), (screen_width-5, i*200),grid_width )
        pygame.draw.line(screen, White, (i*200, 5), (i*200, screen_height-5),grid_width )

def draw_symbols():
    line_width=20
    y=0 
    for i in flags:
        x=0
        for j in i:
            if j == 1:
                pygame.draw.line(screen, Green,(x*200+30,y*200+30),(x*200+170,y*200+170), line_width )
                pygame.draw.line(screen, Green,(x*200+30,y*200+170),(x*200+170,y*200+30), line_width )
            if j ==-1:
                pygame.draw.circle(screen, Red,(x*200+100,y*200+100), radius=80,width=22)
            x+=1
        y+=1


flags=np.array([[0,0,0],[0,0,0],[0,0,0]])
print(flags)
click=False
position=[]
player=1
running=True
while running:
    grid()
    draw_symbols()
    # to handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    if event.type==pygame.MOUSEBUTTONDOWN and click==False:
        click=True

    if event.type==pygame.MOUSEBUTTONUP and click == True:
        click=False
        position=pygame.mouse.get_pos()
        x_position=position[0]
        y_position=position[1]
        if flags[y_position//200][x_position//200]==0: #(y,x) to represent the cells correctly in the matrix of numpy in terminal
            flags[y_position//200][x_position//200]=player
            player*=-1
        print(flags)

    
    pygame.display.update()
       
pygame.quit()
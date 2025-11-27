import pygame
from pygame.locals import *

pygame.init()

#screen size
screen_w= 600
screen_h= 600

#game varriables
cell_size=10
snake_position=[[int(screen_w/2),int(screen_h/2)]]
snake_position.append([int(screen_w/2),int((screen_w/2))+cell_size])
snake_position.append([int(screen_w/2),int((screen_w/2))+cell_size*2])
snake_position.append([int(screen_w/2),int((screen_w/2))+cell_size*3])

#colors
bg =(0, 255, 0)
snake_colour=(0,0,255)
snake_shade=(50,50,255)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

#create window 
screen= pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('Snake Game')

def draw_screen():
    screen.fill(bg)


running=True
while running:
    draw_screen()

    #evernt handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    #draw snake
    head=0
    for x in snake_position:
        if head == 1:
            pygame.draw.rect(screen,snake_colour,(x[0], x[1], cell_size,cell_size))
            pygame.draw.rect(screen,snake_shade,(x[0]+1, x[1]+1, cell_size-2,cell_size-2))
        if head ==0:
            pygame.draw.rect(screen,snake_colour,(x[0]-1,x[0]-1,cell_size+2,cell_size+2))
            #left eye
            pygame.draw.rect(screen,white,(x[0],x[1]+3,5,5))
            pygame.draw.rect(screen,black,(x[0]+1,x[1]+1+3,3,3))
            #right eye
            pygame.draw.rect(screen,white,(x[0]+5,x[1]+3,5,5))
            pygame.draw.rect(screen,black,(x[0]+6,x[1]+1+3,3,3))
            #mouth 
            pygame.draw.rect(screen,red,(x[0]+2,x[1]-1,6,3))

            head=1

        
    pygame.display.update()

pygame.quit()

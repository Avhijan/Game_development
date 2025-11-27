import pygame
from pygame.locals import *
import random

pygame.init()

#screen size
screen_w= 600
screen_h= 600

#game varriables
direction=1# up=1 , right=2, down=3 , left=4
update_snake=1
food=[0,0]
new_food=True
new_segment=[0,0]
score=0
font=pygame.font.SysFont(None, 40)
gameover =False
clicked=False


#snake 
cell_size=10
snake_position=[[int(screen_w/2),int(screen_h/2)]]
snake_position.append([int(screen_w/2),int((screen_h/2))+cell_size])
snake_position.append([int(screen_w/2),int((screen_h/2))+cell_size*2])
snake_position.append([int(screen_w/2),int((screen_h/2))+cell_size*3])

#colors
bg =(0, 255, 0)
snake_colour=(0,0,255)
snake_shade=(50,50,255)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)

#create window 
screen= pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('Snake Game')


def draw_screen():
    screen.fill(bg)

def show_score():
    score_txt='Score= '+str(score)
    score_img=font.render(score_txt, True, yellow)
    screen.blit(score_img,(0,0))



def check_gameover(gameover):
    #snake collision
    head_count=0
    for segment in snake_position:
        if snake_position[0]==segment and head_count>0:
            gameover=True
        head_count+=1
    #boundary collision
    if snake_position[0][0]<0 or snake_position[0][0]>screen_w or snake_position[0][1]<0 or snake_position[0][1]>screen_h:
        gameover=True
    return gameover

play_again_rect= Rect(screen_w//2-90, screen_h//2,180, 50)
def gameover_screen():
    gameover_txt="Game Over"
    gameover_img=font.render(gameover_txt, True, red)
    pygame.draw.rect(screen, black, (0,0, screen_h, screen_w ))
    screen.blit(gameover_img,(220, 50))

    again_txt="Play Again?"
    again_img=font.render(again_txt,True, red)
    pygame.draw.rect(screen, white ,play_again_rect,2,15)
    screen.blit(again_img,(screen_w//2-80, screen_h//2+10 , 160, 50))

running=True
while running:
    draw_screen()
    show_score()
   

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!=3:
                direction=1
            if event.key == pygame.K_RIGHT and direction!=4:
                direction=2
            if event.key == pygame.K_DOWN and direction!=1:
                direction=3
            if event.key == pygame.K_LEFT and direction!=2:
                direction=4

    if new_food==True:
        new_food=False
        food[0]=cell_size*random.randint(0,int(screen_w/cell_size)-1)
        food[1]=cell_size*random.randint(0,int(screen_h/cell_size)-1)
    #draw food
    pygame.draw.rect(screen,red,(food[0],food[1],cell_size,cell_size))

    #check collison
    if snake_position[0] == food:
        new_food=True
        new_segment=list(snake_position[-1])
        if direction== 1:
            new_segment[1] += cell_size
        if direction== 2:
            new_segment[0] -= cell_size
        if direction== 3:
            new_segment[1] -= cell_size
        if direction== 4:
            new_segment[0] += cell_size
        snake_position.append(new_segment)
        score += 1 

    if gameover== False:
        if update_snake>99:
            update_snake=0
            snake_position=snake_position[-1:]+snake_position[:-1]
            if direction==1:#up
                snake_position[0][0]=snake_position[1][0]
                snake_position[0][1]=snake_position[1][1] - cell_size
            if direction==3:#down
                snake_position[0][0]=snake_position[1][0]
                snake_position[0][1]=snake_position[1][1] + cell_size
            if direction==2:#right
                snake_position[0][1]=snake_position[1][1]
                snake_position[0][0]=snake_position[1][0] + cell_size
            if direction==4:#left
                snake_position[0][1]=snake_position[1][1]
                snake_position[0][0]=snake_position[1][0] - cell_size
            gameover=check_gameover(gameover)




    #draw snake
    head=0
    for x in snake_position:
        if head == 1:
            pygame.draw.rect(screen,snake_colour,(x[0], x[1], cell_size,cell_size))
            pygame.draw.rect(screen,snake_shade,(x[0]+1, x[1]+1, cell_size-2,cell_size-2))
        if head ==0:
            pygame.draw.rect(screen,snake_colour,(x[0],x[1],cell_size,cell_size))
            #left eye
            pygame.draw.rect(screen,white,(x[0],x[1]+3,5,5))
            pygame.draw.rect(screen,black,(x[0]+1,x[1]+1+3,3,3))
            #right eye
            pygame.draw.rect(screen,white,(x[0]+5,x[1]+3,5,5))
            pygame.draw.rect(screen,black,(x[0]+6,x[1]+1+3,3,3))
            #mouth 
            pygame.draw.rect(screen,red,(x[0]+2,x[1]-1,6,3))

            head=1


    if gameover==True:
        gameover_screen()
        if event.type==MOUSEBUTTONDOWN and clicked==False:
            clicked=True
        if event.type==MOUSEBUTTONUP and clicked==True:
            clicked=False
            pos=pygame.mouse.get_pos()
            if play_again_rect.collidepoint(pos):
                direction=1# up=1 , right=2, down=3 , left=4
                update_snake=1
                food=[0,0]
                new_food=True
                new_segment=[0,0]
                score=0
                font=pygame.font.SysFont(None, 40)
                gameover =False
                clicked=False

                #snake 
                cell_size=10
                snake_position=[[int(screen_w/2),int(screen_h/2)]]
                snake_position.append([int(screen_w/2),int((screen_h/2))+cell_size])
                snake_position.append([int(screen_w/2),int((screen_h/2))+cell_size*2])
                snake_position.append([int(screen_w/2),int((screen_h/2))+cell_size*3])
                head=0
                
    pygame.display.update()
    update_snake+=1

pygame.quit()

import pygame
import numpy as np
from pygame.locals import *

pygame.init()
#screen initialization
screen_width=600
screen_height=600
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("--TIC TAC TOE--")

#colours
White=(255,255,255)
Black=(0,0,0)
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



Winner=0
gameover=False
def check_winner():
    global Winner
    global gameover
    y=0
    for i in flags:
        # To check rows 
        if sum(i)==3:
            print("Cross Wins") # Player 1
            Winner=1
            gameover=True

        if sum(i)==-3:
            print("Circle Wins") #Player 2
            Winner=-1
            gameover=True

        #To check coloumns
        if flags[0][y]+ flags[1][y] +flags[2][y] == 3:
            print("Cross wins")
            Winner=1
            gameover=True

        if flags[0][y]+ flags[1][y] +flags[2][y] == -3:
            print("Circle wins")
            Winner=-1
            gameover=True
        y+=1
                 
    #To check diagnals 
    if flags[0][0]+flags[1][1]+flags[2][2]== 3 or flags[2][0]+ flags[1][1] +flags[0][2] == 3:
        print('Cross wins')
        Winner=1
        gameover=True

    if flags[0][0]+flags[1][1]+flags[2][2]== -3 or flags[2][0]+ flags[1][1] +flags[0][2] == -3:
            print("Circle wins")
            Winner=-1
            gameover=True

    #To check for draw
    full_cells=0
    for i in flags:
        for j in i:
            if j ==-1 or j==1:
                full_cells+=1
    if full_cells==9:
        gameover=True

#font and playagain button
Play_again_rect= Rect(295, 395, 250, 50)
font=pygame.font.SysFont(None, 100)
def gameover_screen(Winner):
    pygame.draw.rect(screen, Black, (0, 0, screen_width, screen_height)) #background for gameover screen


    # Winner message
    x_m=100
    y_m=150
    x_pm=300
    y_pm=400
    if Winner==1:
        win_txt="Cross Wins!"
    
    elif Winner==-1:
        win_txt="Circle Wins!"

    else:
        win_txt="Draw"
        x_m=225

    win_img= font.render(win_txt, True, White, Black)
    #message background and border
    pygame.draw.rect(screen, White, (screen_width//2-275, screen_height//2-200,550,150), border_radius=15)
    pygame.draw.rect(screen, Black, (screen_width//2-270, screen_height//2-195,540,140), border_radius=15)
    screen.blit(win_img, (x_m, y_m))

    #play again button
    play_again_txt="Play Again"
    Play_again_img= pygame.font.SysFont(None,60).render(play_again_txt, True, White)
    pygame.draw.rect(screen, White, (x_pm-10, y_pm-10,260,60), border_radius=15)
    pygame.draw.rect(screen, Black, Play_again_rect , border_radius=15)
    screen.blit(Play_again_img, (x_pm, y_pm))



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
        if gameover==False:
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
                check_winner()

    if gameover==True:
        gameover_screen(Winner)
        #playagain
        if event.type==pygame.MOUSEBUTTONDOWN and click==False:
                click=True

        if event.type==pygame.MOUSEBUTTONUP and click == True:
            click=False
            position=pygame.mouse.get_pos()
            if Play_again_rect.collidepoint(position):
                    #reset varriables
                    Winner=0
                    gameover=False
                    flags=np.array([[0,0,0],[0,0,0],[0,0,0]])
                    position=[]
                    player=1
                    
    
    pygame.display.update()
       
pygame.quit()
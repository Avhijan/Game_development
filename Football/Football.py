import pygame
from pygame.locals import *

pygame.init()

screen_width=1000
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Football")
#colors
white=(255,255,255)
black=(0,0,0)
red=(255, 0 ,0)
dark_green=(0,100,0)
light_green=(144,238,144)

#game varriables
center=((screen_width/2,screen_height/2))
pi=3.1415

def draw_field():
    #for background grass
    screen.fill(dark_green)
    for i in range(1,12):
        if i%2 != 0:
            pygame.draw.rect(screen, light_green, (77*i, 0, 80, screen_height))

    #for border
    pygame.draw.rect(screen, white, (10, 10 ,screen_width-20,screen_height-20),10)
    pygame.draw.circle(screen, white, center, 125, 10)
    pygame.draw.line(screen, white, (screen_width/2, 10),(screen_width/2, screen_height-20),10 )

    #for goal borders
    pygame.draw.rect(screen, white, (10, screen_height//2 - 150, 150, 300), 10)
    pygame.draw.rect(screen, white, (screen_width-160, screen_height//2 - 150, 150, 300), 10)


    pygame.draw.arc(screen, white,(160-78, screen_height/2-70, 140, 140), 3*pi/2, pi/2, 10 )
    pygame.draw.arc(screen, white,(screen_width-160-70, screen_height/2-70, 140, 140), pi/2, 3*pi/2, 10 )


class player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rect=Rect(self.x, self.y, 20, 30)

    def draw_player(self):
        pygame.draw.rect(screen, white, self.rect, 8,)
        pygame.draw.circle(screen,white,(self.x+10,self.y-12), 14,7)


#player 
player1 = player(screen_width-800,screen_height-40)
player2 = player(screen_width-200, screen_height-40)

running=True
while running:
    draw_field()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        #draw player
        player1.draw_player()
        player2.draw_player()

        

    pygame.display.update()

pygame.quit()

               

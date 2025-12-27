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
blue=(0,0,255)
skin=(232, 190, 172)
dark_green=(0,100,0)
light_green=(144,238,144)

fpsclock=pygame.time.Clock()
#game varriables
center=((screen_width/2,screen_height/2))
pi=3.1415
fps=30

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

class football:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ball_radius=20
        self.speed_x = 5
        self.speed_y = 5
        self.rect=Rect(self.x, self.y, 20, 30)

    def draw_ball(self):
        pygame.draw.circle(screen, white, (self.rect.x, self.rect.y), self.ball_radius)
        pygame.draw.circle(screen, black, (self.rect.x, self.rect.y), self.ball_radius, 3)
        # x = 8
        # y = 10
        # x1 = self.rect.x - x
        # y1 = self.rect.y 

        # x2 = self.rect.x + x
        # y2 = self.rect.y 

        # x3 = self.rect.x + x
        # y3 = self.rect.y - y

        # x4 = self.rect.x + x/2-0.5
        # y4 = self.rect.y -2*y

        # x5 = self.rect.x - x
        # y5 = self.rect.y - y

        #points=[(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5)]
        #pygame.draw.polygon(screen, black, [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5)])

    def move_ball(self):
            
        #collision detection
            if self.rect.top < screen_height:
                self.speed_y *= -1

            if self.rect.bottom > screen_height:
                self.speed_y *= -1

            if self.rect.right < screen_width:
                self.speed_x *= -1
            
            if self.rect.left > 5:
                self.speed_x *= -1


            #check collision with paddles
            if self.rect.colliderect(player1) or self.rect.colliderect(player2):
                self.speed_x *= -1


            self.rect.x += self.speed_x
        #self.rect.y += self.speed_y
        

class player:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.player_color=color
        self.rect=Rect(self.x, self.y, 20, 35)
        self.player_rect = Rect(self.x, self.y, 20, 20)
        self.player_head = Rect(self.x-3,self.y-26, 28, 28)
        self.speed=4

    def draw_player(self):
        pygame.draw.rect(screen, black, self.rect)
        pygame.draw.rect(screen,self.player_color ,self.player_rect)
        pygame.draw.ellipse(screen, skin, self.player_head, 14)
        pygame.draw.ellipse(screen, black, self.player_head, 1)
        # pygame.draw.circle(screen, skin, (self.x+10,self.y-14), 14)
        # pygame.draw.circle(screen, black, (self.x+10,self.y-14), 14, 1)

    def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.rect.top > 5:
                self.rect.move_ip(0,-1*self.speed)
                self.player_rect.move_ip(0,-1*self.speed)
                self.player_head.move_ip(0, -1*self.speed)
            
            if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
                self.rect.move_ip(0,self.speed)
                self.player_rect.move_ip(0, self.speed)
                self.player_head.move_ip(0, self.speed)

            if key[pygame.K_RIGHT] and self.rect.right < screen_width:
                self.rect.move_ip(self.speed, 0)
                self.player_rect.move_ip(self.speed,0)
                self.player_head.move_ip(self.speed,0)

            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.move_ip(-1*self.speed, 0)
                self.player_rect.move_ip(-1*self.speed,0)
                self.player_head.move_ip(-1*self.speed,0)
                
        
#player 
player1 = player(screen_width-900,screen_height//2, blue)
player2 = player(screen_width-100, screen_height//2, red)
ball = football(screen_width//2, screen_height//2)


running=True
while running:
    fpsclock.tick(fps)
    draw_field()
     #draw player
    player1.draw_player()
    player2.draw_player()
    player1.move_player()

    #draw ball
    ball.draw_ball()
    #move football
    ball.move_ball()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        

    pygame.display.update()

pygame.quit()

               

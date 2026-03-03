import pygame
from pygame.locals import *
import random

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
live_ball=False
score = [0, 0]
goal_message = ""
goal_timer = 0
font = pygame.font.SysFont(None, 60)

def draw_field():
    screen.fill(dark_green)
    for i in range(1,12):
        if i%2 != 0:
            pygame.draw.rect(screen, light_green, (77*i, 0, 80, screen_height))

    pygame.draw.rect(screen, white, (10, 10 ,screen_width-20,screen_height-20),10)
    pygame.draw.circle(screen, white, center, 125, 10)
    pygame.draw.line(screen, white, (screen_width/2, 10),(screen_width/2, screen_height-20),10 )


    pygame.draw.rect(screen, white, (10, screen_height//2 - 150, 150, 300), 10)
    pygame.draw.rect(screen, white, (screen_width-160, screen_height//2 - 150, 150, 300), 10)

    pygame.draw.arc(screen, white,(160-78, screen_height/2-70, 140, 140), 3*pi/2, pi/2, 10 )
    pygame.draw.arc(screen, white,(screen_width-160-70, screen_height/2-70, 140, 140), pi/2, 3*pi/2, 10 )

def draw_scores():
    p1 = font.render(str(score[0]), True, blue)
    p2 = font.render(str(score[1]), True, red)
    screen.blit(p1, (screen_width//2 - 80, 20))
    screen.blit(p2, (screen_width//2 + 50, 20))
    dash = font.render("-", True, white)
    screen.blit(dash, (screen_width//2 - 20, 20))

class football:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ball_radius=20
        self.speed_x = 0
        self.speed_y = 0
        self.rect=Rect(self.x, self.y, 20, 30)
        self.winner=0
        self.friction = 0.97

    def draw_ball(self):
        pygame.draw.circle(screen, white, (self.rect.x, self.rect.y), self.ball_radius)
        pygame.draw.circle(screen, black, (self.rect.x, self.rect.y), self.ball_radius, 3)

    def move_ball(self):

        if self.rect.top < 10:
            self.speed_y = abs(self.speed_y)      

        if self.rect.bottom > screen_height - 10:
            self.speed_y = -abs(self.speed_y)   

        goal_top = screen_height//2 - 150
        goal_bottom = screen_height//2 + 150

        if self.rect.left < 10 and not (goal_top < self.rect.centery < goal_bottom):
            self.speed_x = abs(self.speed_x)      

        if self.rect.right > screen_width - 10 and not (goal_top < self.rect.centery < goal_bottom):
            self.speed_x = -abs(self.speed_x)     


        self.speed_x *= self.friction
        self.speed_y *= self.friction


        if abs(self.speed_x) < 0.2: self.speed_x = 0
        if abs(self.speed_y) < 0.2: self.speed_y = 0

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #check winner
        if self.rect.left < 5:
            self.winner = 2  
        if self.rect.right > 995:
            self.winner = 1  

        return self.winner

    def reset(self):
        self.rect.x = screen_width//2
        self.rect.y = screen_height//2
        self.speed_x = 0
        self.speed_y = 0
        self.winner = 0


class player:
    def __init__(self,x,y,color,playernum):
        self.x=x
        self.y=y
        self.player_color=color
        self.num=playernum
        self.rect=Rect(self.x, self.y, 20, 35)
        self.player_rect = Rect(self.x, self.y, 20, 20)
        self.player_head = Rect(self.x-3,self.y-26, 28, 28)
        self.speed=4

    def draw_player(self):
        pygame.draw.rect(screen, black, self.rect)
        pygame.draw.rect(screen,self.player_color ,self.player_rect)
        pygame.draw.ellipse(screen, skin, self.player_head, 14)
        pygame.draw.ellipse(screen, black, self.player_head, 1)

    def move_player(self):
        key = pygame.key.get_pressed()
        if self.num == 1:
            if key[pygame.K_w] and self.rect.top > 5:
                self.rect.move_ip(0,-1*self.speed)
                self.player_rect.move_ip(0,-1*self.speed)
                self.player_head.move_ip(0, -1*self.speed)
            
            if key[pygame.K_s] and self.rect.bottom < screen_height:
                self.rect.move_ip(0,self.speed)
                self.player_rect.move_ip(0, self.speed)
                self.player_head.move_ip(0, self.speed)

            if key[pygame.K_d] and self.rect.right < screen_width:
                self.rect.move_ip(self.speed, 0)
                self.player_rect.move_ip(self.speed,0)
                self.player_head.move_ip(self.speed,0)

            if key[pygame.K_a] and self.rect.left > 0:
                self.rect.move_ip(-1*self.speed, 0)
                self.player_rect.move_ip(-1*self.speed,0)
                self.player_head.move_ip(-1*self.speed,0)

        if self.num ==2:
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
                
        if self.rect.colliderect(ball.rect):
            dx = ball.rect.centerx - self.rect.centerx
            dy = ball.rect.centery - self.rect.centery
            if abs(dy) < 10: dy = 0 
            dist = (dx**2 + dy**2) ** 0.5
            if dist == 0: dist = 1
            ball.speed_x = (dx / dist) * 7
            ball.speed_y = (dy / dist) * 7

#player 
player1 = player(screen_width-900,screen_height//2, blue, 1)
player2 = player(screen_width-100, screen_height//2, red, 2)
ball = football(screen_width//2, screen_height//2)


running=True
while running:
    fpsclock.tick(fps)
    draw_field()
    draw_scores()
    #draw player
    player1.draw_player()
    player2.draw_player()
    player1.move_player()
    player2.move_player()

    #draw ball
    ball.draw_ball()
    
    winner = ball.move_ball()

    # handle goal
    if winner != 0:
        score[winner - 1] += 1
        goal_message = f"GOAL! Player {winner} scores!"
        goal_timer = fps * 2
        ball.reset()
        player1.rect.topleft = (screen_width-900, screen_height//2)
        player1.player_rect.topleft = (screen_width-900, screen_height//2)
        player1.player_head.topleft = (screen_width-900-3, screen_height//2-26)
        player2.rect.topleft = (screen_width-100, screen_height//2)
        player2.player_rect.topleft = (screen_width-100, screen_height//2)
        player2.player_head.topleft = (screen_width-100-3, screen_height//2-26)

    # draw goal message
    if goal_timer > 0:
        msg = font.render(goal_message, True, (255, 220, 0))
        screen.blit(msg, (screen_width//2 - msg.get_width()//2, screen_height//2 - 30))
        goal_timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    pygame.display.update()

pygame.quit()
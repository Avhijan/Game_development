import pygame
from pygame.locals import*

pygame.init()
screen_width=600
screen_height=500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("__Pong Game__")

fpsclock=pygame.time.Clock()
#define font
font=pygame.font.SysFont('Constantia',30)
#define game varriables
margin=50
Ai_score=0
you_score=0
fps=60
winner=0
live_ball=False
speed_increase=0


#define colors
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
white=(255,255,255)

def show_text(text,font,color,x,y):
    img=font.render(text,True, color)
    screen.blit(img,(x,y))

def Background():
    screen.fill(black)
    pygame.draw.line(screen, white, (0,margin),(screen_width,margin),2)

class paddle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rect= Rect(self.x,self.y, 20, 100)
        self.speed=5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top> margin:
            self.rect.move_ip(0,-1*self.speed)
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0,self.speed)

    def ai(self):
        #to move paddle automatically
        #move down
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)
        #move up
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1*self.speed)

    def draw(self):
        pygame.draw.rect(screen,white,self.rect)

class ball():
    def __init__(self,x,y):
        self.reset(x,y)
       
    def move(self):
        #collision detection
        if self.rect.top < margin:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.speed_y *= -1
        #check collision with paddles
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(Ai_paddle):
            self.speed_x *= -1
        #check for out of bounds
        if self.rect.left < 0:
            self.winner=1
        if self.rect.right > screen_width:
            self.winner=-1
        self.rect.x +=self.speed_x
        self.rect.y +=self.speed_y
        return self.winner
    
    def draw(self):
        pygame.draw.circle(screen,white,(self.rect.x +self.ball_radius, self.rect.y+self.ball_radius), self.ball_radius)

    def reset(self,x,y):
        self.x=x
        self.y=y
        self.ball_radius=8
        self.rect= Rect(self.x,self.y, self.ball_radius*2, self.ball_radius*2)
        self.speed_x=-4
        self.speed_y=4
        self.winner=0 # 1 for player and -1 for Ai

#paddle
player_paddle=paddle(screen_width-40, screen_height//2)
Ai_paddle=paddle(20,screen_height//2)
#pong ball
pong=ball(screen_width-60,screen_height//2-50)

running=True
while running:
    fpsclock.tick(fps)

    Background()
    show_text('Ai:'+str(Ai_score), font, white, 20, 15)
    show_text('You:'+str(you_score),font,white, 450, 15)
    show_text('Speed:' + str(abs(pong.speed_x)),font,white,screen_width//2-100,15 )
    if live_ball==True:
        #move ball
        winner=pong.move()
        speed_increase +=1
        if winner==0:
            #move paddle
            player_paddle.move()
            Ai_paddle.ai()
            #draw ball
            pong.draw()
        else:
            live_ball=False
            if winner==1:
                you_score +=1
            if winner == -1:
                Ai_score +=1
            

    #draw paddles
    player_paddle.draw()
    Ai_paddle.draw()

    #Tutorial for player
    if live_ball==False:
        if winner==0:
            show_text("Click anywhere to start",font, white, 130, screen_height//2 -100)
        if winner==1:
            show_text("Click anywhere to start",font, white, 130, screen_height//2 -100)
            show_text('You scored!!!',font, white, 190, screen_height//2 -50)
        if winner==-1:
            show_text("Click anywhere to start",font, white, 130, screen_height//2 -100)
            show_text('AI scored :(',font, white, 210, screen_height//2 -50)
    
   

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and live_ball==False:
            live_ball=True
            pong.reset(screen_width-60,screen_height//2-50)

    if speed_increase>500:
        speed_increase=0
        if pong.speed_x<0:
            pong.speed_x -=1
        if pong.speed_x>0:
            pong.speed_x +=1
        if pong.speed_y<0:
            pong.speed_y -=1
        if pong.speed_y>0:
            pong.speed_y +=1






    pygame.display.update()
pygame.quit()

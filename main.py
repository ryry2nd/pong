#imports
from cv2 import circle
import pygame, os

#inits
pygame.init()
pygame.font.init()
pygame.mixer.init()

#constents
WIDTH, HEIGHT = 900, 500
FPS = 60
VEL = 5

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# paddle
class Paddle:
    def __init__(self, PWIDTH, PHEIGHT, POS):#initualise the vars
        self.WIDTH = PWIDTH
        self.HEIGHT = PHEIGHT
        self.x = POS[0]
        self.y = POS[1]
    def make_it(self):# makes the paddle
        PADDLE = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(WIN, WHITE, PADDLE)

#ball
class Ball:
    def __init__(self, POS, size):
        self.x = POS[0]
        self.y = POS[1]
        self.size = size
    def make_it(self):
        pygame.draw.circle(WIN, WHITE, (self.x, self.y), self.size)
        

#main funtion
def main():
    #init objects
    PLAYER1 = Paddle(10, 100, (30, HEIGHT // 2 - 50))
    PLAYER2 = Paddle(10, 100, (WIDTH - 40, HEIGHT // 2 - 50))
    BALL = Ball((WIDTH//2,HEIGHT//2), 10)
    
    BALL_VEL = 0

    run = True
    clock = pygame.time.Clock()#defines the clock

    while run:# game loop
        clock.tick(FPS)#fps

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    run = False
        
        keys_pressed = pygame.key.get_pressed()# gets all the keys
        
        if keys_pressed[pygame.K_w] and PLAYER1.y - VEL > 0:# moves player1 up if in bounds
            PLAYER1.y -= VEL
        if keys_pressed[pygame.K_s] and PLAYER1.y + VEL + PLAYER1.HEIGHT < HEIGHT:# moves player1 down if in bounds
            PLAYER1.y += VEL
        if keys_pressed[pygame.K_UP] and PLAYER2.y - VEL > 0:# moves player2 up if in bounds
            PLAYER2.y -= VEL
        if keys_pressed[pygame.K_DOWN] and PLAYER2.y + VEL + PLAYER2.HEIGHT < HEIGHT:# moves player2 down if in bounds
            PLAYER2.y += VEL

        WIN.fill(BLACK)# fills the screen

        #makes the objects
        PLAYER1.make_it()
        PLAYER2.make_it()
        BALL.make_it()
        
        pygame.display.update()# updates the display
        
    pygame.quit()#quits

# if it is being imported run the main
if __name__ == '__main__':
    main()
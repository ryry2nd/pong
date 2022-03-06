#imports
import pygame, os, math, random

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

# paddle object
class Paddle:
    def __init__(self, size, POS):#initualise the vars
        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.x = POS[0]
        self.y = POS[1]
    def make_it(self):# makes the paddle
        PADDLE = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(WIN, WHITE, PADDLE)

#ball object
class Ball:
    #def vars
    xVel = 0
    yVel = 0

    def __init__(self, size, POS):# init vars
        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.x = POS[0]
        self.y = POS[1]
    def make_it(self):#makes the paddle
        BALL = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(WIN, WHITE, BALL)
    def move(self, players):# moves the player
        BALL = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

        # bounces off the walls
        if self.x + self.xVel <= 0 or self.x + self.xVel >= WIDTH - self.WIDTH:
            self.xVel = -self.xVel
        if self.y + self.yVel <= 0 or self.y + self.yVel >= HEIGHT - self.HEIGHT:
            self.yVel = -self.yVel
        
        for player in players:# loops through the paddles
            if BALL.colliderect(pygame.Rect(player.x, player.y, player.WIDTH, player.HEIGHT)):# runs when there is a colision
                self.xVel = -self.xVel# reverses the balls x vel
                self.yVel = -((((player.y + (player.HEIGHT // 2)) - self.y) - 10) // 10)# sets the y level based on where it hits the paddle
                if abs(self.xVel) < 30:# runs when it is below the max sppeed
                    # make the ball faster
                    if self.xVel > 0:
                        self.xVel += 1
                    else:
                        self.xVel -= 1

        #move the ball
        self.x += self.xVel
        self.y += self.yVel
        
#main funtion
def main():
    #init objects
    PLAYER1 = Paddle((20, 100), (60, HEIGHT // 2 - 50))
    PLAYER2 = Paddle((20, 100), (WIDTH - 70, HEIGHT // 2 - 50))
    BALL = Ball((20, 20), (WIDTH//2 - 10, HEIGHT//2 - 10))

    BALL.xVel = -1# default vel

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

        BALL.move((PLAYER1, PLAYER2)) #move the ball

        #makes the objects
        PLAYER1.make_it()
        PLAYER2.make_it()
        BALL.make_it()

        pygame.display.update()# updates the display
        
    pygame.quit()#quits

# if it is being imported run the main
if __name__ == '__main__':
    main()
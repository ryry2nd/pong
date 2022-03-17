"""
defines the ball and paddle classes
"""
#imports
import pygame

#inits
pygame.init()
pygame.font.init()

# paddle object
class Paddle:
    VEL = 6# this is the velocity of the paddle
    #initialise the vars
    def __init__(self, POS):
        self.WIDTH = 20#defines the width
        self.HEIGHT = 100#defines the height
        self.x = POS[0]#defines the xpos
        self.y = POS[1]#defines the ypos

    #moves the paddle
    def move(self, directionIsUp, HEIGHT):
        # runs when it is going up and in bounds
        if directionIsUp and self.y - self.VEL > 0:
            self.y -= self.VEL# moves the paddle
        #runs when it is going down and is in bounds
        elif not(directionIsUp) and self.y + self.VEL + self.HEIGHT < HEIGHT:
            self.y += self.VEL#moves the paddle

    # makes the paddle
    def make_it(self, WIN):
        PADDLE = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(WIN, (255, 255, 255), PADDLE)

#ball object
class Ball:
    #def vars
    xVel = 0
    yVel = 0

    # init vars
    def __init__(self, POS, RES):
        self.size = 20#defines the size
        self.x = POS[0]#defines the xpos
        self.y = POS[1]#defines the ypos
        #defines the screen res
        self.SCRWIDTH = RES[0]
        self.SCRHEIGHT = RES[1]
    #makes the ball
    def make_it(self, WIN):
        pygame.draw.circle(WIN, (255, 255, 255),
            (self.x, self.y), self.size)
    
    #sets up the colision
    def collision(self, players):
        #makes the virtual ball
        BALL = pygame.Rect(self.x, self.y, self.size, self.size)

        # bounces off the walls
        if self.y + self.yVel <= 0 or self.y + self.yVel >= self.SCRHEIGHT - self.size:
            self.yVel = -self.yVel

        for player in players:# loops through the paddles
            if BALL.colliderect(pygame.Rect(player.x, player.y, player.WIDTH, player.HEIGHT)):# runs when there is a colision
                #if player.x == BALL.x:
                #    if player.y < 0:
                #        player.y += 1
                #    else:
                #        player.y -= 1

                self.xVel =- self.xVel# reverses the balls x vel
                self.yVel =- ((((player.y + (player.HEIGHT // 2)) - self.y) - player.WIDTH // 2) // 10)# sets the y level based on where it hits the paddle
                
                # make the ball faster
                if self.xVel > 0:
                    self.xVel += 1
                else:
                    self.xVel -= 1
    
    # moves the ball
    def move(self, players):
        for i in range(abs(self.xVel)):#loops through the ball's xVel and adds 1 to the position
            #sets the colision
            self.collision(players)
    
            #moves the ball's xpos by 1
            if self.xVel > 0:
                self.x += 1
            else:
                self.x -= 1
        
        self.y += self.yVel
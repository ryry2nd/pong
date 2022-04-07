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
        self.rect = pygame.Rect(POS[0], POS[1], 20, 100)#makes the rectangle

    #moves the paddle
    def move(self, directionIsUp, HEIGHT):
        # runs when it is going up and in bounds
        if directionIsUp and self.rect.top > 0:
            self.rect.move_ip(0, -self.VEL)# moves the paddle
        #runs when it is going down and is in bounds
        elif not(directionIsUp) and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.VEL)#moves the paddle

    # draws the paddle
    def make_it(self, WIN):
        pygame.draw.rect(WIN, (255, 255, 255), self.rect)

#ball object
class Ball:
    #def vars
    xVel = 0
    yVel = 0

    # init vars
    def __init__(self, POS):
        self.rect = pygame.Rect(POS[0], POS[1], 20, 20)#makes the rect

    #draws the ball
    def make_it(self, WIN):
        pygame.draw.rect(WIN, (255, 255, 255), self.rect)

    # moves the ball
    def move(self, players, HEIGHT):
        for i in range(abs(self.xVel)):#loops through the ball's xVel and adds 1 to the position
            #sets the colision
            # bounces off the walls
            if self.rect.y + self.yVel <= 0 or self.rect.y + self.yVel >= HEIGHT - self.rect.height:
                self.yVel = -self.yVel

            for player in players:# loops through the paddles
                if self.rect.colliderect(player.rect):# runs when there is a colision
                    self.xVel =- self.xVel# reverses the balls x vel
                    self.yVel =- ((((player.rect.y + (player.rect.height / 2)) - self.rect.y) - player.rect.width / 2) / 10)# sets the y level based on where it hits the paddle
                    
                    # make the ball faster
                    if self.xVel > 0:
                        self.xVel += 1
                    else:
                        self.xVel -= 1
    
            #moves the ball's xpos by 1
            if self.xVel > 0:
                self.rect.x += 1
            else:
                self.rect.x -= 1
        
        self.rect.y += self.yVel
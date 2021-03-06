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
    def move(self, directionIsUp, HEIGHT, BALL, collided):
        #if it collided the top, move the paddle back
        if round(BALL.bottom/10)*10 == round(self.rect.top/10)*10 and collided:
            self.rect.y += self.VEL
        #if it collided the bottom, move the paddle forward
        elif round(BALL.top/10)*10 == round(self.rect.bottom/10)*10 and collided:
            self.rect.y -= self.VEL
        # runs when it is going up and in bounds
        elif directionIsUp and self.rect.top > 0:
            self.rect.y -= self.VEL# moves the paddle
        #runs when it is going down and is in bounds
        elif not(directionIsUp) and self.rect.bottom < HEIGHT:
            self.rect.y += self.VEL#moves the paddle
        
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
        #init vars
        collided = False
        tempRect = self.rect

        for i in range(abs(self.xVel)):#loops through the ball's xVel and adds 1 to the position
            #sets the colision
            # bounces off the walls
            if tempRect.y + self.yVel <= 0 or tempRect.y + self.yVel >= HEIGHT - tempRect.height:
                self.yVel *= -1

            for player in players:# loops through the paddles
                if tempRect.colliderect(player):# runs when there is a colision
                    self.xVel =- self.xVel# reverses the balls x vel
                    # sets the y level based on where it hits the paddle
                    self.yVel =- ((((player.y + (player.height / 2)) - tempRect.y) - player.width / 2) / 10)
                    
                    # make the ball faster
                    if self.xVel > 0:
                        self.xVel += 1
                    else:
                        self.xVel -= 1

                    collided = True#if it collided it sets the variable to true
                    break #breaks out of the for loop
            
            #moves the ball's xpos by 1
            if self.xVel > 0:
                tempRect.x += 1
            else:
                tempRect.x -= 1
        
        tempRect.y += self.yVel# adds the ball to the yVel
        self.rect = tempRect
        
        return collided#returns the velocity
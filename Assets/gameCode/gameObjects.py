import pygame

#inits
pygame.init()
pygame.font.init()

# paddle object
class Paddle:
    VEL = 5
    def __init__(self, size, POS):#initualise the vars
        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.x = POS[0]
        self.y = POS[1]
    def move(self, directionIsUp, HEIGHT):
        if directionIsUp and self.y - self.VEL > 0:
            self.y -= self.VEL
        elif not(directionIsUp) and self.y + self.VEL + self.HEIGHT < HEIGHT:
            self.y += self.VEL
    def make_it(self, WIN):# makes the paddle
        PADDLE = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(WIN, (255, 255, 255), PADDLE)

#ball object
class Ball:
    #def vars
    xVel = 0
    yVel = 0

    def __init__(self, size, POS, res):# init vars
        self.size = size
        self.x = POS[0]
        self.y = POS[1]
        self.SCRWIDTH = res[0]
        self.SCRHEIGHT = res[1]
    def make_it(self, WIN):#makes the paddle
        pygame.draw.circle(WIN, (255, 255, 255), (self.x, self.y), self.size)
    def move(self, players):# moves the player
        BALL = pygame.Rect(self.x, self.y, self.size * (self.xVel / 16), self.size)

        # bounces off the walls
        if self.y + self.yVel <= 0 or self.y + self.yVel >= self.SCRHEIGHT - self.size:
            self.yVel = -self.yVel
        
        for player in players:# loops through the paddles
            if BALL.colliderect(pygame.Rect(player.x, player.y, player.WIDTH, player.HEIGHT)):# runs when there is a colision
                self.xVel = -self.xVel# reverses the balls x vel
                self.yVel = -((((player.y + (player.HEIGHT // 2)) - self.y) - 10) // 10)# sets the y level based on where it hits the paddle

                # make the ball faster
                if self.xVel > 0:
                    self.xVel += 1
                else:
                    self.xVel -= 1

        #move the ball
        self.x += self.xVel
        self.y += self.yVel
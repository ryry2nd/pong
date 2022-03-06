#imports
import pygame, random

#inits
pygame.init()
pygame.font.init()
pygame.mixer.init()

#constents
WIDTH, HEIGHT = 900, 500
FPS = 60
VEL = 5

#fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 100)
WIN_FONT = pygame.font.SysFont('comicsans', 100)

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load('Assets/ball.png'))

# sets the points
p1Points, p2Points = 0, 0

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
        self.size = size
        self.x = POS[0]
        self.y = POS[1]
    def make_it(self):#makes the paddle
        pygame.draw.circle(WIN, WHITE, (self.x, self.y), self.size)
    def move(self, players):# moves the player
        BALL = pygame.Rect(self.x, self.y, self.size, self.size)

        # bounces off the walls
        if self.y + self.yVel <= 0 or self.y + self.yVel >= HEIGHT - self.size:
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

# checks if there is a win
def checkWin():
    win = None

    if p1Points == 7:# if there is a win, set a winner
        win = 'Player1'
    elif p2Points == 7:
        win = 'Player2'
    
    if win:# if there is a win print it out and update the screen
        WIN.fill(BLACK)
        WIN.blit(WIN_FONT.render(win + " wins!", 1, WHITE), (0 + 100, HEIGHT//2 - 50))
        pygame.display.update()
        pygame.time.delay(5000)
    
    return win #returns the winner
        

#main funtion
def main():
    #init vars
    global p1Points, p2Points

    #init objects
    PLAYER1 = Paddle((20, 100), (60, HEIGHT // 2 - 50))
    PLAYER2 = Paddle((20, 100), (WIDTH - 70, HEIGHT // 2 - 50))
    BALL = Ball(20, (WIDTH//2 - 10, HEIGHT//2 - 10))

    run = True
    restart = True
    clock = pygame.time.Clock()#defines the clock

    if p1Points > p2Points:
        BALL.xVel = 3
    elif p1Points < p2Points:
        BALL.xVel = -3
    else:
        BALL.xVel = random.choice([-3,3])# default vel

    while run:# game loop
        clock.tick(FPS)#fps

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False
                restart = False

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    run = False
                    restart = False
        
        keys_pressed = pygame.key.get_pressed()# gets all the keys
        
        if keys_pressed[pygame.K_w] and PLAYER1.y - VEL > 0:# moves player1 up if in bounds
            PLAYER1.y -= VEL
        if keys_pressed[pygame.K_s] and PLAYER1.y + VEL + PLAYER1.HEIGHT < HEIGHT:# moves player1 down if in bounds
            PLAYER1.y += VEL
        if keys_pressed[pygame.K_UP] and PLAYER2.y - VEL > 0:# moves player2 up if in bounds
            PLAYER2.y -= VEL
        if keys_pressed[pygame.K_DOWN] and PLAYER2.y + VEL + PLAYER2.HEIGHT < HEIGHT:# moves player2 down if in bounds
            PLAYER2.y += VEL

        if BALL.x < 0: # if the ball is on the left increace the score by 1 and restart
            p2Points += 1
            run = False
        elif BALL.x + BALL.size > WIDTH:# if the ball is on the right increace the score by 1 and restart
            p1Points += 1
            run = False

        #renders the fonts
        p1Score_text = SCORE_FONT.render(str(p1Points), 1, WHITE)
        p2Score_text = SCORE_FONT.render(str(p2Points), 1, WHITE)

        WIN.fill(BLACK)# fills the screen
        pygame.draw.rect(WIN, WHITE, pygame.Rect(WIDTH//2, 0, 10, HEIGHT))

        BALL.move((PLAYER1, PLAYER2)) #move the ball

        #makes the objects
        PLAYER1.make_it()
        PLAYER2.make_it()
        BALL.make_it()

        #makes the score
        WIN.blit(p1Score_text, ((WIDTH//2) - 100, 0))
        WIN.blit(p2Score_text, ((WIDTH//2 - 50) + 100, 0))

        pygame.display.update()# updates the display
        
        if checkWin():# checkes if there is a winner
            run = False
            restart = False
    
    if restart:# if it is being restarted, restart
        main()
    else:#otherwise, quit
        pygame.quit()

# if it is being imported run the main
if __name__ == '__main__':
    main()
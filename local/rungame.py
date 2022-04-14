"""
runs the local game
"""
#imports
from tkinter import Misc
import pygame, random, sys, threading
from Assets.gameCode.game.gameObjects import Paddle, Ball
from Assets.gameCode.game.settings import *

#inits
pygame.init()
pygame.font.init()

#fonts
SCORE_FONT = Fonts.SCORE_FONT
WIN_FONT = Fonts.WIN_FONT

# init vars
p1Points, p2Points = 0, 0
runThread = True

# checks if there is a win
def checkWin(WIN, HEIGHT, ballT, displayThread):
    global runThread
    win = None

    if p1Points == 7:# if there is a win, set a winner
        win = 'Player1'
    elif p2Points == 7:
        win = 'Player2'
    
    if win:# if there is a win print it out and update the screen
        # stops the thread
        runThread = False
        ballT.join()
        displayThread.join()
        WIN.fill((0, 0, 0))
        WIN.blit(WIN_FONT.render(win + " wins!", 1, (255, 255, 255)), (0 + 100, HEIGHT/2 - 50))
        pygame.display.update()
        pygame.time.delay(3000)
    
    return win #returns the winner

#restarts the points
def restartPoints():
    global p1Points, p2Points, runThread
    p1Points, p2Points = 0, 0
    runThread = True

#updates the display
def updateDisplay(WIN, RES, objects):
    #renders the fonts
    p1Score_text = SCORE_FONT.render(str(p1Points), 1, (255, 255, 255))
    p2Score_text = SCORE_FONT.render(str(p2Points), 1, (255, 255, 255))

    #makes the background
    WIN.fill((0, 0, 0))
    pygame.draw.rect(WIN, (255, 255, 255), (RES[0]/2, 0, 10, RES[1]))

    #makes the objects
    objects[0].make_it(WIN)
    objects[1].make_it(WIN)
    objects[2].make_it(WIN)

    #makes the score
    WIN.blit(p1Score_text, (RES[0] / 2 - 60, 0))
    WIN.blit(p2Score_text, (RES[0] / 2 + 20, 0))

    pygame.display.update()# updates the display

#defines the display thread
def updateDisplayThread(WIN, RES, FPS, objects):
    #init vars
    clock = pygame.time.Clock()

    #game loop
    while runThread:
        clock.tick(FPS)#fps
        updateDisplay(WIN, RES, objects)#update the display

#main function
def main(WIN, RES, FPS):
    #get globals
    global p1Points, p2Points, runThread

    #def width and height
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #init objects
    PLAYER1 = Paddle((60, HEIGHT / 2 - 50))
    PLAYER2 = Paddle((WIDTH - 70, HEIGHT / 2 - 50))
    BALL = Ball((WIDTH/2 - 10, HEIGHT/2 - 10))
    
    #init thread
    displayThread = threading.Thread(target=updateDisplayThread, 
        args=(WIN, (WIDTH, HEIGHT), FPS, (PLAYER1, PLAYER2, BALL), ))
    
    #start thread
    displayThread.start()

    #init vars
    clock = pygame.time.Clock()#defines the clock

    while True:# runs every round
        #reset vars
        PLAYER1.rect.y = HEIGHT / 2 - 50
        PLAYER2.rect.y = HEIGHT / 2 - 50
        BALL.rect.x = WIDTH / 2 - 10
        BALL.rect.y = HEIGHT / 2 - 10
        BALL.yVel = 0

        #gets the ball starting vel
        if p1Points > p2Points:
            BALL.xVel = 3
        elif p1Points < p2Points:
            BALL.xVel = -3
        else:
            BALL.xVel = random.choice([-3,3])

        ballT = threading.Thread(target=BALL.move, args=((PLAYER1.rect, PLAYER2.rect), HEIGHT, ))#inits the ball move thread
        ballT.start()#starts the ball move thread

        while True:#runs every frame

            clock.tick(Miscellaneous.TICKSPEED)#fps

            for event in pygame.event.get():#loops through the events
                if event.type == pygame.QUIT:#if it is quit, quit
                    runThread = False
                    displayThread.join()
                    ballT.join()
                    sys.exit()

                if event.type == pygame.KEYDOWN:# runs when a key is pressed
                    if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                        runThread = False
                        displayThread.join()
                        ballT.join()
                        restartPoints()
                        return False

            keys_pressed = pygame.key.get_pressed()# gets all the keys

            collided = ballT.join()
            ballT = threading.Thread(target=BALL.move, args=((PLAYER1.rect, PLAYER2.rect), HEIGHT, ))#inits the ball move thread
            ballT.start()#starts the ball move thread

            if keys_pressed[Key_Binds.PLAYER1_UP]:# moves player1 up if in bounds
                PLAYER1.move(True, HEIGHT, BALL.rect, collided)
            if keys_pressed[Key_Binds.PLAYER1_DOWN]:# moves player1 down if in bounds
                PLAYER1.move(False, HEIGHT, BALL.rect, collided)
            if keys_pressed[Key_Binds.PLAYER2_UP]:# moves player2 up if in bounds
                PLAYER2.move(True, HEIGHT, BALL.rect, collided)
            if keys_pressed[Key_Binds.PLAYER2_DOWN]:# moves player2 down if in bounds
                PLAYER2.move(False, HEIGHT, BALL.rect, collided)
            

            if BALL.rect.left < 0: # if the ball is on the left increase the score by 1 and restart
                p2Points += 1
                break
            elif BALL.rect.right > WIDTH:# if the ball is on the right increase the score by 1 and restart
                p1Points += 1
                break

        if checkWin(WIN, HEIGHT, ballT, displayThread):# checks if there is a winner
            #restarts the points
            restartPoints()
            break
    return True
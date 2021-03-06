"""
runs the client code
"""
#imports
import pygame, sys, threading
from online.client.network import Network
from Assets.gameCode.errors import error
from online import getLocalIp
from Assets.gameCode.gui.countDown import countDown
from Assets.gameCode.game.settings import *
#inits
pygame.init()
pygame.font.init()

#constents
IP_ADDRESS = getLocalIp.main()
attributes = {"points": [0, 0], "yourP": -500, "otherP": -500, "ball": [-500, 0]}
runThread = True

#fonts
SCORE_FONT = Fonts.SCORE_FONT
WIN_FONT = Fonts.WIN_FONT
PRINT_IP_FONT = Fonts.PRINT_IP_FONT

#prints who won
def win(WIN, winner, HEIGHT):
    WIN.fill((0, 0, 0))
    WIN.blit(WIN_FONT.render(winner + " wins!", 1, (255, 255, 255)), (0 + 100, HEIGHT/2 - 50))
    pygame.display.update()
    pygame.time.delay(3000)

def updateDisplay(WIN, RES, playersXPos):
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #renders the fonts
    p1Score_text = SCORE_FONT.render(str(attributes["points"][0]), 1, (255, 255, 255))
    p2Score_text = SCORE_FONT.render(str(attributes["points"][1]), 1, (255, 255, 255))

    #sets up the screen
    WIN.fill((0, 0, 0))
    pygame.draw.rect(WIN, (255, 255, 255), (WIDTH/2, 0, 10, HEIGHT))

    #makes the score
    WIN.blit(p1Score_text, (WIDTH/2-55, 0))
    WIN.blit(p2Score_text, (WIDTH/2+20, 0))
    
    #makes the objects
    pygame.draw.rect(WIN, (255, 255, 255), (playersXPos[0], attributes["yourP"], 20, 100))
    pygame.draw.rect(WIN, (255, 255, 255), (playersXPos[1], attributes["otherP"], 20, 100))
    pygame.draw.rect(WIN, (255, 255, 255), (attributes["ball"][0], attributes["ball"][1], 20, 20))

    pygame.display.update()# updates the display

#defines the display thread
def updateDisplayThread(WIN, RES, FPS, objectsXPos):
    #init vars
    clock = pygame.time.Clock()

    #game loop
    while runThread:
        clock.tick(FPS)#fps
        if type(attributes) != bool and type(attributes) != str and type(attributes) != int:# if attrobutes is not any of these values, update the screen
            updateDisplay(WIN, RES, objectsXPos)#update the display

#main function
def main(WIN, RES, FPS, IP):
    global attributes, runThread
    #def width and height
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #inits Network
    n = Network(IP, RES)

    #gets the objects
    initObject = n.getP()
    if not initObject:# if it returned false show the ip not found screen
        error.main(WIN, "Ip not found")
        return # goes back to the home screen
    
    #gets the x position of both players
    p1XPos = initObject[0]
    p2XPos = initObject[1]

    #init vars
    connecting = (p1XPos == 60)# is true if it is player 1
    clock = pygame.time.Clock()#defines the clock

    #renders when it needs to print the ip
    print_ip_text = PRINT_IP_FONT.render("The IP is: " + IP_ADDRESS, 1, (255, 255, 255))

    #the connection screen
    while connecting:
        clock.tick(FPS)#fps
        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                n.send(True)#tells the server to quit
                sys.exit()

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    n.send(True)#tells the server to quit
                    return

        #makes the screen
        WIN.fill((0, 0, 0))
        WIN.blit(print_ip_text, (0, 100))
        pygame.display.update()

        #asks if player 2 has joined yet
        connecting = n.send()

    #counts down
    WIN.fill((0, 0, 0))
    pygame.display.update()
    countDown(WIN, WIDTH, HEIGHT)
    

    displayThread = threading.Thread(target=updateDisplayThread, args=(WIN, RES, FPS, (p1XPos, p2XPos), ))#inits the display thread

    displayThread.start()#starts the display thread

    while True:# game loop
        moveUp = None#restarts the move Up variable
        clock.tick(Miscellaneous.TICKSPEED)#fps

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                runThread = False
                displayThread.join()
                runThread = True
                sys.exit()

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    runThread = False
                    displayThread.join()
                    runThread = True
                    return

        #sends the y position and returns the attributes
        keys_pressed = pygame.key.get_pressed()# gets all the keys
        
        if keys_pressed[Key_Binds.PLAYER1_UP]:# moves player1 up if in bounds
            moveUp = True
        elif keys_pressed[Key_Binds.PLAYER1_DOWN]:# moves player1 down if in bounds
            moveUp = False

        attributes = n.send(moveUp)# sends if it is moveing up and receves the data

        #if it is 1 then player 1 wins
        if attributes == 1:
            runThread = False
            displayThread.join()
            runThread = True
            win(WIN, "player1", HEIGHT)
            runThread = False
            displayThread.join()
            runThread = True
            break
        # if it is 2 then player 2 wins
        elif attributes == 2:
            runThread = False
            displayThread.join()
            runThread = True
            win(WIN, "player2", HEIGHT)
            break
        # if it is exit then exit
        elif attributes == 0:
            runThread = False
            displayThread.join()
            runThread = True
            break
    
    attributes = {"points": [0, 0], "yourP": -500, "otherP": -500, "ball": [-500, 0]}#sets the attrobutes to their defult value
"""
runs the client code
"""
#imports
import pygame, socket
from online.client.network import Network
from Assets.gameCode.errors import error
from online import getLocalIp
from Assets.gameCode.game.settings import Settings
#inits
pygame.init()
pygame.font.init()

#constents
IP_ADDRESS = getLocalIp.main()

#fonts
SCORE_FONT = pygame.font.SysFont(Settings.FONTNAME, 100)
WIN_FONT = pygame.font.SysFont(Settings.FONTNAME, 100)
PRINT_IP_FONT = pygame.font.SysFont(Settings.FONTNAME, 75)

#prints who won
def win(WIN, winner, HEIGHT):
    WIN.fill((0, 0, 0))
    WIN.blit(WIN_FONT.render(winner + " wins!", 1, (255, 255, 255)), (0 + 100, HEIGHT//2 - 50))
    pygame.display.update()
    pygame.time.delay(3000)


#main function
def main(WIN, RES, FPS, IP):
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
    run = True
    connecting = (p1XPos == 60)# is true if it is player 1
    clock = pygame.time.Clock()#defines the clock

    #renders when it needs to print the ip
    print_ip_text = PRINT_IP_FONT.render("The IP is: " + IP_ADDRESS, 1, (255, 255, 255))

    #the connection screen
    while connecting:
        clock.tick(FPS)#fps
        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False
                n.send(True)#tells the server to quit
                pygame.quit()
                exit()

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

    #delays the screen
    WIN.fill((0, 0, 0))
    pygame.display.update()
    pygame.time.delay(2000)
    
    while run:# game loop
        moveUp = None#restarts the move Up variable
        clock.tick(FPS)#fps

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    return

        #sends the y position and returns the atrobutes
        keys_pressed = pygame.key.get_pressed()# gets all the keys
        
        if keys_pressed[pygame.K_w]:# moves player1 up if in bounds
            moveUp = True
        elif keys_pressed[pygame.K_s]:# moves player1 down if in bounds
            moveUp = False

        atrobutes = n.send(moveUp)# sends if it is moveing up and receves the data

        #if it is 1 then player 1 wins
        if atrobutes == 1:
            win(WIN, "player1", HEIGHT)
            break
        # if it is 2 then player 2 wins
        elif atrobutes == 2:
            win(WIN, "player2", HEIGHT)
            break
        # if it is exit then exit
        elif atrobutes == 0:
            break

        #renders the fonts
        p1Score_text = SCORE_FONT.render(str(atrobutes["points"][0]), 1, (255, 255, 255))
        p2Score_text = SCORE_FONT.render(str(atrobutes["points"][1]), 1, (255, 255, 255))

        #sets up the screen
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH//2, 0, 10, HEIGHT))

        #makes the score
        WIN.blit(p1Score_text, ((WIDTH//2) - 100, 0))
        WIN.blit(p2Score_text, ((WIDTH//2 - 50) + 100, 0))

        #makes the objects
        pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(p1XPos, atrobutes["yourP"], 20, 100))
        pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(p2XPos, atrobutes["otherP"], 20, 100))
        pygame.draw.circle(WIN, (255, 255, 255), (atrobutes["ball"][0], atrobutes["ball"][1]), 20)

        pygame.display.update()# updates the display
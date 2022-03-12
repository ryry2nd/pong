#imports
import pygame, socket
from threading import Thread
import local.rungame as single
from online import getLocalIp
import online.client.runClient as client
import online.server.runServer as server
import online.client.getServer as getServer

#inits
pygame.init()
pygame.font.init()

#fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 40)

#constints
WIDTH, HEIGHT = 900, 500
FPS = 60

#set window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

#defines what happens when you click a window
def clickWindow(WIN, POS, l1, l2=""):
    x = POS[0]
    y = POS[1]

    rectangle = pygame.Rect(x, y, 100, 100)#makes a rectangle
    singleplayer_text = [SCORE_FONT.render(l1, 1, (255, 255, 255)), 
        SCORE_FONT.render(l2, 1, (255, 255, 255))]#renders the text

    pygame.draw.rect(WIN, (0, 0, 0), rectangle)#draws the rectangle
    WIN.blit(singleplayer_text[0], (x,y))#draws the text
    WIN.blit(singleplayer_text[1], (x,y+50))

    #if the box is clicked, return True
    if pygame.mouse.get_pressed()[0] and rectangle.collidepoint(pygame.mouse.get_pos()):
        return True

#main funtion 
def main():
    run = True
    clock = pygame.time.Clock()#defines a clock

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    run = False

        WIN.fill((255, 255, 255))# fills the screen

        #if the box is clicked, start a local game
        if clickWindow(WIN, (100, 100), "Local", "Game"):
            single.main(WIN, (WIDTH, HEIGHT), FPS)
        #if the box is clocked go to the find a game code
        elif clickWindow(WIN, (300, 100), "Find a", "Game"):
            IP = getServer.main(WIN, (WIDTH, HEIGHT), FPS)#askes for the ip
            if IP:
                client.main(WIN, (WIDTH, HEIGHT), FPS, IP)# finds the ip
        #if the box is clicked make a server
        elif clickWindow(WIN, (500, 100), "Make a", "Server"):
            #define the thread
            t1 = Thread(target=server.main, args=((WIDTH, HEIGHT), ))
            t1.start()#start the thread
            #join the server with the ip
            client.main(WIN, (WIDTH, HEIGHT), FPS, getLocalIp.main())
            t1.join()

        
        pygame.display.update()#update the display
    
    pygame.quit()

#if the code is not being imported run the code
if __name__ == '__main__':
    main()
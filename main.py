"""
loads the gui
"""
#imports
import pygame, os, time
from threading import Thread
import local.rungame as single
from online import getLocalIp
import online.client.runClient as client
import online.server.runServer as server
import online.client.getServer as getServer
from Assets.gameCode.gui.countDown import countDown
from Assets.gameCode.gui.clickWindow import clickWindow
from Assets.gameCode.gui.restartButton import restartButton

#inits
pygame.init()
pygame.font.init()

#constints
WIDTH, HEIGHT = 900, 500
FPS = 60

#set window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'textures', 'icon.png')))

#main function 
def main():
    run = True
    clock = pygame.time.Clock()#defines a clock
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False

            elif event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    run = False

        WIN.fill((0, 0, 0))# fills the screen

        #if the box is clicked, start a local game
        if clickWindow(WIN, (100, 100), "Local", "Game"):
            countDown(WIN, WIDTH, HEIGHT)# counts down
            allow = single.main(WIN, (WIDTH, HEIGHT), FPS)# starts the game
            while allow and restartButton(WIN, (WIDTH, HEIGHT), FPS):# if the person clicked restart, restart
                countDown(WIN, WIDTH, HEIGHT)# counts down
                allow = single.main(WIN, (WIDTH, HEIGHT), FPS)# starts the game
            pygame.time.delay(1000)
            
        #if the box is clocked go to the find a game code
        elif clickWindow(WIN, (300, 100), "Join a", "Server"):
            IP = getServer.main(WIN, (WIDTH, HEIGHT), FPS)#asks for the ip
            if IP:
                client.main(WIN, (WIDTH, HEIGHT), FPS, IP)# finds the ip
        #if the box is clicked make a server
        elif clickWindow(WIN, (500, 100), "Be a", "Server"):
            #define the thread
            t1 = Thread(target=server.main, args=((WIDTH, HEIGHT), ))
            t1.start()#start the thread
            #join the server with the ip
            
            connected = False
            cnt=0
            #the server may not be ready yet so loop for 5 seconds until connection if not bomb out
            while not connected:
                try:
                    cnt+=1
                    client.main(WIN, (WIDTH, HEIGHT), FPS, getLocalIp.main())
                    connected = True
                except ConnectionRefusedError:
                    if cnt > 5:
                        raise
                    time.sleep(1)
                
            t1.join()# joins the server thread

        
        pygame.display.update()#update the display
    
    pygame.quit()# quits pygame

#if the code is not being imported run the code
if __name__ == '__main__':
    main()
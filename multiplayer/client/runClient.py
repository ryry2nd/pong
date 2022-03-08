#imports
import pygame, socket
from multiplayer.client.network import Network
from multiplayer.client import getServer

#inits
pygame.init()
pygame.font.init()

#fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 100)
WIN_FONT = pygame.font.SysFont('comicsans', 100)

#main funtion
def main(WIN, RES, FPS, IP = socket.gethostbyname(socket.gethostname())):
    #if not IP:
    #    IP = getServer.main(WIN, RES, FPS)
    #def width and height
    WIDTH = RES[0]
    HEIGHT = RES[1]

    n = Network(IP)
    p = n.getP()

    run = True
    restart = True
    clock = pygame.time.Clock()#defines the clock

    while run:# game loop
        clock.tick(FPS)#fps

        atrobutes = n.send(p)

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    run = False
                    restart = False
        
        keys_pressed = pygame.key.get_pressed()# gets all the keys
        
        if keys_pressed[pygame.K_w]:# moves player1 up if in bounds
            p.move(True, HEIGHT)
        if keys_pressed[pygame.K_s]:# moves player1 down if in bounds
            p.move(False, HEIGHT)

        #renders the fonts
        p1Score_text = SCORE_FONT.render(str(atrobutes["points"][0]), 1, (255, 255, 255))
        p2Score_text = SCORE_FONT.render(str(atrobutes["points"][1]), 1, (255, 255, 255))

        WIN.fill((0, 0, 0))# fills the screen
        pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH//2, 0, 10, HEIGHT))

        #makes the score
        WIN.blit(p1Score_text, ((WIDTH//2) - 100, 0))
        WIN.blit(p2Score_text, ((WIDTH//2 - 50) + 100, 0))

        p.make_it(WIN)
        atrobutes["otherP"].make_it(WIN)

        pygame.display.update()# updates the display
    
    if restart:# if it is being restarted, restart
        main(WIN, (WIDTH, HEIGHT), FPS, IP)
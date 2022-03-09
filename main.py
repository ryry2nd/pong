#imports
import pygame, socket, sys
from threading import Thread
import local.rungame as single
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

    rectangle = pygame.Rect(x, y, 100, 100)
    singleplayer_text = [SCORE_FONT.render(l1, 1, (255, 255, 255)), 
        SCORE_FONT.render(l2, 1, (255, 255, 255))]

    pygame.draw.rect(WIN, (0, 0, 0), rectangle)
    WIN.blit(singleplayer_text[0], (x,y))
    WIN.blit(singleplayer_text[1], (x,y+50))

    if pygame.mouse.get_pressed()[0] and rectangle.collidepoint(pygame.mouse.get_pos()):
        return True

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False

            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    run = False

        WIN.fill((255, 255, 255))# fills the screen

        if clickWindow(WIN, (100, 100), "Local", "Game"):
            single.main(WIN, (WIDTH, HEIGHT), FPS)
        if clickWindow(WIN, (300, 100), "Find a", "Game"):
            IP = getServer.main(WIN, (WIDTH, HEIGHT), FPS)
            if IP:
                client.main(WIN, (WIDTH, HEIGHT), FPS, IP)
        if clickWindow(WIN, (500, 100), "Make a", "Server"):
            t1 = Thread(target=server.main, args=((WIDTH, HEIGHT), ))
            t1.start()
            client.main(WIN, (WIDTH, HEIGHT), FPS, socket.gethostbyname(socket.gethostname()))

        pygame.display.update()
    
    pygame.quit()

if __name__ == '__main__':
    main()
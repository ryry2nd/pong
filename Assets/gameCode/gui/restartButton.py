"""
makes the restart button
"""
#imports
from Assets.gameCode.gui.clickWindow import clickWindow
import pygame, sys

#defines the restart button
def restartButton(WIN, RES, FPS):
    #defines the width and height
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #init vars
    clock = pygame.time.Clock()#defines a clock

    #game loop
    while True:
        clock.tick(FPS)# fps
        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                sys.exit()

            elif event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    break

        WIN.fill((0, 0, 0))# fills the screen

        if clickWindow(WIN, (100, 100), "Restart"):# if restart was clicked, restart
            return True
        if clickWindow(WIN, (300, 100), "Go", "Back"):# if back was clicked, go back
            return False
        
        pygame.display.update()# updates the display
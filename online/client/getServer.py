"""
gets the server
"""
#imports
import pygame
from Assets.gameCode.gui import inputIp
from Assets.gameCode.game.settings import *

#inits
pygame.init()
pygame.font.init()

#fonts
SERVER_TEXT = Fonts.SERVER_FONT.render(
    str("Chose the IP of the player you want to join"), 1, (255, 255, 255))

#defines main function
def main(WIN, RES, FPS):
    inputL = inputIp.InputIp(RES)#inits the ip class

    #defines the height
    HEIGHT = RES[1]

    #define vars
    run = True
    clock = pygame.time.Clock()

    #game loop
    while run:
        clock.tick(FPS)#fps

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    return False
                elif event.key == pygame.K_RETURN:# if return is pressed return the letters
                    return inputIp.ip
                else:#otherwise add the key
                    inputL.addkey(event.key)

        WIN.fill((0, 0, 0))#fill the screen

        #adds the text
        WIN.blit(SERVER_TEXT, (0, HEIGHT/2 - 100))
        inputL.placeText(WIN, (0, HEIGHT/2 - 200))

        pygame.display.update()#updates the display
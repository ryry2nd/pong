"""
prints the error given
"""
#imports
from Assets.gameCode.game.settings import Settings
import pygame


#defines main code
def main(WIN, error):
    ERROR_TEXT = Settings.Fonts.ERROR_FONT.render(error, 1, (255, 255, 255))#renders based on the error
    WIN.fill((0, 0, 0))#fills the screen
    WIN.blit(ERROR_TEXT, (0,0))#makes the text
    pygame.display.update()#updates the display
    pygame.time.delay(5000)#waits 5 seconds
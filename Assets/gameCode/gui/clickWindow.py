"""
defines what happions when you click a window
"""
#imports
import pygame
from Assets.settings import Settings

#inits
pygame.init()
pygame.font.init()

#fonts
SCORE_FONT = pygame.font.SysFont(Settings.FONTNAME, 40)

#defines what happens when you click a window
def clickWindow(WIN, POS, l1, l2=""):
    # gets the x and y position
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
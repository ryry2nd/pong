import pygame
class Settings(object):
    def __init__(self):
        pass
    """ 
    Blippo Bold was the original font for pong
    or so the internet tells me
    """

    FONT_FILE = 'Assets/Blippo Bold.ttf' 
    SCORE_FONT_FILE = 'Assets/vt323.regular.ttf'
    COUNTDOWN_FONT = pygame.font.Font(SCORE_FONT_FILE, 200)
    PRINT_IP_FONT = pygame.font.Font(FONT_FILE, 30)
    ERROR_FONT = pygame.font.Font(FONT_FILE, 20) 
    DEFAULT_FONT = pygame.font.Font(FONT_FILE, 30)
    SCORE_FONT = pygame.font.Font(SCORE_FONT_FILE, 100)
    WIN_FONT = pygame.font.Font(FONT_FILE, 30)
    SERVER_FONT = pygame.font.Font(FONT_FILE, 20)
    INPUT_FONT = pygame.font.Font(FONT_FILE, 30)
    


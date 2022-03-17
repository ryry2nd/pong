"""
defines the settings
"""
#imports
import pygame, os

""" 
Blippo Bold was the original font for pong
or so the internet tells me
"""

#defines fonts
class Fonts:
    FONT_FILE = os.path.join('Assets', 'fonts', 'Blippo Bold.ttf')
    SCORE_FONT_FILE = os.path.join('Assets', 'fonts', 'vt323.regular.ttf')
    COUNTDOWN_FONT = pygame.font.Font(SCORE_FONT_FILE, 200)
    PRINT_IP_FONT = pygame.font.Font(FONT_FILE, 50)
    ERROR_FONT = pygame.font.Font(FONT_FILE, 20) 
    DEFAULT_FONT = pygame.font.Font(FONT_FILE, 30)
    SCORE_FONT = pygame.font.Font(SCORE_FONT_FILE, 100)
    WIN_FONT = pygame.font.Font(FONT_FILE, 100)
    SERVER_FONT = pygame.font.Font(FONT_FILE, 20)
    INPUT_FONT = pygame.font.Font(FONT_FILE, 30)

#defines the key binds
class Key_Binds:
    PLAYER1_UP = pygame.K_w
    PLAYER1_DOWN = pygame.K_s
    PLAYER2_UP = pygame.K_UP
    PLAYER2_DOWN = pygame.K_DOWN

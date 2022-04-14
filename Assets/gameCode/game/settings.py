"""
defines the settings
"""
#imports
import pygame, os, json

""" 
Blippo Bold was the original font for pong
or so the internet tells me
"""

#files
SETTINGS_FILE = json.load(open("settings.json"))
FONT_FILE = os.path.join('Assets', 'fonts', 'Blippo Bold.ttf')
SCORE_FONT_FILE = os.path.join('Assets', 'fonts', 'vt323.regular.ttf')

#defines fonts
class Fonts:
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
    PLAYER1_UP = SETTINGS_FILE["keyBinds"]["player1Up"]
    PLAYER1_DOWN = SETTINGS_FILE["keyBinds"]["player1Down"]
    PLAYER2_UP = SETTINGS_FILE["keyBinds"]["player2Up"]
    PLAYER2_DOWN = SETTINGS_FILE["keyBinds"]["player2Down"]

#defines the other variables
class Miscellaneous:
    FPS = SETTINGS_FILE["miscellaneous"]["FPS"]
    WIDTH, HEIGHT = SETTINGS_FILE["miscellaneous"]["WIDTH"], SETTINGS_FILE["miscellaneous"]["HEIGHT"]
    PORT = SETTINGS_FILE["miscellaneous"]["PORT"]
    TICKSPEED = SETTINGS_FILE["miscellaneous"]["tickSpeed"]
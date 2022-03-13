"""
counts down
"""
#imports
from Assets.gameCode.game.settings import Settings
import pygame

#defines the countdown function
def countDown(WIN, WIDTH, HEIGHT):
    for i in range(3, 0, -1):# loops down
        WIN.fill((0, 0, 0))# fills the screen
        WIN.blit(Settings.Fonts.COUNTDOWN_FONT.render(str(i), 1, (255, 255, 255)), (WIDTH/2, HEIGHT/2 - 50))# places the text
        pygame.display.update()
        pygame.time.delay(1000)
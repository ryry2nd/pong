import pygame

ERROR_FONT = pygame.font.SysFont('comicsans', 50)

def main(WIN, error):
    ERROR_TEXT = ERROR_FONT.render(error, 1, (0, 0, 0))
    WIN.fill((255, 255, 255))
    WIN.blit(ERROR_TEXT, (0,0))

    pygame.display.update()
    pygame.time.delay(5000)
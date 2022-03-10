import pygame
from online.client.inputletters import InputLetters

pygame.init()
pygame.font.init()

#fonts
SERVER_TEXT = pygame.font.SysFont('comicsans', 50).render(
    str("Chose the IP of the player you want to join"), 1, (0, 0, 0))

def main(WIN, RES, FPS):
    inputL = InputLetters(RES)
    
    WIDTH = RES[0]
    HEIGHT = RES[1]

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    return False
                elif event.key == pygame.K_RETURN:
                    return inputL.letters
                else:
                    inputL.addkey(event.key)

        WIN.fill((255, 255, 255))
        WIN.blit(SERVER_TEXT, (0, HEIGHT//2 - 100))
        inputL.placeText(WIN, (0, HEIGHT//2 - 200))

        pygame.display.update()
import pygame
pygame.init()
pygame.font.init()

#inputletters
INPUT_FONT = pygame.font.SysFont('comicsans', 100)

class InputLetters:
    letters = []
    def __init__(self, res):
        self.WIDTH = res[0]
        self.HEIGHT = res[1]
    def placeText(self, WIN, RES):
        text = ""
        for i in self.letters:
            text += i
            
        return WIN.blit(INPUT_FONT.render(str(text), 
            1, (0, 0, 0)), RES)
    def addkey(self, keys):
        if keys[pygame.K_BACKSPACE]:
            self.letters.pop()
        else:
            pass
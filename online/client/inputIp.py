#imports
import pygame

#init
pygame.init()
pygame.font.init()

#inputletters
INPUT_FONT = pygame.font.SysFont('comicsans', 100)

#defines the input letters class
class InputIp:
    ip = ""# defines the ip string
    #init
    def __init__(self, res):
        #defines the resolution
        self.WIDTH = res[0]
        self.HEIGHT = res[1]
    #places the text on the screen
    def placeText(self, WIN, RES):
        WIN.blit(INPUT_FONT.render(str(self.letters), 
            1, (0, 0, 0)), RES)
    #adds a key
    def addkey(self, keys):
        # if backspace is pressed remove the last number
        if keys == pygame.K_BACKSPACE and self.letters != []:
            self.letters = self.letters[0:len(self.letters)-1]
        else:
            #adds a number or period if it is pressed
            if keys == pygame.K_0:
                self.letters += "0"
            elif keys == pygame.K_1:
                self.letters += "1"
            elif keys == pygame.K_2:
                self.letters += "2"
            elif keys == pygame.K_3:
                self.letters += "3"
            elif keys == pygame.K_4:
                self.letters += "4"
            elif keys == pygame.K_5:
                self.letters += "5"
            elif keys == pygame.K_6:
                self.letters += "6"
            elif keys == pygame.K_7:
                self.letters += "7"
            elif keys == pygame.K_8:
                self.letters += "8"
            elif keys == pygame.K_9:
                self.letters += "9"
            elif keys == pygame.K_PERIOD:
                self.letters += "."
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
        WIN.blit(INPUT_FONT.render(str(self.ip), 
            1, (0, 0, 0)), RES)
    #adds a key
    def addkey(self, keys):
        # if backspace is pressed remove the last number
        if keys == pygame.K_BACKSPACE and self.ip != []:
            self.ip = self.ip[0:len(self.ip)-1]
        else:
            #adds a number or period if it is pressed
            if keys == pygame.K_0:
                self.ip += "0"
            elif keys == pygame.K_1:
                self.ip += "1"
            elif keys == pygame.K_2:
                self.ip += "2"
            elif keys == pygame.K_3:
                self.ip += "3"
            elif keys == pygame.K_4:
                self.ip += "4"
            elif keys == pygame.K_5:
                self.ip += "5"
            elif keys == pygame.K_6:
                self.ip += "6"
            elif keys == pygame.K_7:
                self.ip += "7"
            elif keys == pygame.K_8:
                self.ip += "8"
            elif keys == pygame.K_9:
                self.ip += "9"
            elif keys == pygame.K_PERIOD:
                self.ip += "."
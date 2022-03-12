"""
defines the input letters class
"""
#imports
import pygame

#init
pygame.init()
pygame.font.init()

#inputletters
INPUT_FONT = pygame.font.SysFont('comicsans', 100)

ip = "192.168."# defines the ip string

#defines the input letters class
class InputIp:
    #init
    def __init__(self, res):
        #defines the resolution
        self.WIDTH = res[0]
        self.HEIGHT = res[1]
    #places the text on the screen
    def placeText(self, WIN, RES):
        WIN.blit(INPUT_FONT.render(ip, 
            1, (255, 255, 255)), RES)
    #adds a key
    def addkey(self, keys):
        global ip
        # if backspace is pressed remove the last number
        if keys == pygame.K_BACKSPACE and ip != []:
            ip = ip[0:len(ip)-1]
        else:
            #adds a number or period if it is pressed
            if keys == pygame.K_0:
                ip += "0"
            elif keys == pygame.K_1:
                ip += "1"
            elif keys == pygame.K_2:
                ip += "2"
            elif keys == pygame.K_3:
                ip += "3"
            elif keys == pygame.K_4:
                ip += "4"
            elif keys == pygame.K_5:
                ip += "5"
            elif keys == pygame.K_6:
                ip += "6"
            elif keys == pygame.K_7:
                ip += "7"
            elif keys == pygame.K_8:
                ip += "8"
            elif keys == pygame.K_9:
                ip += "9"
            elif keys == pygame.K_PERIOD:
                ip += "."
#imports
import pygame, os

#inits
pygame.init()

#constents
WIDTH, HEIGHT = 500, 500
FPS = 60

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#screen
WIN = pygame.display.set_mode([WIDTH, HEIGHT])

#main funtion
def main():
    run = True

    clock = pygame.time.Clock()#defines the clock

    while run:# game loop
        clock.tick(FPS)#fps

        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                run = False
        
        WIN.fill(WHITE)# fills the screen

        pygame.display.update()# updates the display
        
    pygame.quit()#quits

# if it is being imported run the main
if __name__ == '__main__':
    main()
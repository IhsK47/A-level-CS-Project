import pygame
import sys 

pygame.init ()

screen_width = 1280
screen_height = 720
#this is the screen size which is set to be HD resolution

screen = pygame.display.set_mode((screen_width, screen_height)) #initialise the display module

running = True
while running: #this while loop allows a game loop to run
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #game quit
            pygame.quit()
            sys.exit()
            running = False


class Button():
    ''



pygame.font.init()

font = pygame.font("arial") #defining fonts

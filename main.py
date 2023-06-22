'''
fix pygame being in red

blit: block image transfer, draw one image onto another
screen.blit (surface name, position)

surface object instantion: thing = pygame.Surface( (w,h) )    parameters of a tuple with w,h
colo

in middle of button

'''

import pygame
import sys 

pygame.init ()

screen_width = 1280
screen_height = 720
#this is the screen size which is set to be HD resolution

screen = pygame.display.set_caption('My very cool game') #giving the window a name

screen = pygame.display.set_mode((screen_width, screen_height)) #initialise the display module/object

clock = pygame.time.Clock() #intantiating the clock object


test_button = pygame.Surface(  (200,100)  ) # surface object instantion: parameters of a tuple with w,h
test_button.fill ('Blue')

running = True
while running: #this while loop allows a game loop to run
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #game quit
            pygame.quit()
            sys.exit()
            running = False

    screen.blit (test_button,(500,200))

    pygame.display.update()
    clock.tick(90) #max 90 fps to make sure program doesnt overdo 



class Button():
    ''



pygame.font.init()

font = pygame.font("arial") #defining fonts



















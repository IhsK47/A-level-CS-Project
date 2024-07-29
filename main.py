'''
please note this is not the correct file to use, please use mainv2.py
'''

'''
blit: block image transfer, blit one image onto another
screen.blit (surface name, position) #the sprites top left corresponds to x,y f screen

surface object instantion: thing = pygame.Surface( (w,h) )   parameters of a tuple with w,h
colo
def rect(surface: Surface, color: ColorValue, rect: RectValue, width: int=0, border_radius: int=-1, border_top_left_radius: int=-1, 
border_top_right_radius: int=-1, border_bottom_left_radius: int=-1, border_bottom_right_radius: int=-1

in middle of sprite
https://www.youtube.com/watch?v=2iyx8_elcYg&list=PLWgEGaPlUGPdaoAuY1Iv1xQrqYLWrmTHZ&index=4&t=340s&ab_channel=CodingWithRuss

'''
#hint: save changes locally before saving to github ;)

import pygame
import sys 
import time
from constants import *

pygame.init()
pygame.font.init()


screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object

clock = pygame.time.Clock() #intantiating the clock object

#loading background
sky_surface = pygame.image.load('graphics\sunsetPixel.png').convert_alpha() #importing the image
sky_surface = pygame.transform.scale(sky_surface, (screen_size)) #resizing to screen size


overlay = pygame.Surface(screen_size) #instantiating an overlay to soften image for main menu
overlay.fill((192,192,192)) #grey rgb
overlay.set_alpha (120) #setting alpha for transparency


game_state = 'mainMenu'


class Button(): #defining the button class  
    #contruter method
    def __init__(self, text, x, y):
        self.rect = pygame.Rect(x, y, 200, 100)
        self.text = text
        self.color = grey
        self.text_color = black

    def draw(self, screen):
        # Draw the button on the screen
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)  # Create a font object
        text_surface = font.render(self.text, True, self.text_color)  # Render the text
        text_rect = text_surface.get_rect(center=self.rect.center)  # Center the text on the button
        screen.blit(text_surface, text_rect)  # Blit the text onto the screen

    def is_clicked(self, pos):
        # Check if a given point (pos) is inside the button's rectangle
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            return True


def main ():

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    mainMenu()
    pygame.display.flip()


def mainMenu ():
    global __display__ 

    pygame.display.set_caption('Main Menu')
    screen.blit(sky_surface, (0,0) )
    screen.blit(overlay, (0,0) )
    print ('menu')
    #main menu buttons
    
    
    playButton.draw(screen)  # Draw the button on the screen
    statsButton.draw(screen)
    settingsButton.draw(screen)
    quitButton.draw(screen)

    for event in pygame.event.get(): 

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button was clicked
 #           next 
            if playButton.is_clicked(pos):
                playButtonScreen ()
            if quitButton.is_clicked(pos):
                return False
            elif settingsButton.is_clicked(pos):
                settingsScreen ()


def playButtonScreen():

    pygame.display.set_caption('The Very Cool Game')
    screen.blit(sky_surface, (0,0) )
    print ('play')
    testbutton = Button ("test text",400,400)
    testbutton.draw(screen)
    pygame.display.update()


def settingsScreen ():
    pygame.display.set_caption('Settings Menu')
    print ('settings')

def createFont (font,size):
    newFont = pygame.font.sysFont(font,size)
    return newFont

def draw_text(text, font, col, x, y): #function to draw text and then blit it
  txt = font.render(text, True, col)
  screen.blit(txt, (x, y))

playButton = Button("Play", 540, 100) #instantiation of the button
statsButton = Button ("Stats", 540, 250)
settingsButton = Button ("Settings", 540, 400)
quitButton = Button ("Quit", 540, 550)

main()
running = True
while running: #this while loop allows a game loop to run

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if quitButton.is_clicked(pos): #'''(event.type == pygame.QUIT) or'''  #game quit
            print ('quit1')
            pygame.quit()
            sys.exit()
            running = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button was clicked
            #pos = pygame.mouse.get_pos()
            if playButton.is_clicked(pos):
                playButtonScreen ()
            if quitButton.is_clicked(pos):
                print('quit2')
                running = False                

            elif settingsButton.is_clicked(pos):
                settingsScreen ()


    pygame.display.flip()
    clock.tick(90) #max 90 fps to make sure program doesnt overdo 


import pygame
import math
import random
import time

from constants import *
from gamePlay import *


pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object
clock = pygame.time.Clock() #intantiating the clock object



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


class MainMenu (pygame.sprite.Sprite):
    
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 540
        self.playButton = Button("Play", self.x, 100) #instantiation of the button
        self.statsButton = Button ("Stats", self.x, 250)
        self.settingsButton = Button ("Settings", self.x, 400)
        self.quitButton = Button ("Quit", self.x, 550)

    def draw (self):
        self.playButton.draw(screen)  # Draw the button on the screen
        self.statsButton.draw(screen)
        self.settingsButton.draw(screen)
        self.quitButton.draw(screen)

    def update (self):
        #background.with_overlay()
        self.draw()
        pos = pygame.mouse.get_pos() #get mouse position
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Check if the left mouse button was clicked 
                if self.playButton.is_clicked(pos):
                    game.endless_mode ()
                if self.quitButton.is_clicked(pos):
                    pygame.quit()
                elif self.settingsButton.is_clicked(pos):
                    settingsScreen ()
                elif self.statsButton.is_clicked(pos):
                    pass
                    # statsScreen
                self.kill()


def draw_text(text, text_type, col, x, y): #function to draw text and then blit it
  
    given_font = pygame.font.SysFont( text_type[0],text_type[1]  ) #text_type will always be a tuple and SysFont required seperately given arguements
    txt = given_font.render(text, True, col)
    screen.blit( txt, (x, y) )


#create base (baseSprite,x,y)
base = Base (baseSprite,-30, 445) 
#create main character 
barrie = Barrie (barrieSprite, 250, 482, 0.24)

#instantiate other relevant classes
background = Background ()
stats = Stats ()
game = Game () 
sound = Sounds ()
menu = MainMenu ()

#barrie group
barrie_group = pygame.sprite.GroupSingle()
barrie_group.add(barrie)

#create groups 
bullet_group = pygame.sprite.Group ()
enemy_group = pygame.sprite.Group ()
allurium_group = pygame.sprite.Group ()


running = True
while running: #this while loop allows a game loop to run

    menu.update()

    pos = pygame.mouse.get_pos()

    pygame.display.update()
    for event in pygame.event.get(): 
        print (event) #to allow me see when and which events are being considered
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)



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

class MainMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 540
        self.playButton = Button("Play", self.x, 100) #instantiation of the button
        self.statsButton = Button("Stats", self.x, 250)
        self.settingsButton = Button("Settings", self.x, 400)
        self.quitButton = Button("Quit", self.x, 550)

        self.play_clicked = False
        self.stats_clicked = False
        self.settings_clicked = False
        self.quit_clicked = False

    def draw(self):
        background.with_overlay() 
        self.playButton.draw(screen) # Draw the button on the screen
        self.statsButton.draw(screen)
        self.settingsButton.draw(screen)
        self.quitButton.draw(screen)

    def update(self):
        self.draw()
        self.pos = pygame.mouse.get_pos() #get mouse position

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Check if the left mouse button was clicked
                if self.playButton.is_clicked(self.pos):
                    self.play_clicked = True
                elif self.quitButton.is_clicked(self.pos):
                    self.quit_clicked = True
                elif self.settingsButton.is_clicked(self.pos):
                    self.settings_clicked = True
                elif self.statsButton.is_clicked(self.pos):
                    self.stats_clicked = True

                pygame.display.update()
                self.kill()

    def is_play_clicked(self):
        return self.play_clicked
    def is_quit_clicked(self):
        return self.quit_clicked
    def is_settings_clicked(self):
        return self.settings_clicked
    def is_stats_clicked(self):
        return self.stats_clicked


def settingsScreen ():
    background.with_overlay()
    pygame.display.set_caption('Settings Menu')
    print ('settings')
    pygame.display.update()


def draw_text(text, text_type, col, x, y): #function to draw text and then blit it
  
    given_font = pygame.font.SysFont( text_type[0],text_type[1]  ) #text_type will always be a tuple and SysFont required seperately given arguements
    txt = given_font.render(text, True, col)
    screen.blit( txt, (x, y) )


#instantiate 
menu = MainMenu ()

running = True
active_screen = "main_menu"

while running:
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            print('x was clicked, I think')
            running = False

    if active_screen == "main_menu":
        menu.update()

        if menu.is_play_clicked(): #settings the active_screen variable respectively
            active_screen = "endless_mode"
            print ('play')
        elif menu.is_quit_clicked():
            print('quitv2')
            exit()
        elif menu.is_settings_clicked():
            active_screen = "settings"
        elif menu.is_stats_clicked():
            active_screen = "stats"

    elif active_screen == "settings":
        settingsScreen()

    elif active_screen == 'stats':
        #statsScreen()
        pass

    elif active_screen == "endless_mode":
        game.endless_mode()

    pygame.display.update()
    clock.tick(60)


    pos = pygame.mouse.get_pos()

    pygame.display.update()
    for event in pygame.event.get(): 
        print (event) #to allow me see when and which events are being considered
        if event.type == pygame.QUIT:
            print ('x was clicked, i think')
            running = False



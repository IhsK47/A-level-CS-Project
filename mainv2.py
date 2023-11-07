import pygame
import sys 
import time

pygame.init()
pygame.font.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
lightBlue = (0,255,255)
yellow = (255,255,0)
green = (0,255,0)
pink = (255,0,255)
grey = (220,220,220)
darkGrey = (140,140,140)
#defining colours

screen_width = 1280
screen_height = 720
screen_size = (screen_width,screen_height)
#this is the screen size which is set to be HD resolution

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
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)
        font = pygame.font.Font(None, 36)  # Create a font object
        text_surface = font.render(self.text, True, self.text_color)  # Render the text
        text_rect = text_surface.get_rect(center=self.rect.center)  # Center the text on the button
        screen.blit(text_surface, text_rect)  # Blit the text onto the screen

    def is_clicked(self, pos):
        # Check if a given point (pos) is inside the button's rectangle
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            return True


def background(): 
    #loading background
    sky_surface = pygame.image.load('graphics\sunsetPixel.png').convert_alpha() #importing the image
    sky_surface = pygame.transform.scale(sky_surface, (screen_size)) #resizing to screen size
    screen.blit(sky_surface, (0,0) )

def overlay ():
    overlay = pygame.Surface(screen_size) #instantiating an overlay to soften image for main menu
    overlay.fill((192,192,192)) #grey rgb
    overlay.set_alpha (120) #setting alpha for transparency
    screen.blit(overlay, (0,0) )





def main ():


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    if __display__ == 'menu':
        mainMenu()

main()

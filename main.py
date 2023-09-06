'''
pygame.draw.circle(screen,(255,00,00), ( int(700) , int(700) ) , 10) general test circle

blit: block image transfer, blit one image onto another
screen.blit (surface name, position)

surface object instantion: thing = pygame.Surface( (w,h) )    parameters of a tuple with w,h
colo
def rect(surface: Surface, color: ColorValue, rect: RectValue, width: int=0, border_radius: int=-1, border_top_left_radius: int=-1, 
border_top_right_radius: int=-1, border_bottom_left_radius: int=-1, border_bottom_right_radius: int=-1

in middle of sprite
https://www.youtube.com/watch?v=2iyx8_elcYg&list=PLWgEGaPlUGPdaoAuY1Iv1xQrqYLWrmTHZ&index=4&t=340s&ab_channel=CodingWithRuss


LL: work directory issue -----------------------

'''
#hint: save changes locally before saving to github ;)

import pygame
import sys 

pygame.init()

screen_width = 1280
screen_height = 720
screen_size = (screen_width,screen_height)
#this is the screen size which is set to be HD resolution

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


#font = pygame.font.SysFont ()
#defining fonts


class sprite():
    ''


class Button (): #defining the button class  
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
        return self.rect.collidepoint(pos)

screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object

clock = pygame.time.Clock() #intantiating the clock object

#loading background
sky_surface = pygame.image.load('//CFBS-SVR-FILE1/PupilsData/2017/Kabirm/Documents/A-Level Programming Project/graphics/sunsetPixel.png').convert_alpha() #importing the image
sky_surface = pygame.transform.scale(sky_surface, (screen_size)) #resizing to screen size


overlay = pygame.Surface(screen_size) #instantiating an overlay to soften image for main menu
overlay.fill((192,192,192)) #grey rgb
overlay.set_alpha (120) #setting alpha for transparency

play = Button ("Play", 540, 100)
stats = Button ("stats", 540, 250)
settings = Button ("settings", 540, 400)
quit = Button ("Quit", 540, 550)


running = True
while running: #this while loop allows a game loop to run
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #game quit
            pygame.quit()
            sys.exit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button was clicked
            pos = pygame.mouse.get_pos()
            if quit.is_clicked(pos):
                running = False

    screen.blit(sky_surface, (0,0) )
    screen.blit(overlay, (0,0) )

    #main menu buttons
    play.draw(screen)  # Draw the button on the screen
    stats.draw(screen)
    settings.draw(screen)
    quit.draw(screen)


    pygame.display.update()
    clock.tick(90) #max 90 fps to make sure program doesnt overdo 



pygame.font.init()

font = pygame.font("arial") #defining fonts







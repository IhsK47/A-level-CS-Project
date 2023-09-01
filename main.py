'''
pygame.draw.circle(screen,(255,00,00), ( int(700) , int(700) ) , 10) general test circle


blit: block image transfer, blit one image onto another
screen.blit (surface name, position)

surface object instantion: thing = pygame.Surface( (w,h) )    parameters of a tuple with w,h
colo

in middle of sprite
https://www.youtube.com/watch?v=2iyx8_elcYg&list=PLWgEGaPlUGPdaoAuY1Iv1xQrqYLWrmTHZ&index=4&t=340s&ab_channel=CodingWithRuss

'''
#hint: save changes locally before saving to github ;)

import pygame
import sys 

pygame.init()

screen_width = 1280
screen_height = 720
screen_size = (screen_width,screen_height)
#this is the screen size which is set to be HD resolution


#defining fonts

screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object

clock = pygame.time.Clock() #intantiating the clock object

sky_surface = pygame.image.load('//CFBS-SVR-FILE1/PupilsData/2017/Kabirm/Documents/A-Level Programming Project/graphics/sunsetPixel.png').convert_alpha() #importing the image
sky_surface = pygame.transform.scale(sky_surface, (screen_size)) #resizing to screen size


overlay = pygame.Surface(screen_size) #instantiating an overlay to soften image for main menu
overlay.fill((192,192,192)) #grey rgb
overlay.set_alpha (120) #setting alpha for transparency

running = True
while running: #this while loop allows a game loop to run
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #game quit
            pygame.quit()
            sys.exit()
            running = False

    screen.blit(sky_surface, (0,0) )
    screen.blit(overlay, (0,0) )    

    pygame.display.update()
    clock.tick(90) #max 90 fps to make sure program doesnt overdo 



class sprite():
    ''

class button ():
  def __init__(self, given_text):
    #contruter method
    self.text = given_text


pygame.font.init()

font = pygame.font("arial") #defining fonts







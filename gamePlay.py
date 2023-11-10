import pygame


screen_width = 1280
screen_height = 720
screen_size = (screen_width,screen_height)
#this is the screen size which is set to be HD resolution

screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object
clock = pygame.time.Clock() #intantiating the clock object


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



#load images
castleSprite = pygame.image.load('graphics\castle 3d.png').convert_alpha() #castle


#castle class

class Castle ():
    def __init__ (self,castleSprite,x, y, scale):
        self.health = 1000
        self.max_health = self.health
    
        width = castleSprite.get_width () 
        height = castleSprite.get_height ()

        self.image = pygame.transform.scale(image, (int(width*scale)) , (height*scale) ) #to ensure image is a correct size
        self.rect = self.castleSprite.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect


    def setHealth (self, health): #set health via castle upgrades
        self.health = health




running = True
while running: #this while loop allows a game loop to run

    background()

    pos = pygame.mouse.get_pos()
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False





pygame.quit()
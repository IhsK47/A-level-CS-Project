import pygame


screen_width = 1280
screen_height = 720
screen_size = (screen_width,screen_height)
#this is the screen size which is set to be HD resolution

screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object
clock = pygame.time.Clock() #intantiating the clock object

player_team = 'teamBarie'
enemies_team = 'Opps'


def background(): 
    #loading background
    sky_surface = pygame.image.load('graphics\sunsetPixel.png').convert_alpha() #importing the image
    sky_surface = pygame.transform.scale(sky_surface, (screen_size)) #resizing to screen size
    screen.blit(sky_surface, (0,0) ) # 0,0 starts at bottom right 

def overlay ():
    overlay = pygame.Surface(screen_size) #instantiating an overlay to soften image for main menu
    overlay.fill((192,192,192)) #grey rgb
    overlay.set_alpha (120) #setting alpha for transparency
    screen.blit(overlay, (0,0) )


#load images
castleSprite = pygame.image.load('graphics\castle 3d.png').convert_alpha() #castle
barrieSprite = pygame.image.load('grahics\barrieStickman.png').convert_alpha() #main character



#castle class

class Castle ():
    def __init__ (self,castleSprite,x, y, scale):
        self.health = 1000
        self.max_health = self.health
    
        width = int(castleSprite.get_width () * scale)
        height = int(castleSprite.get_height ()  * scale)
        print ('castle w.h:', width, height)

        self.castleSprite = pygame.transform.scale(castleSprite, (height, width) ) #to ensure image is a correct size
        self.rect = self.castleSprite.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect


    def setHealth (self, health): #set health via castle upgrades
        self.health = health

    def draw (self):
        self.image = self.castleSprite
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in


class Barrie (): #the main character of my game is called barrie
    
    def __init__ (self,barrieSprite,x, y, scale):
        self.health = 200
        self.max_health = self.health
        self.move_speed = 5

        width = int(barrieSprite.get_width () * scale)
        height = int(barrieSprite.get_height ()  * scale)
        print ('barrie w.h:', width, height)

        self.barrieSprite = pygame.transform.scale(barrieSprite, (height, width) ) #to ensure image is a correct size
        self.rect = self.barrieSprite.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect

    def movement (self):
        pass #to be completed later

    def setHealth (self, health): #set health via castle upgrades
        self.health = health

    def shoot(self):
        pass # to be completed later


    def draw (self):
        self.image = self.barrieSprite
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in


class Soilders (pygame.sprite.Sprite):

    def __init__ (self, x, y, unit_type, soilder_team, side, vetical, walk_frames, attack_frames, health, attack, defence, speed): 
        pass



# create castle (castleSprite,x,y, scale)
castle = Castle (castleSprite,0, 380 ,0.7 ) 


running = True
while running: #this while loop allows a game loop to run

    background()
    castle.draw ()

    pos = pygame.mouse.get_pos()
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False





pygame.quit()
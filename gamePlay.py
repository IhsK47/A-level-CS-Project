import pygame
import math
from constants import *

screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object
clock = pygame.time.Clock() #intantiating the clock object

player_team = 'teamBarie'
enemies_team = 'Opps'

#white = (255,255,255)

class Background ():

    def __init__ (self):  #loading background

        self.sky_surface = pygame.image.load('graphics\sunsetPixel.png').convert_alpha() #importing the image
        self.sky_surface = pygame.transform.scale(self.sky_surface, (screen_size)) #resizing to screen size        

    def draw(self): 
        screen.blit(self.sky_surface, (0,0) ) # 0,0 starts at bottom right 

    def overlay (self):
        overlay = pygame.Surface(screen_size) #instantiating an overlay to soften image for main menu
        overlay.fill((192,192,192)) #grey rgb
        overlay.set_alpha (120) #setting alpha for transparency
        screen.blit(overlay, (0,0) )

#create background object
background = Background ()

#load images
castleSprite = pygame.image.load('graphics\castle 3d.png').convert_alpha() #castle
barrieSprite = pygame.image.load('graphics\BarrieStickman.png').convert_alpha() #main character

#creating a rect for enemy testing 
enemySprite = pygame.Rect(  screen_width-10 , 460, 100,100   )

#castle class

class Castle ():
    def __init__ (self,castleSprite,x, y, scale):
        self.health = 1000
        self.max_health = self.health
    
        width = int(castleSprite.get_width () * scale)
        height = int(castleSprite.get_height ()  * scale)
        print ('castle w.h:', width, height)

        self.castleSprite = pygame.transform.scale(castleSprite, (width,height ) ) #to ensure image is a correct size
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
        self.speed = 15
        self.fired = False

        width = int(barrieSprite.get_width () * scale)
        height = int(barrieSprite.get_height ()  * scale)

        self.barrieSprite = pygame.transform.scale(barrieSprite, (width, height) ) #to ensure image is a correct size
        self.rect = self.barrieSprite.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect

    def move (self):
        # if pos < screen width: #barriers
#        self.rect.move_ip(0,speed)

        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if (key[pygame.K_a] == True) or (key[pygame.K_DOWN] == True):
                self.rect.move_ip(-self.speed, 0)
            if (key[pygame.K_d] == True) or (key[pygame.K_UP] == True):
                self.rect.move_ip(self.speed, 0)
        pygame.display.flip()


    def setHealth (self, health): #set health via castle upgrades
        self.health = health

    def draw (self):
        self.image = self.barrieSprite
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in

    def shoot(self): #created bullets using bullets class
        
        pos = pygame.mouse.get_pos()

        bulletStart_x = self.rect.right - 5
        bulletStart_y = self.rect.top + 20
        x_dist = pos[0] - bulletStart_x
        y_dist = bulletStart_y - pos[1]
        self.angle = math.atan2 (y_dist, x_dist)

        if pygame.mouse.get_pressed()[0] == True and self.fired == False:
            self.fired = True
            bullet = Bullet (bulletStart_x,bulletStart_y, self.angle)
            bullet_group.add(bullet)
        if pygame.mouse.get_pressed()[0] == False:
            self.fired = False

        
        pygame.draw.line (screen, white, (bulletStart_x, bulletStart_y)  ,  (pos) )

        pygame.display.flip ()
        
class Bullet (pygame.sprite.Sprite):

    def __init__ (self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graphics\BarrieBullet.png').convert_alpha() #load bullet

        self.scale = 0.3
        width = int(self.image.get_width () * self.scale)
        height = int(self.image.get_height ()  * self.scale)
        self.image = pygame.transform.scale(self.image, (width, height) ) #to ensure image is a correct size

        self.speed = 9
        self.angle = angle

        #horizontal and vertical speeds using trig 
        self.dx = math.cos(self.angle) * self.speed
        self.dy = - (math.sin(self.angle) * self.speed)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect
    
    def update (self):

        if self.rect.right < 0 or self.rect.left > screen_width or self.rect.bottom < 0 or self.rect.top > screen_height:
            self.kill ()
        self.rect.move_ip(self.dx, 0)
        self.rect.move_ip(0, self.dy)
        


class Soldiers (pygame.sprite.Sprite): 

    def __init__ (self, x, y, soldier_type, soldier_team, side, walk_frames, attack_frames, health, attack, defence, speed): 
        pygame.sprite.Sprite.__init__ (self)

        self.soldier_type = soldier_type
        self.soldier_team = soldier_team

        self.enemySprite = pygame.image.load('graphics\enemySprite.png').convert_alpha()
        
        if self.soldier_team == enemies_team:
            self.image = self.enemySprite
            self.scale = 0.3
            width = int(self.image.get_width () * self.scale)
            height = int(self.image.get_height ()  * self.scale)
            self.image = pygame.transform.scale(self.image, (width, height) ) #to ensure image is a correct size



        self.side = side #left/right
        self.vertical = 480 # y pos
        
        self.walkingAnimationLength = walk_frames
        self.attackingAnimationLength = attack_frames

        self.health = health
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.alive = True

        self.last_update = 0 #when amimation was last updated
        self.current_frame = 0 #current frame for animation, starts at zero to be on the first frame
        self.load_animations()



    def load_animations ():
        pass #to be completed later
    ''' #this code below ensures that the first frame is the first frame of walking with is in animation list as zero,zero 
    self.animation_list = animation_list 
    self.action = 0
    self.frame_index = 0
    self.image = self.animation_list [self.action][self.frame_index]
    '''





# create castle (castleSprite,x,y, scale)
castle = Castle (castleSprite,0, 380 ,0.7 ) 
#create main character 
barrie = Barrie (barrieSprite, 250, 480, 0.25)

#create groups 
bullet_group = pygame.sprite.Group ()



running = True

while running: #this while loop allows a game loop to run

    background.draw()
    castle.draw ()

    barrie.draw ()
    barrie.move()
    barrie.shoot()

    bullet_group.draw (screen)
    bullet_group.update ()

    pos = pygame.mouse.get_pos()
    pygame.display.update()
    for event in pygame.event.get(): 
        print (event)
        if event.type == pygame.QUIT:
            running = False





pygame.quit()
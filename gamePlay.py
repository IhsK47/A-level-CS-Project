import pygame
import math
import random
from constants import *

screen = pygame.display.set_caption('My very cool game') #giving the window a name
screen = pygame.display.set_mode(screen_size) #initialise the display module/object
clock = pygame.time.Clock() #intantiating the clock object

player_team = 'teamBarie'
enemies_team = 'Opps'

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
baseSprite = pygame.image.load('graphics\Base100.png').convert_alpha() #base
barrieSprite = pygame.image.load('graphics\BarrieStickman.png').convert_alpha() #main character

class Base (): #base class
    def __init__ (self,baseSprite,x, y):
        self.health = 400
        self.max_health = self.health
    
        self.baseSprite = baseSprite
        self.scale = 0.5
        self.image = scale (baseSprite, self.scale)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect

    def setHealth (self, health): #set health via base upgrades
        self.health = health

    def draw (self):
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in

    def update (self):
        self.draw ()

class Barrie (pygame.sprite.Sprite): #the main character of my game is called barrie
    
    def __init__ (self,barrieSprite,x, y, scale):
        
        pygame.sprite.Sprite.__init__ (self)
        self.barrieSprite = barrieSprite
        self.health = 200
        self.max_health = self.health
        self.speed = 15
        self.fired = False

        self.allurium = 0

        width = int(barrieSprite.get_width () * scale)
        height = int(barrieSprite.get_height ()  * scale)

        self.barrieSprite = pygame.transform.scale(barrieSprite, (width, height) ) #to ensure image is a correct size
        self.rect = self.barrieSprite.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect

    def move (self):

        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if (self.rect.left > 0)  and ( (key[pygame.K_a] == True) or (key[pygame.K_DOWN] == True) ) :
                self.rect.move_ip(-self.speed, 0 )
            if (self.rect.right < screen_width)  and  (key[pygame.K_d] == True) or (key[pygame.K_UP] == True):
                self.rect.move_ip(self.speed, 0 )
        #pygame.display.flip()

    def setHealth (self, health): #set health via base upgrades
        self.health = health

    def draw (self):
        self.image = self.barrieSprite
        pygame.draw.rect (screen, white, self.rect, 1) #########################################
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in

    def shoot(self): #created bullets using bullets class
        
        pos = pygame.mouse.get_pos()

        bulletStart_x = self.rect.right - 5
        bulletStart_y = self.rect.top + 25
        x_dist = pos[0] - bulletStart_x
        y_dist = bulletStart_y - pos[1]
        self.angle = math.atan2 (y_dist, x_dist)

        if pygame.mouse.get_pressed()[0] == True and self.fired == False:
            self.fired = True
            bullet = Bullet (bulletStart_x,bulletStart_y, self.angle)
            bullet_group.add(bullet)
        if pygame.mouse.get_pressed()[0] == False:
            self.fired = False

        
        pygame.draw.line (screen, white, (bulletStart_x, bulletStart_y)  ,  (pos) ) #############################

    def allurium_pickUp(self):
        print ('alluriumpu running',self.allurium)
        for allurium_sprite in pygame.sprite.spritecollide(self,allurium_group, True): #setting to true will automatically delete the allurium that has collided
            print ('allurium hit')
            self.allurium += allurium_sprite.quantity

    def update (self):
        self.draw ()
        self.move()
        self.allurium_pickUp ()
        self.shoot()


class Enemy (pygame.sprite.Sprite): 

    def __init__ (self, x, enemy_type, walk_frames, attack_frames, attack, defence, speed): 
        pygame.sprite.Sprite.__init__ (self)

        if enemy_type == 'swordman':
            self.enemySprite = pygame.image.load('graphics\enemySprite.png').convert_alpha()            
            self.scale = 0.21
            self.health = 80
            self.damage = 25

        self.image = self.enemySprite
        width = int(self.image.get_width () * self.scale)
        height = int(self.image.get_height ()  * self.scale)
        self.image = pygame.transform.scale(self.image, (width, height) ) #to ensure image is a correct size
        
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.y = x, 525 # y pos

        self.attack = attack
        self.attack_cooldown = 900
        self.attackingAnimationLength = attack_frames
        self.last_attack = pygame.time.get_ticks()

        self.speed = speed
        self.walkingAnimationLength = walk_frames

        self.defence = defence
        self.alive = True

        self.action_list = ['walk','attackP','attackB','death'] #attackP = attacking player, attackB = attacking base
        self.current_action = 0 # 0: walk, 1: attackB, 2: attackP 3: death

        self.last_update = 0 #when amimation was last updated
        self.current_frame = 0 #current frame for animation, starts at zero to be on the first frame
        self.update_time = pygame.time.get_ticks()
        
        self.load_animations()

    def check_collisions():
        pass

    def move (self):
        self.rect.x -= self.speed
        screen.blit(self.image,self.rect)

    def drop_item(self, item_type):
        if item_type == 'allurium':
            allurium_drop = Allurium(self.rect.x,self.rect.bottom)
            allurium_group.add(allurium_drop)
        elif item_type == 'coins':
            # Implement the creation of a coins instance here
            pass
        # Add more conditions for other types of items

    def update (self):

        if self.health <= 0:
            self.alive = False
            self.update_action (0) #die
            print ('enemy killed')
            # Randomly choose the type of item to drop (you can implement your logic here)
            item_to_drop = random.choice(['allurium','allurium'])  #, 'gold'])
            self.drop_item(item_to_drop)
            self.kill ()
        else:
            if pygame.sprite.spritecollide(self,bullet_group, True): #setting to true will automatically delete the bullet that has collided
                print ('enemy hit')
                self.health -= 20
            if self.rect.left < barrie.rect.right and not(self.rect.right < barrie.rect.left): #check if enemy has reached barrie 
                self.update_action (1) #attack barrie
                print ('enemy is attacking barrie')
            elif self.rect.left < base.rect.right: #check if enemy has reached base 
                self.update_action (2) #attack base
                print ('enemy is attacking base')
            elif self.alive: #only moves if alive
                self.move()
                
    def update_action (self, new_action): #check if the new action is different to the previous one
        if new_action != self.current_action:
            self.current_action = new_action
            self.current_frame = 0 #this ensures frame index is returned to 0 to begin on the animations for the next action rather than starting halfway through the other actions
            self.update_date = pygame.time.get_ticks () 

    def load_animations (self):
        pass #to be completed later
    ''' #this code below ensures that the first frame is the first frame of walking with is in animation list as zero,zero 
    self.animation_list = animation_list 
    self.action = 0
    self.frame_index = 0
    self.image = self.animation_list [self.action][self.frame_index]
    '''

class Allurium(pygame.sprite.Sprite):
    def __init__ (self, x, y ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graphics\Allurium_bars.webp').convert_alpha() #load bullet
        self.image = scale (self.image,0.7)

        self.quantity = 3

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y - 2*(self.image.get_height()) #x&y co-odinates for the rect

    def draw (self): #spawn allurium
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in

    def update (self):
        self.draw()

        
class Bullet (pygame.sprite.Sprite):

    def __init__ (self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graphics\BarrieBullet.png').convert_alpha() #load bullet

        self.scale = 0.3
        width = int(self.image.get_width () * self.scale)
        height = int(self.image.get_height ()  * self.scale)
        self.image = pygame.transform.scale(self.image, (width, height) ) #to ensure image is a correct size

        self.speed = 8
        self.angle = angle

        #horizontal and vertical speeds using trig 
        self.dx = math.cos(self.angle) * self.speed
        self.dy = - (math.sin(self.angle) * self.speed)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x - width), y #x&y co-odinates for the rect
    
    def update (self):

        if self.rect.right < 0 or self.rect.left > screen_width or self.rect.bottom < 0 or self.rect.top > screen_height:
            self.kill ()
        self.rect.move_ip(self.dx, 0)
        self.rect.move_ip(0, self.dy)



def scale (image, scale):
    width = int(image.get_width () * scale)
    height = int(image.get_height ()  * scale)
    print (width, height)
    image = pygame.transform.scale(image, (width, height)) #to ensure image is a correct size
    return image


# create base (baseSprite,x,y, scale)
base = Base (baseSprite,0, 445 ) 
#create main character 
barrie = Barrie (barrieSprite, 250, 482, 0.24)

#barrie group
barrie_group = pygame.sprite.GroupSingle()
barrie_group.add(barrie)

#create groups 
bullet_group = pygame.sprite.Group ()
enemy_group = pygame.sprite.Group ()
allurium_group = pygame.sprite.Group ()

#create enemy
enemy1 = Enemy (screen_width - 100, 'swordman',10, 10,10, 10, 4)
enemy_group.add(enemy1)

running = True

while running: #this while loop allows a game loop to run

    background.draw()
    base.draw ()

    barrie_group.update()

    bullet_group.update ()
    bullet_group.draw (screen) 

    enemy_group.update ()
    enemy_group.draw (screen)
    
    allurium_group.update()

    pos = pygame.mouse.get_pos()

    pygame.display.update()
    for event in pygame.event.get(): 
        print (event) #to allow me see when and which events are being considered
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
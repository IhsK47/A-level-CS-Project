import pygame
import math
import random
import time
from constants import *

pygame.init()
pygame.font.init()
pygame.mixer.init()


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

    def with_overlay (self):
        self.draw()
        self.overlay()


#load images
baseSprite = pygame.image.load('graphics\Base100.png').convert_alpha() #base
barrieSprite = pygame.image.load('graphics\BarrieStickman.png').convert_alpha() #main character

class Base (): #base class
    def __init__ (self,baseSprite,x, y):
        self.health = 400
        self.max_health = self.health
        self.alive = True
    
        self.baseSprite = baseSprite
        self.scale = 0.5
        self.image = scale (baseSprite, self.scale)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect

        self.healthBar = HealthBar (x+50, y - 70, self.rect.width-50, 30 , self.max_health, player_team)

    def setMaxHealth (self, health): #set health via base upgrades
        self.health = health

    def damaged (self,damage):
        if self.health > 0: 
            self.health -= damage
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            self.alive = False

    def draw (self):
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in

    def update (self):
        self.draw ()
        self.healthBar.update(self.health, self.rect.x+40, self.rect.y - 70 )
        

class Barrie (pygame.sprite.Sprite): #the main character of my game is called barrie
    
    def __init__ (self,barrieSprite,x, y, scale):
        
        pygame.sprite.Sprite.__init__ (self)
        self.barrieSprite = barrieSprite
        self.health = 200
        self.max_health = self.health
        self.speed = 13
        self.fired = False
        self.alive = True
        self.allurium = 0

        width = int(barrieSprite.get_width () * scale)
        height = int(barrieSprite.get_height ()  * scale)

        self.barrieSprite = pygame.transform.scale(barrieSprite, (width, height) ) #to ensure image is a correct size
        self.rect = self.barrieSprite.get_rect()
        self.rect.x, self.rect.y = x, y #x&y co-odinates for the rect

        self.healthBar = HealthBar (x, y - 10, self.rect.width, 10 , self.max_health, player_team)

    def move (self):

        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if (self.rect.left > 0)  and ( (key[pygame.K_a] == True) or (key[pygame.K_DOWN] == True) ) :
                self.rect.move_ip(-self.speed, 0 )
            if (self.rect.right < screen_width)  and  (key[pygame.K_d] == True) or (key[pygame.K_UP] == True):
                self.rect.move_ip(self.speed, 0 )
        #pygame.display.flip()

    def setMaxHealth (self, health): #set health via base upgrades
        self.health = health

    def draw (self):
        self.image = self.barrieSprite
        pygame.draw.rect (screen, white, self.rect, 1) ######################################### testinf purposes
        screen.blit (self.image, self.rect) #co ordinated defined already for x & y hence self.rect can be passed in
        self.healthBar.update(self.health, self.rect.x, self.rect.y - 10 )

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
        for allurium_sprite in pygame.sprite.spritecollide(self,allurium_group, True): #setting to true will automatically delete the allurium that has collided
            print ('allurium hit', self.allurium)
            self.allurium += allurium_sprite.quantity

    def damaged (self,damage):
        if self.health > 0: 
            self.health -= damage
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            self.alive = False

    def update (self):
        self.draw ()
        if self.alive:
            self.move()
            self.allurium_pickUp ()
            self.shoot()

class Enemy (pygame.sprite.Sprite): 

    def __init__ (self, x, enemy_type): 
        pygame.sprite.Sprite.__init__ (self)

        if enemy_type == 'swordman':
            self.enemySprite = pygame.image.load('graphics\enemySprite.png').convert_alpha()            
            self.scale = 0.18
            self.health = 80
            self.damage = 25
            self.scoreValue = 50
            
        self.speed = 3
        self.image = self.enemySprite
        width = int(self.image.get_width () * self.scale)
        height = int(self.image.get_height ()  * self.scale)
        self.image = pygame.transform.scale(self.image, (width, height) ) #to ensure image is a correct size
        
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.y = x, 530 # y pos

        self.attack_cooldown = 900 #900 milliseconds
        self.attackingAnimationLength = 10
        self.last_attack = pygame.time.get_ticks()

        
        self.walkingAnimationLength = 10

        self.alive = True

        self.action_list = ['walk','attackP','attackB','death'] #attackP = attacking player, attackB = attacking base
        self.current_action = 0 # 0: walk, 1: attackB, 2: attackP 3: death

        self.last_update = 0 #when amimation was last updated
        self.current_frame = 0 #current frame for animation, starts at zero to be on the first frame
        self.update_time = pygame.time.get_ticks()
        
        self.healthBar = HealthBar (x,self.rect.y-8,self.rect.width, 8 , self.health, enemies_team)
        self.load_animations()

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

    def attack (self, target):
        if pygame.time.get_ticks () - self.last_attack > self.attack_cooldown: #check time since last attack > cooldown
            print ('enemy is attacking',target)
            target.damaged (self.damage)
            self.last_attack = pygame.time.get_ticks () #reset it so last attack is now > cooldown

    def update (self):

        self.healthBar.update(self.health, self.rect.x, self.rect.y - 8)
        if self.health <= 0:
            self.alive = False
            stats.score += self.scoreValue
            stats.currentScore += self.scoreValue
            stats.enemiesKilled += 1

            self.update_action (0) #die
            print ('enemy killed', stats.enemiesKilled)
            print ('currentscore: ',stats.currentScore) #test stats working
            # Randomly choose the type of item to drop (you can implement your logic here)
            item_to_drop = random.choice(['allurium','allurium'])  #, 'coins'])
            self.drop_item(item_to_drop)
            self.kill ()
        else:
            if pygame.sprite.spritecollide(self,bullet_group, True): #setting to true will automatically delete the bullet that has collided
                self.health -= 20
                stats.totalDamageDealt += 20
                
            if self.rect.left < barrie.rect.right and not(self.rect.right < barrie.rect.left): #check if enemy has reached barrie 
                self.update_action (1) #attack barrie

            elif self.rect.left < base.rect.right: #check if enemy has reached base 
                self.update_action (2) #attack base

            elif self.alive: #only moves if alive
                self.move()
                
        if self.current_action == 1:
            self.attack (barrie)
        elif self.current_action == 2:
            self.attack(base)

    def update_action (self, new_action): #check if the new action is different to the previous one
        if new_action != self.current_action:
            self.current_action = new_action
            self.current_frame = 0 #this ensures frame index is returned to 0 to begin animations for next action rather than starting halfway
            self.update_date = pygame.time.get_ticks () 

    def load_animations (self):
        pass #to be completed later
    ''' #this code below ensures that the first frame is the first frame of walking with is in animation list as zero,zero 
    self.animation_list = animation_list 
    self.action = 0
    self.frame_index = 0
    self.image = self.animation_list [self.action][self.frame_index]
    '''

class HealthBar ():
    def __init__(self, x, y, width, height, max_health, character_team):

        self.x,self.y = x, y
        self.width = width
        self.height = height
        self.max_health = max_health

        self.bg_colour = grey
        if character_team == player_team:
            self.health_colour = green
        elif character_team == enemies_team:
            self.health_colour = red

    def update(self, health, x, y):
            bar_width = int(self.width * (health / self.max_health))
            self.x,self.y = x, y
            pygame.draw.rect(screen, self.bg_colour, (self.x, self.y, self.width, self.height)) #first draws bg
            pygame.draw.rect(screen, self.health_colour, (self.x, self.y, bar_width, self.height)) #draws actual health over


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

        self.speed = 10
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


class Stats ():
    def __init__ (self):
        self.score = 0
        self.currentScore = 0
        self.highScore = 0
        self.enemiesSpawned = 0
        self.enemiesKilled = 0
        self.totalEnemiesKilled = 0
        self.roundsPlayed = 0
        self.totalPlayingTime = 0
        self.totalAllies = 0
        self.totalDamageDealt = 0
    
    def round_end(self):
        if self.score > self.highScore:
            self.highScore = self.currentScore
        self.currentScore = 0
        self.totalEnemiesKilled += self.enemiesKilled
        self.enemiesKilled = 0
        

class Sounds ():
    def __init__ (self):

        self.defeatMusic = pygame.mixer.Sound('audio/Afraid Humming.mp3')
       
        #self.victoryMusic = pygame.mixer.music.load('Audio/        .mp3')

class Game():

    def __init__(self):
        self.enemy_spawn_interval = [1300, 1000, 1100, 700, 1500, 900] #index 0-4
        self.enemy_spawn_timer = pygame.time.get_ticks()  # Initialize the timer

    
    def update_loop (self):
        background.draw()
        
        base.update ()
        barrie_group.update()

        bullet_group.update ()
        bullet_group.draw (screen) 

        enemy_group.update ()
        enemy_group.draw (screen)
        
        allurium_group.update()

    
    def endless_mode(self):
        current_time = pygame.time.get_ticks()

        self.update_loop ()

        if barrie.alive and base.alive:

            if stats.score < 1000: #for 20 kills, 1.3s // total = 20
                spawn = 0
            elif stats.score < 1500: #for 10 kills, 1s // total = 30
                spawn = 1
            elif stats.score < 2000: #for 10 kills, 1.1s // total = 40 
                spawn = 2
            elif stats.score < 3250: #for 15 kills, 0.7s // total = 45 
                spawn = 3
            elif stats.score < 3750: #for 20 kills, 1.5s // total = 55
                spawn = 4
            elif stats.score < 4000: #for 15 kills, 0.9s // total = 60
                spawn = 5
            else:
                spawn = 0
                stats.score = 0
            
            if (current_time - self.enemy_spawn_timer) > self.enemy_spawn_interval[spawn]:
                enemy1 = Enemy(screen_width - 100, 'swordman')
                enemy_group.add(enemy1)
                self.enemy_spawn_timer = current_time  # Reset the timer
        else: 
            
            background.overlay()
            defeat_Screen(stats.enemiesKilled,stats.currentScore)
            time.sleep(3) #####################################################################
            stats.round_end()


def victory_Screen():
    #sound.victoryMusic.play()

    draw_text ('Victory!',titleFont, black ,screen_width / 2 -100, 200 )
    draw_text (f'kills = {kills}', normalFont, black , screen_width / 2 - 65 , 300 )
    draw_text (f'score = {score}', normalFont, black , screen_width / 2 - 65  , 350 )

def defeat_Screen(kills,score):
    #show defeat message
    sound.defeatMusic.play()

    draw_text ('Defeat.',titleFont, black ,screen_width / 2 -100, 200 )
    draw_text (f'kills = {kills}', normalFont, black , screen_width / 2 - 65 , 300 )
    draw_text (f'score = {score}', normalFont, black , screen_width / 2 - 65  , 350 )

def scale (image, scale):
    width = int(image.get_width () * scale)
    height = int(image.get_height () * scale)

    image = pygame.transform.scale(image, (width, height)) #to ensure image is a correct size
    return image






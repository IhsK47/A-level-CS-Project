import pygame

pygame.init ()

screen_width = 1280
screen_height = 720
#this is the screen size which is the HD size

#font = pygame.font("arial") #defining fonts


screen = pygame.display.set_mode((screen_width, screen_height)) #initialise the display module

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #game quit
            pygame.quit()
            sys.exit()
            running = False
#    pygame.display.update() #

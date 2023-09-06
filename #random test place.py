#random test place

'''
pygame.draw.line(surface: Surface, color: _ColorValue, start_pos: _Coordinate, end_pos: _Coordinate, width: int=1)


import pygame

pygame.init()

screen_width = 1280
screen_height = 720
screen_size = (screen_width,screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("test enviroment")

fonts = ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui', 'microsoftyibaiti', 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 'mongolianbaiti', 'msgothic', 'msuigothic', 'mspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsun', 'nsimsun', 'simsunextb', 'sitkasmall', 'sitkatext', 'sitkasubheading', 'sitkaheading', 'sitkadisplay', 'sitkabanner', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 'yugothicregular', 'yugothicuisemilight', 'holomdl2assets', 'agencyfb', 'algerian', 'bookantiqua', 'arialrounded', 'baskervilleoldface', 'bauhaus93', 'bell', 'bernardcondensed', 'bodoni', 'bodoniblack', 'bodonicondensed', 'bodonipostercompressed', 'bookmanoldstyle', 'bradleyhanditc', 'britannic', 'berlinsansfb', 'berlinsansfbdemi', 'broadway', 'brushscript', 'bookshelfsymbol7', 'californianfb', 'calisto', 'castellar', 'centuryschoolbook', 'centaur', 'century', 'chiller', 'colonna', 'cooperblack', 'copperplategothic', 'curlz', 'dubai', 'dubaimedium', 'dubairegular', 'elephant', 'engravers', 'erasitc', 'erasdemiitc', 'erasmediumitc', 'felixtitling', 'forte', 'franklingothicbook', 'franklingothicdemi', 'franklingothicdemicond', 'franklingothicheavy', 'franklingothicmediumcond', 'freestylescript', 'frenchscript', 'footlight', 'garamond', 'gigi', 'gillsans', 'gillsanscondensed', 'gillsansultracondensed', 'gillsansultra', 'gloucesterextracondensed', 'gillsansextcondensed', 'centurygothic', 'goudyoldstyle', 'goudystout', 'harlowsolid', 'harrington', 'haettenschweiler', 'hightowertext', 'imprintshadow', 'informalroman', 'blackadderitc', 'edwardianscriptitc', 'kristenitc', 'jokerman', 'juiceitc', 'kunstlerscript', 'widelatin', 'lucidabright', 'lucidacalligraphy', 'leelawadee', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'lucidasansregular', 'lucidasansroman', 'lucidasanstypewriterregular', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'magneto', 'maiandragd', 'maturascriptcapitals', 'mistral', 'modernno20', 'microsoftuighur', 'monotypecorsiva', 'extra', 'niagaraengraved', 'niagarasolid', 'ocraextended', 'oldenglishtext', 'onyx', 'msoutlook', 'palacescript', 'papyrus', 'parchment', 'perpetua', 'perpetuatitling', 'playbill', 'poorrichard', 'pristina', 'rage', 'ravie', 'msreferencesansserif', 'msreferencespecialty', 'rockwellcondensed', 'rockwell', 'rockwellextra', 'script', 'showcardgothic', 'snapitc', 'stencil', 'twcen', 'twcencondensed', 'twcencondensedextra', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'wingdings2', 'wingdings3', 'arialforautographuni', 'levenim', 'freesiaupc', 'traditionalarabic', 'lettergothicstdslantedopentype', 'cordiaupc', 'diamondcreek', 'lemonmilk', 'fantasticreasonpersonaluse', 'myriadarabicopentype', 'prestigeelitestdbdopentype', 'kodchiangupc', 'milleniapersonaluse', 'oratorstdopentype', 'browallianew', 'simhei', 'strawberryblossom', 'miriamfixed', 'kozgopr6nmediumopentype', 'myriadproboldconditopentype', 'kozminpr6nregularopentype', 'adobeheitistdregularopentype', 'kozminpr6nheavyopentype', 'acaslonproboldopentype', 'northwoodhigh', 'sakkalmajalla', 'myriadprosemiboldopentype', 'arialms', 'utsaah', 'adobenaskhmediumopentype', 'kalinga', 'raavi', 'aparajita', 'dilleniaupc', 'kozgopr6nextralightopentype', 'kaiti', 'black', 'kartika', 'beautyandthebeast', 'irisupc', 'laoui', 'narkisim', 'acaslonproitalicopentype', 'lilyupc', 'hobostdopentype', 'miracleplacepersonaluse', 'daunpenh', 'kozgopr6nlightopentype', 'minionpromediumopentype', 'adobefangsongstdregularopentype', 'coffeeatmidnightdemo', 'khmerui', 'acaslonprosemibolditalicopentype', 'starjedioutline', 'agaramondprobolditalicopentype', 'kozgopromediumopentype', 'kozgopr6nboldopentype', 'cordianew', 'thewestgate', 'gisha', 'kozgopr6nregularopentype', 'nyala', 'coffeewritten', 'blackoakstdopentype', 'estrangeloedessa', 'coffeewithsugar', 'stencilstdopentype', 'vani', 'angsanaupc', 'pokemonhollownormal', 'kozminpromediumopentype', 'dabrush', 'rakoonpersonaluse', 'acaslonprobolditalicopentype', 'tunga', 'dfkaisb', 
'sugarpunchdemo', 'kokila', 'lemonadestand', 'adobedevanagariitalicopentype', 'euphemia', 'iskoolapota', 'meiryo', 'meiryoui', 'eucrosiaupc', 'tektonproboldcondopentype', 'badaboombb', 'adobedevanagaribolditalicopentype', 'shonarbangla', 'angsananew', 'simplifiedarabic', 'adobearabicboldopentype', 'januaryhandwriting', 'adobedevanagariitalic', 'adventure', 'ocrastdopentype', 'adobemyungjostdmediumopentype', 'myriadproboldopentype', 'trajanproregularopentype', 'rod', 'myriadproitopentype', 'shruti', 'amazdoomrightoutline', 'david', 'lettergothicstdboldopentype', 'dokchampa', 'browalliaupc', 'gautami', 'dulcelin', 'batang', 'batangche', 'gungsuh', 'gungsuhche', 'msmincho', 'mspmincho', 'gulim', 'gulimche', 'dotum', 'dotumche', 'latha', 'mangal', 'minionprobolditopentype', 'minionproboldcnopentype', 'mingliu', 'pmingliu', 'mingliuhkscs', 'plantagenetcherokee', 'kozgoproboldopentype', 'myriadhebrewopentype', 'kozminpr6nboldopentype', 'vrinda', 'aharoni', 
'adventurehollow', 'moolboran', 'vijaya', 'sunriseinternationaldemo', 'andalus', 'arabictypesetting', 'simplifiedarabicfixed', 'frankruehl', 'miriam', 'fangsong', 'chaparralproboldopentype', 'chaparralproitalicopentype', 'jasmineupc', 'acaslonprosemiboldopentype', 'kozgoproregularopentype', 'waitandbleed', 'adobehebrewregularopentype', 'sheilazaindemo', 'amazdoomleft', 'adobegothicstdboldopentype', 'lithosproblackopentype', 'acaslonproregularopentype', 'adobefanheitistdboldopentype', 'adobekaitistdregularopentype', 'agaramondproboldopentype', 'agaramondproitalicopentype', 
'agaramondproregularopentype', 'birchstdopentype', 'kozminproheavyopentype', 'cooperblackstditalicopentype', 'brushscriptstdopentype', 'chaparralprobolditopentype', 'minionprosemiboldopentype', 'chaparralprolightitopentype', 'chaparralproregularopentype', 'charlemagnestdboldopentype', 'cooperblackstdopentype', 'giddyupstdopentype', 'kozgoproextralightopentype', 'kozgoproheavyopentype', 'kozgoprolightopentype', 'kozminproboldopentype', 'kozminproextralightopentype', 'kozminprolightopentype', 'kozminproregularopentype', 'lithosproregularopentype', 'mesquitestdopentype', 'minionproboldcnitopentype', 'minionpromediumitopentype', 'minionprosemibolditopentype', 'nuevastdboldopentype', 'nuevastdboldcondopentype', 'nuevastdboldconditalicopentype', 'nuevastdcondopentype', 'nuevastdconditalicopentype', 'nuevastditalicopentype', 'oratorstdslantedopentype', 'lettergothicstdboldslantedopentype', 'poplarstdopentype', 'rosewoodstdregularopentype', 'tektonproboldopentype', 'tektonproboldextopentype', 'tektonproboldoblopentype', 'trajanproboldopentype', 'adobearabicbolditalicopentype', 'adobearabicitalicopentype', 'adobearabicregularopentype', 'adobedevanagariboldopentype', 'adobedevanagariregularopentype', 'adobehebrewboldopentype', 'adobehebrewbolditalicopentype', 'adobehebrewitalicopentype', 'adobemingstdlightopentype', 'adobesongstdlightopentype', 'kozgopr6nheavyopentype', 'kozminpr6nextralightopentype', 'kozminpr6nlightopentype', 'kozminpr6nmediumopentype', 'lettergothicstdopentype', 'minionproboldopentype', 'minionproitopentype', 'minionproregularopentype', 'myriadproboldcondopentype', 'amazdoomleftoutline', 'myriadprobolditopentype', 'myriadprocondopentype', 'myriadproconditopentype', 'myriadproregularopentype', 'myriadprosemibolditopentype', 'adobedevanagariregular', 'adobedevanagaribold', 'adobedevanagaribolditalic', 'ebonyeyespersonaluse', 'zwadobef', 'wabbitsansregular', 'warisover', 'whiteonblack', 'whoa', 'amazdoomleft2', 'americancaptain', 'amazdoomright', 'amazdoomright2', 'anandablack', 'ananda', 'antlercapsregular', 'barberstreetpersonaluseonly', 'beauty', 'bebasneue', 'bignoodletitling', 'bignoodletitlingoblique', 'blackcoffeeregular', 'blackcoffeeshadow', 'caviardreams', 'champagne', 'limousines', 'cheri', 'cheriliney', 'coolveticargregular', 'curlyshirley', 'getcoffeeregular', 'goodvibes', 'heartbreaker', 'jellycrazies', 'jfwildwood', 'lobster14', 'mayton', 'pokemonsolidnormal', 'rundemo', 'snubnosedemoregular', 'starjedi', 'starjedihollow', 'staywildypersonaluseonly', 'starjedilogodoubleline1', 'starjedilogodoubleline2', 'strangeshadow', 'starjedilogomonoline', 'varsityregular', 'sourcecodeproblack', 'sourcecodepro', 'sourcecodeproextralight', 'sourcecodeprosemibold']

run = True

while run:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

'''

import pygame
import sys

pygame.init()
pygame.font.init()

# Constants for colors
white = (255, 255, 255)
black = (0, 0, 0)
lightBlue = (0, 255, 255)


class Button(): #defining buttonc class
    def __init__(self, text, x, y, width, height, color, text_color):
        # Create a rectangle (rect) for the button
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text  # The text to display on the button
        self.color = color  # The color of the button
        self.text_color = text_color  # The color of the text on the button

    def draw(self, screen):
        # Draw the button on the screen
        pygame.draw.rect(screen, self.color, self.rect, width = 1, border_radius=2)
        font = pygame.font.Font(None, 36)  # Create a font object
        text_surface = font.render(self.text, True, self.text_color)  # Render the text
        text_rect = text_surface.get_rect(center=self.rect.center)  # Center the text on the button
        screen.blit(text_surface, text_rect)  # Blit the text onto the screen

    def is_clicked(self, pos):
        # Check if a given point (pos) is inside the button's rectangle
        return self.rect.collidepoint(pos)

# Initialize the screen and clock
screen_width = 1280
screen_height = 720
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)  # Create the game window
pygame.display.set_caption('My very cool game')  # Set the window title
clock = pygame.time.Clock()  # Create a clock object to control frame rate

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            pygame.quit()
            sys.exit()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button was clicked
            pos = pygame.mouse.get_pos()
            if button1.is_clicked(pos):
                print("Button Clicked!")

    # Create a button
    button1 = Button("Click Me", 640, 360, 100, 50, lightBlue, white)
    button1.draw(screen)  # Draw the button on the screen

    pygame.display.update()  # Update the display to show changes
    clock.tick(60)  # Limit the frame rate to 60 frames per second
import pygame
import time
import random
from constants import *
from textWriter import *
from strings import *
from choices import *
from paths import *
from gameCode import *
import character
#End import list
#Begin game
def main():
#Initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GreyTone")
    pygame.font.init()
    text = FONT.render("", True, constants.TEXTCOLOR)
    textlength = 0
    textBackground = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT//1.2))
    textBackground.fill((0,0,255))
    textBox = text.get_rect()
    textBox.center = TEXTBOX_SIZE
    clock = pygame.time.Clock()
    dt = 0
    block = False
    display = True
    #Insert Groups
    #End Insert Groups
    #Insert Containers
    #End Insert Containers
#End Initialization
#Begin Game Code
    while True:
        screen.fill((0, 0, 0))
        screen.blit(textBackground, (0, SCREEN_HEIGHT//1.3))
        screen.blit(text, textBox)
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
    #Begin Game Math Code
        if textlength == len(TEXTSTRING) + 1:
            if block == False:
                display = not display
                block = True
        else:    
            block = False
        if display:
            text, textlength = textWriter(TEXTSTRING, FONT, textlength, constants.TEXTCOLOR)
            time.sleep(TEXTSPEED)
        elif not display:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                text, textlength = FONT.render("", True, TEXTCOLOR), 0
                display = True
            if keys[pygame.K_2]:
                constants.TEXTCOLOR = (255,0,0)
                text, textlength = FONT.render("", True, TEXTCOLOR), 0
                display = True
            if keys[pygame.K_3]:
                constants.TEXTCOLOR = (255,255,255)
                text, textlength = FONT.render("", True, TEXTCOLOR), 0
                display = True
            if keys[pygame.K_4]:
                constants.TEXTCOLOR = (0,255,0)
                text, textlength = FONT.render("", True, TEXTCOLOR), 0
                display = True
    #End Game Math Code
#End Game Code
#-------------------------------------------------------------------
#Begin Clock Increment
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
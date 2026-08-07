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
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render("GreyTone", True, (255,255,255))
    textBackground = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT//1.2))
    textBackground.fill((0,0,255))
    textBox = text.get_rect()
    textBox.center = TEXTBOX_SIZE
    clock = pygame.time.Clock()
    dt = 0
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
    #End Game Math Code
#End Game Code
#-------------------------------------------------------------------
#Begin Clock Increment
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
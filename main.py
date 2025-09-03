import pygame
import time
import random
from constants import *
from textWriter import textWriter
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
    pygame.display.set_caption("JustAnotherGame")
    clock = pygame.time.Clock()
    dt = 0
#End Initialization
#Insert Groups
#For items that receive updates:
    updateable = pygame.sprite.Group()
#For items that can be drawn:
    drawable = pygame.sprite.Group()
#End Insert Groups

#Insert Containers

#End Insert Containers
#Begin Game Math Code
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        textBox = font.render(text, True, (255, 255, 255))
        
#End Game Math Code
#Begin Game Draw Code
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        screen.blit(textBox, (SCREEN_WIDTH / 8, SCREEN_HEIGHT / 1.5))
#End Game Draw Code
#Begin Clock Increment
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
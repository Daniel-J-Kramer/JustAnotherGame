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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("JustAnotherGame")
    clock = pygame.time.Clock()
    dt = 0
#Insert Groups
#For items that receive updates:
    updateable = pygame.sprite.Group()
#For items that can be drawn:
    drawable = pygame.sprite.Group()
#End Insert Groups

#Insert Containers

#End Insert Containers

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

#Begin Game Math Code
        
#End Game Math Code
#Begin Game Draw Code
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
#End Game Draw Code
#Begin Clock Increment
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
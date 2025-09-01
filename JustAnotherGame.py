import pygame
import time
import random
from constants import *
from textWriter import textWriter
from strings import *
from choices import *
from paths import *
import character
#End import list
#Begin game
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        choicespeed(delay)
        print("")
        time.sleep(.2)
        textWriter(narrator[0], delay)
        time.sleep(1)
        textWriter(narrator[1], delay)
        time.sleep(1)
        textWriter(narrator[2], delay)
        time.sleep(1)
        choice = choicetype(delay)
        print("")
        textWriter(narrator[11], delay)
        time.sleep(1)
        textWriter(narrator[12], delay)
        time.sleep(1)
        textWriter(narrator[13], delay)
        modifier = choicedifficulty(delay)
        time.sleep(1)
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
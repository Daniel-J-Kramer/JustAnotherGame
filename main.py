import pygame
import time
import random
from constants import *
from textWriter import textWriter, Text
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
    pygame.font.init()
#Insert Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
#End Insert Groups
#Insert Containers
    Text.containers = (updateable, drawable)
#End Insert Containers
    string = "Hello World"
    textWriter = Text(string, (1.5 / SCREEN_WIDTH), (1.5 / SCREEN_HEIGHT))
#End Initialization
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
#Begin Game Code

#Begin Game Math Code
        
        
#End Game Math Code
#End Game Code
#Begin Game Draw Code
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        screen.blit(textWriter.font.render(textWriter.string, True, textWriter.color), (textWriter.x, textWriter.y))
#End Game Draw Code
#-------------------------------------------------------------------
#Begin Clock Increment
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
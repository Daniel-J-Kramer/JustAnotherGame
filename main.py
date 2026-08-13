import pygame
import time
import random
from constants import *
from strings import *
from choices import *
from paths import *
from gameCode import *
import character
from Text import Text
#End import list
#Begin game
def main():
#Initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("JustAnotherGame")
    pygame.font.init()
#    updateable = pygame.sprite.Group()
#    drawable = pygame.sprite.Group()

#    Text.containers(updateable, drawable)
    #Initialize Text
    txtmain: Text = Text(MAINSTRING, FONT, TEXTCOLOR, MAINTEXTBOX_SIZE)
    txtmain.step1 = True
    txtquestion: Text = Text(QUESTIONSTRING, FONT, TEXTCOLOR, TEXTQBOX_SIZE)
    txtquestion.step2 = True
    txtstrone: Text = Text(STRINGONE, FONT, TEXTCOLOR, TEXT1BOXSIZE)
    txtstrtwo: Text = Text(STRINGTWO, FONT, TEXTCOLOR, TEXT2BOXSIZE)
    txtstrthree: Text = Text(STRINGTHREE, FONT, TEXTCOLOR, TEXT3BOXSIZE)
    txtstrfour: Text = Text(STRINGFOUR, FONT, TEXTCOLOR, TEXT4BOXSIZE)
    txtstrone.step3 = True
    txtstrtwo.step3 = True
    txtstrthree.step3 = True
    txtstrfour.step3 = True
    #Text Backgrounds
    txtmainBackground = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT//1.2))
    txtmainBackground.fill(MAINTEXTBOXCOLOR)
    txtBackground = pygame.Surface((SCREEN_WIDTH//7, SCREEN_HEIGHT))
    txtBackground.fill(TEXTBOXCOLOR)

    txtmain.get_screen()
    txtquestion.get_screen()
    txtstrone.get_screen()
    txtstrtwo.get_screen()
    txtstrthree.get_screen()
    txtstrfour.get_screen()
    #Text Surfaces
    txtmain.go_get_rect(MAINTEXTBOX_SIZE)
    txtquestion.go_get_rect(TEXTQBOX_SIZE)
    txtstrone.go_get_rect(TEXT1BOXSIZE)
    txtstrtwo.go_get_rect(TEXT2BOXSIZE)
    txtstrthree.go_get_rect(TEXT3BOXSIZE)
    txtstrfour.go_get_rect(TEXT4BOXSIZE)
    #Time Variables and Others
    clock = pygame.time.Clock()
    dt = 0
    block = False
    display = True
#End Initialization
#Begin Game Loop
    while True:
        screen.fill((0, 0, 0))
        screen.blit(txtmainBackground, (0,SCREEN_HEIGHT//1.3))
        screen.blit(txtBackground, (0, 0))
        screen.blit(txtmain.screen, txtmain.pos)
        screen.blit(txtquestion.screen, txtquestion.pos)
        screen.blit(txtstrone.screen, txtstrone.pos)
        screen.blit(txtstrtwo.screen, txtstrtwo.pos)
        screen.blit(txtstrthree.screen, txtstrthree.pos)
        screen.blit(txtstrfour.screen, txtstrfour.pos)
        
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
    #Begin Game Math Code
        if (len(txtstrone.text) + len(txtstrtwo.text) + len(txtstrthree.text) + len(txtstrfour.text)) == (len(txtstrone.written) + len(txtstrtwo.written) + len(txtstrthree.written) + len(txtstrfour.written)):
            if block == False:
                display = not display
                block = True
        else:    
            block = False
        if display:
            txtmain.write_text()
            if len(txtmain.text) == len(txtmain.written):
                txtquestion.write_text()
                if len(txtquestion.text) == len(txtquestion.written):
                    txtstrone.write_text()
                    txtstrtwo.write_text()
                    txtstrthree.write_text()
                    txtstrfour.write_text()

            time.sleep(TEXTSPEED)
        elif not display:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:

                display = True
            if keys[pygame.K_2]:
                txtmain.color = (255,0,0)

                display = True
            if keys[pygame.K_3]:
                txtmain.color = (255,255,255)

                display = True
            if keys[pygame.K_4]:
                txtmain.color = (0,255,0)

                display = True
    #End Game Math Code
#-------------------------------------------------------------------
    #Begin Clock Increment
        dt = clock.tick(60) / 1000
        pygame.display.flip()
    #End Clock Increment
#End Game Loop

if __name__ == "__main__":
    main()
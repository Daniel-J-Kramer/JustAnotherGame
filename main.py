import pygame
import time
import random
from constants import *
from strings import *
from choices import *
from paths import *
from gameCode import *
import Character
from Text import Text 
#End import list
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
texts = pygame.sprite.Group()
#Begin game
def main():
#Initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("JustAnotherGame")
    pygame.font.init()

    #Initialize Groups
    

    #Initialize Text
    txtmain: Text = Text("MAINTEXT", MAINSTRING, FONT, TEXTCOLOR, MAINTEXTBOX_SIZE)
    txtmain.step = True
    txtquestion: Text = Text("QUESTIONTEXT", QUESTIONSTRING, FONT, TEXTCOLOR, TEXTQBOX_SIZE)
    txtstrone: Text = Text("STRINGONE", STRINGONE, FONT, TEXTCOLOR, TEXT1BOXSIZE)
    txtstrtwo: Text = Text("STRINGTWO", STRINGTWO, FONT, TEXTCOLOR, TEXT2BOXSIZE)
    txtstrthree: Text = Text("STRINGTHREE", STRINGTHREE, FONT, TEXTCOLOR, TEXT3BOXSIZE)
    txtstrfour: Text = Text("STRINGFOUR", STRINGFOUR, FONT, TEXTCOLOR, TEXT4BOXSIZE)
    updateable.add(txtmain, txtquestion, txtstrone, txtstrtwo, txtstrthree, txtstrfour)
    drawable.add(txtmain, txtquestion, txtstrone, txtstrtwo, txtstrthree, txtstrfour)
    texts.add(txtmain, txtquestion, txtstrone, txtstrtwo, txtstrthree, txtstrfour)

    #Text Backgrounds
    txtmainBackground = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT//1.2))
    txtmainBackground.fill(MAINTEXTBOXCOLOR)
    txtBackground = pygame.Surface((SCREEN_WIDTH//7, SCREEN_HEIGHT))
    txtBackground.fill(TEXTBOXCOLOR)

    txtmain.get_image()
    txtquestion.get_image()
    txtstrone.get_image()
    txtstrtwo.get_image()
    txtstrthree.get_image()
    txtstrfour.get_image()

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
        drawable.draw(screen)

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
            if txtmain.step == False:
                txtmain.step = True

            updateable.update()

            if len(txtmain.text) == len(txtmain.written):
                txtquestion.step = True
                if len(txtquestion.text) == len(txtquestion.written):
                    txtstrone.step = True
                    txtstrtwo.step = True
                    txtstrthree.step = True
                    txtstrfour.step = True

            time.sleep(TEXTSPEED)
        elif not display:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                for obj in texts:
                    obj.reset_string()
                display = True
            if keys[pygame.K_2]:
                txtmain.color = (255,0,0)
                for obj in texts:
                    obj.reset_string()
                display = True
            if keys[pygame.K_3]:
                txtmain.color = (255,255,255)
                for obj in texts:
                    obj.reset_string()
                display = True
            if keys[pygame.K_4]:
                txtmain.color = (0,255,0)
                for obj in texts:
                    obj.reset_string()
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
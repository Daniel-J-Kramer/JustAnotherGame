import pygame
import time
import random
from constants import *
import choices
from strings import *
import Character
from Text import Text
from getText import getText
#End import list

#Begin game
def main():
#Initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("JustAnotherGame")
    pygame.font.init()

    #Initialize Text
    txtmain: Text = Text("MAINTEXT", MAINSTRING, FONT, TEXTCOLOR, MAINTEXTBOX_SIZE, True)
    txtmain.step = True
    txtquestion: Text = Text("QUESTIONTEXT", QUESTIONSTRING, FONT, TEXTCOLOR, TEXTQBOX_SIZE, True)
    txtstrone: Text = Text("STRINGONE", STRINGONE, FONT, TEXTCOLOR, TEXT1BOXSIZE, True)
    txtstrtwo: Text = Text("STRINGTWO", STRINGTWO, FONT, TEXTCOLOR, TEXT2BOXSIZE, True)
    txtstrthree: Text = Text("STRINGTHREE", STRINGTHREE, FONT, TEXTCOLOR, TEXT3BOXSIZE, True)
    txtstrfour: Text = Text("STRINGFOUR", STRINGFOUR, FONT, TEXTCOLOR, TEXT4BOXSIZE, True)
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
        #Write Texts
        strings_done = False
        for string in texts:
            if (string.done == False):
                strings_done = False
                break
            strings_done = True
            
        if (strings_done):
            if block == False:
                display = not display
                block = True
        else:    
            block = False

        if display:
            if txtmain.step == False:
                txtmain.step = True
                updateable.add(txtmain, txtquestion, txtstrone, txtstrtwo, txtstrthree, txtstrfour)
                drawable.add(txtmain, txtquestion, txtstrone, txtstrtwo, txtstrthree, txtstrfour)
                texts.add(txtmain, txtquestion, txtstrone, txtstrtwo, txtstrthree, txtstrfour)

            updateable.update()

            if len(txtmain.text) == len(txtmain.written):
                txtquestion.step = True
                if len(txtquestion.text) == len(txtquestion.written):
                    txtstrone.step = True
                    txtstrtwo.step = True
                    txtstrthree.step = True
                    txtstrfour.step = True

            time.sleep(TEXTSPEED)
            
        #Make Choices
        elif not display:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                APATH, BPATH, CPATH, DPATH = APATH(APATH, BPATH, CPATH, DPATH)
                print(APATH)
                print(BPATH)
                print(CPATH)
                print(DPATH)
                for obj in texts:
                    obj.reset_string()
                display = True
                strings_done = False
            if keys[pygame.K_2]:
                APATH, BPATH, CPATH, DPATH = BPATH(APATH, BPATH, CPATH, DPATH)
                for obj in texts:
                    obj.reset_string()
                display = True
                strings_done = False
            if keys[pygame.K_3]:
                APATH, BPATH, CPATH, DPATH = CPATH(APATH, BPATH, CPATH, DPATH)
                for obj in texts:
                    obj.reset_string()
                display = True
                strings_done = False
            if keys[pygame.K_4]:
                APATH, BPATH, CPATH, DPATH = DPATH(APATH, BPATH, CPATH, DPATH)
                for obj in texts:
                    obj.reset_string()
                display = True
                strings_done = False

    #End Game Math Code
#-------------------------------------------------------------------
    #Begin Clock Increment
        dt = clock.tick(60) / 1000
        pygame.display.flip()
    #End Clock Increment
#End Game Loop

if __name__ == "__main__":
    main()
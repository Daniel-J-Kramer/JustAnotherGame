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
    #Initialize Text
    txtmain = FONT.render("", True, TEXTCOLOR)
    txtquestion = FONT.render("", True, TEXTCOLOR)
    txtstrone = FONT.render("", True, TEXTCOLOR)
    txtstrtwo = FONT.render("", True, TEXTCOLOR)
    txtstrthree = FONT.render("", True, TEXTCOLOR)
    txtstrfour = FONT.render("", True, TEXTCOLOR)
    #Text Lengths
    txtmainlen = 0
    txtquestionlen = 0
    txtstronelen = 0
    txtstrtwolen = 0
    txtstrthreelen = 0
    txtstrfourlen = 0
    #Text Backgrounds
    txtmainBackground = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT//1.2))
    txtmainBackground.fill(MAINTEXTBOXCOLOR)
    txtBackground = pygame.Surface((SCREEN_WIDTH//7, SCREEN_HEIGHT))
    txtBackground.fill(TEXTBOXCOLOR)
    #Text Surfaces
    txtBoxmain = txtmain.get_rect()
    txtBoxmain.center = MAINTEXTBOX_SIZE
    txtqBox = txtquestion.get_rect()
    txtqBox.center = TEXTQBOX_SIZE
    txt1Box = txtstrone.get_rect()
    txt1Box.center = TEXT1BOXSIZE
    txt2Box = txtstrtwo.get_rect()
    txt2Box.center = TEXT2BOXSIZE
    txt3Box = txtstrthree.get_rect()
    txt3Box.center = TEXT3BOXSIZE
    txt4Box = txtstrfour.get_rect()
    txt4Box.center = TEXT4BOXSIZE
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
        screen.blit(txtmain, txtBoxmain)
        screen.blit(txtquestion, txtqBox)
        screen.blit(txtstrone, txt1Box)
        screen.blit(txtstrtwo, txt2Box)
        screen.blit(txtstrthree, txt3Box)
        screen.blit(txtstrfour, txt4Box)

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
    #Begin Game Math Code
        if txtmainlen == len(MAINSTRING) + 1:
            if block == False:
                display = not display
                block = True
        else:    
            block = False
        if display:
            txtmain, txtmainlen = textWriter(MAINSTRING, FONT, txtmainlen, TEXTCOLOR)
            txtquestion, txtquestionlen = textWriter(QUESTIONSTRING, FONT, txtquestionlen)
            txtstrone, txtstronelen = textWriter(STRINGONE, FONT, txtstronelen)
            txtstrtwo, txtstrtwolen = textWriter(STRINGTWO, FONT, txtstrtwolen)
            txtstrthree, txtstrthreelen = textWriter(STRINGTHREE, FONT, txtstrthreelen)
            txtstrfour, txtstrfourlen = textWriter(STRINGFOUR, FONT, txtstrfourlen)
            time.sleep(TEXTSPEED)
        elif not display:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                txtmain, txtmainlen = FONT.render("", True, TEXTCOLOR), 0
                display = True
            if keys[pygame.K_2]:
                constants.TEXTCOLOR = (255,0,0)
                txtmain, txtmainlen = FONT.render("", True, TEXTCOLOR), 0
                display = True
            if keys[pygame.K_3]:
                constants.TEXTCOLOR = (255,255,255)
                txtmain, txtmainlen = FONT.render("", True, TEXTCOLOR), 0
                display = True
            if keys[pygame.K_4]:
                constants.TEXTCOLOR = (0,255,0)
                txtmain, txtmainlen = FONT.render("", True, TEXTCOLOR), 0
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
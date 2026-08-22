import pygame
from strings import startStrings
from paths import *
pygame.font.init()

#Sprite Groups
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
texts = pygame.sprite.Group()

#Display constants
SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720
MAINTEXTBOX_SIZE: tuple = (int(SCREEN_WIDTH//6.5), int(SCREEN_HEIGHT//1.25))
MAINTEXTBOXCOLOR: tuple = (128,128,128)
TEXTQBOX_SIZE: tuple = (int(SCREEN_WIDTH//90), int(SCREEN_HEIGHT//32))
TEXT1BOXSIZE: tuple = (int(SCREEN_WIDTH//90), int(SCREEN_HEIGHT//5))
TEXT2BOXSIZE: tuple = (int(SCREEN_WIDTH//90), int(SCREEN_HEIGHT//2.5))
TEXT3BOXSIZE: tuple = (int(SCREEN_WIDTH//90), int(SCREEN_HEIGHT//1.67))
TEXT4BOXSIZE: tuple = (int(SCREEN_WIDTH//90), int(SCREEN_HEIGHT//1.25))
TEXTBOXCOLOR: tuple = (0,0,255)

#Text constants
FONTSIZE: int = SCREEN_HEIGHT // 44
FONT: pygame.font.Font = pygame.font.Font('freesansbold.ttf', FONTSIZE)
TEXTCOLOR: tuple = (255,255,255)
MAINSTRING: str = startStrings[0]
QUESTIONSTRING: str = startStrings[1]
STRINGONE: str = startStrings[2]
STRINGTWO: str = startStrings[3]
STRINGTHREE: str = startStrings[4]
STRINGFOUR: str = startStrings[5]
SLOWTEXT: float = .15
NORMAL: float = .1
FASTTEXT: float = .05
TEXTSPEED: float = FASTTEXT

#game states
CHOICE: int = 0
PATH: int = 0
SAVESTATE: int = 0
MODIFIER: float = 0
DELAY: float = .03
APATH = choiceAAA
BPATH = choiceAAB
CPATH = choiceAAC
DPATH = choiceAAD
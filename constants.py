import pygame
pygame.font.init()

#Display constants
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 360
TEXTBOX_SIZE = (int(SCREEN_WIDTH//10), int(SCREEN_HEIGHT//1.2))

#Text constants
FONT = pygame.font.Font('freesansbold.ttf', 16)
TEXTCOLOR = (255,255,255)
TEXTSTRING = "Want to play a game???"
SLOWTEXT = .2
NORMAL = .15
FASTTEXT = .075
TEXTSPEED = NORMAL

#game constants
CHOICE = 0
PATH = 0
SAVESTATE = 0
MODIFIER = 0
DELAY = .03
import time
import pygame
import constants
def textWriter(delay, string, font=pygame.font.SysFont("Comic Sans MS", 24), pos_x=(1.5*constants.SCREEN_WIDTH), pos_y=(1.5*constants.SCREEN_HEIGHT), color=(255, 255, 255)):
    length = len(string)
    char = ""
    finalstring = ""
    for c in range(0, length):
        char = string[c]
        finalstring += char
        time.sleep(delay / 2)
        if c < (length - 1):
            return (finalstring + '\r')
        else:
            return finalstring


        
import time
import pygame
def textWriter(string, delay, font):
    length = len(string)
    char = ""
    finalstring = ""
    for c in range(0, length):
        char = string[c]
        finalstring += char
        time.sleep(delay / 2)
        if c < (length - 1):
            print(finalstring, end='\r')
        else:
            print(finalstring)

class Text():

    def __init__(self, string, x, y, font=pygame.font.SysFont("Comic Sans MS", 24), color=(255, 255, 255)):
        self.name = self
        self.string = string
        self.font = font
        self.color = color
        self.x = x
        self.y = y

    def change_string(self, string, font=pygame.font.SysFont("Comic Sans MS", 24), color=(255, 255, 255)):
        self.string = string
        self.font = font

    def change_pos(self, x, y):
        self.x = x
        self.y = y
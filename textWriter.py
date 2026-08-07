import time
import pygame
import constants
def textWriter(string: str, font: pygame.font.Font, length: int):
    pos = len(string) - length
    if pos == 0:
        return (string[pos])
    else:
        return (string[:pos])
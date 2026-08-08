import time
import pygame
import constants
def textWriter(string: str, font: pygame.font.Font, length: int, color=(255,255,255)):
    new_text = font.render(string[:length], True, color)
    return new_text, (length + 1)
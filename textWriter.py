import time
import pygame
import constants
def textWriter(string: str, font: pygame.font.Font, length: int, color=(255,255,255)):
    new_text = font.render(string[:length], True, color)
    if length < len(string) + 1:
        return new_text, (length + 1)
    else:
        return font.render(string, True, color), length
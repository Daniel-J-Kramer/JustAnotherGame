import pygame
from constants import *
import random



class Text(pygame.sprite.Sprite):

    def __init__(self, text: str, font: pygame.font.Font, color: tuple, pos: tuple):
    #    if hasattr(self, "containers"):
   #         super().__init__(self.containers)
  #      else:
 #           super().__init__()

        self.text: str = text
        self.font: pygame.font.Font = font
        self.color: tuple = color
        self.rect: pygame.rect.Rect | None = None
        self.screen: pygame.Surface = self.font.render("", True, self.color)
        self.length: int = 0
        self.pos: tuple = pos
        self.written: str = ""
        self.step1: bool = False
        self.step2: bool = False
        self.step3: bool = False

    def get_text(self):
        return self.text

    def get_font(self):
        return self.font
    
    def get_color(self):
        return self.color

    def draw(self, screen):
        return FONT.render(self.text, True, self.color)

    def go_get_rect(self, txtbox):
        self.rect = self.screen.get_rect()
        self.rect.center = txtbox

    def get_screen(self):
        self.screen = self.font.render(self.written, True, self.color)

    def write_text(self):
        self.written = self.text[:self.length]
        self.length += 1
        self.get_screen()
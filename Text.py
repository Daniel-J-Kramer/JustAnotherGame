import pygame
from constants import *
import random


class Text(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    def __init__(self, name: str, text: str, font: pygame.font.Font, color: tuple, pos: tuple):

        self.text: str = text
        self.font: pygame.font.Font = font
        self.color: tuple = color
        self.rect: pygame.rect.Rect | None = None
        self.image: pygame.Surface = self.font.render("", True, self.color)
        self.length: int = 0
        self.pos: tuple = pos
        self.written: str = ""
        self.step: bool = False


    def get_text(self):
        return self.text

    def get_font(self):
        return self.font
    
    def get_color(self):
        return self.color

    def draw(self, screen):
        return FONT.render(self.text, True, self.color)

    def update(self):
        if self.step:
            self.write_text()

    def go_get_rect(self, txtbox):
        self.rect = self.image.get_rect()
        self.rect.center = txtbox

    def get_image(self):
        self.image = self.font.render(self.written, True, self.color)

    def write_text(self):
        self.written = self.text[:self.length]
        self.length += 1
        self.get_image()
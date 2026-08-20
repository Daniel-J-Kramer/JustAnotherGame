import pygame
from constants import *
import random
from DefaultObject import DefaultObject


class Text(DefaultObject):
    
    
    def __init__(self, name: str, text: str, font: pygame.font.Font, color: tuple, pos: tuple):
        super().__init__()
        
        self.text: str = text
        self.name = name
        self.font: pygame.font.Font = font
        self.color: tuple = color
        self.rect: pygame.rect.Rect | None = None
        self.image: pygame.Surface = self.font.render("", True, self.color)
        self.length: int = 0
        self.pos: tuple = pos
        self.written: str = ""
        self.step: bool = False
        self.maxlen: int = 18
        if (self.name == "MAINTEXT"):
            self.maxlen = 56

        
        
    def get_text(self):
        return self.text

    def get_font(self):
        return self.font
    
    def get_color(self):
        return self.color

    def draw(self, screen):
        return self.font.render(self.written, True, self.color)

    def update(self):
        if self.step == True:
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
        if (len(self.written) == self.maxlen):
            splits = self.text.split(" ")
            carry = []
            count = 0
            for s in splits:
                count += len(s) + 1
                if count >= 18:
                    count -= len(s) + 1
                    carry.append(s)
                    splits.remove(s)
            self.text = " ".join(splits)
            self.split_string(" ".join(carry), self.pos)
            



    def split_string(self, text, pos):
        new_string = Text(f"{self.name}1",text,FONT,TEXTCOLOR,pos)
        new_string.step = True
        new_string.get_image()
        if self.rect:
            new_string.go_get_rect((self.rect.x, self.rect.y + (SCREEN_HEIGHT // 1)))
        updateable.add(new_string)
        drawable.add(new_string)
        texts.add(new_string)

    def reset_string(self):
        self.written = ""
        self.length = 0
        self.step = False
        self.get_image()
import pygame


class DefaultObject(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10,10))
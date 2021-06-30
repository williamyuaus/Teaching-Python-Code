import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, imagePath, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
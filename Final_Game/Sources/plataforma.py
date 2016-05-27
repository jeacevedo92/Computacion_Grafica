import pygame
from Colors import *

class Plataforma(pygame.sprite.Sprite):
    """ Plataforma donde el usuario puede subir """
    
    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(VERDE)
        
        self.rect = self.image.get_rect()
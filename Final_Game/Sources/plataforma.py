import pygame
from Colors import *

class Plataforma(pygame.sprite.Sprite):
    """ Plataforma donde el usuario puede subir """
    
    def __init__(self, imagen,tipo_modificador):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen)
        
        #self.image = pygame.Surface([ancho, alto])
        #self.image.fill(VERDE)        
        self.rect = self.image.get_rect()

        self.tipo_plataforma = tipo_modificador  #si es 0 no es modificador si es 1 es el primer modificador si es 2 es el segundo....
import pygame
from Colors import *

class Nivel(object):
    """ Esta es una superclase usada para definir un nivel
        Se crean clases hijas por cada nivel que desee emplearse """
    
    # Lista de sprites usada en todos los niveles. Add or remove
    plataforma_lista = None
    enemigos_lista = None
    fatalplat = None

    checkpoin_lista = None

    modificadores = None

    checkpoint = [100,40]
    
    # Imagen de Fondo
    #fondo = None
    fondo=pygame.image.load('../Images/fondo2.png')
    #valor desplazamiento de fondo
    mov_fondo=0
    
    def __init__(self, jugador):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.plataforma_lista = pygame.sprite.Group()
        self.enemigos_lista = pygame.sprite.Group()
        self.fatalplat = pygame.sprite.Group()
        self.modificadores = pygame.sprite.Group()
        self.jugador = jugador
        self.checkpoint = [100,40]
        self.checkpoin_lista = pygame.sprite.Group()
    
    # Actualizamos elementos en el nivel
    def update(self):
        """ Actualiza todo lo que este en este nivel."""
        self.plataforma_lista.update()
        self.enemigos_lista.update()
        self.fatalplat.update()
        self.modificadores.update()
        self.checkpoin_lista.update()

    
    def draw(self, pantalla):
        """ Dibuja lo que se encuentre en el nivel. """
        
        # Dibujamos fondo
        #pantalla.fill(AZUL)
        
        pantalla.blit(self.fondo, (0,0))
        
        # Dibujamos todos los sprites en las listas
        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)
        self.fatalplat.draw(pantalla)
        self.modificadores.draw(pantalla)

        self.checkpoin_lista.draw(pantalla)


    def Mover_fondo(self, mov_x):
        self.mov_fondo += mov_x
        self.checkpoint[0] += mov_x
        for plataforma in self.plataforma_lista:
            plataforma.rect.x += mov_x

        for enemigo in self.enemigos_lista:
            #~ enemigo.rect.x += mov_x
            enemigo.desplazamiento += mov_x

        for plataforma in self.fatalplat:
            plataforma.rect.x += mov_x

        for plataforma in self.modificadores:
            plataforma.rect.x += mov_x

        for plataforma in self.checkpoin_lista:
            plataforma.rect.x += mov_x


            

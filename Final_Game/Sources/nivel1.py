import pygame
from Colors import *
from nivel import *
from plataforma import *

# Creamos variasplataformas para un nivel
class Nivel_01(Nivel):
    """ Definition for level 1. """
    
    def __init__(self, jugador):
        """ Creamos nivel 1. """
        
        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-1000
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [ ["o3.png", 0, 500],
                  ["o3.png", 500, 500],
                  ["o3.png", 1000, 500],
                  ["o3.png", 1500, 500],
                  ["o3.png", 2000, 500],
                 ]
            
        # Go through the array above and add platforms
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0],)
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)
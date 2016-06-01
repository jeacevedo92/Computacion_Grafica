import pygame
from Colors import *
from nivel import *
from plataforma import *


class Nivel_02(Nivel):
    """ Definicion para el nivel 2. """
    
    def __init__(self, jugador):
        """ Creamos nivel 2. """
        
        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-4000
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [

        ["../Images/lava.png",0, 550],
        ["../Images/lava.png",700, 550],
        ["../Images/lava.png",1400, 550],
        ["../Images/lava.png",2100, 550],
        ["../Images/lava.png",2800, 550],
        ["../Images/lava.png",3500, 550],
        ["../Images/lava.png",4200, 550],


        ["../Images/plataforma_alien21.png", 0, 550],
        ["../Images/plataforma_alien21.png", 250, 550],        
        ["../Images/caja_alien.png", 460, 460],



        ["../Images/plataforma_alien2.png", 750, 550],
        ["../Images/caja_alien.png", 1000, 460],
        ["../Images/caja_alien.png", 1200, 460],
        ["../Images/caja_alien.png", 1200, 370],
        ["../Images/plataforma_alien21.png", 1000, 550],


        ["../Images/plataforma_alien2corta.png", 1400, 230],
        ["../Images/plataforma_alien21corta.png", 1500, 230],

        ["../Images/plataforma_alien2corta.png", 2000, 230],
        ["../Images/plataforma_alien21corta.png",2100, 230],

        ["../Images/plataforma_alien2muycorta.png",2400, 300],
        ["../Images/plataforma_alien21muycorta.png",2410, 300],

        ["../Images/plataforma_alien2muycorta.png",2600, 400],
        ["../Images/plataforma_alien21muycorta.png",2610, 400],

        ["../Images/plataforma_alien2.png", 2800, 550],
        ["../Images/plataforma_alien21.png", 3050, 550],

        ["../Images/plataforma_alien2.png", 3300, 550],
        ["../Images/plataforma_alien21.png",3550, 550],

        ["../Images/plataforma_alien2.png", 3500, 550],
        ["../Images/plataforma_alien21.png",3750, 550]         
    
		]
            
        # Go through the array above and add platforms
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

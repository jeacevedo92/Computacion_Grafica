import pygame
from Colors import *
from nivel import *
from plataforma import *

lava = 130

class Nivel_02(Nivel):
    """ Definicion para el nivel 2. """
    
    def __init__(self, jugador):
        """ Creamos nivel 2. """
        
        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-4000
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [

        #lava
        ["../Images/lava_alien.png",lava*0, 590],        
        ["../Images/lava_alien.png",lava*1, 590],
        ["../Images/lava_alien.png",lava*2, 590],
        ["../Images/lava_alien.png",lava*3, 590],
        ["../Images/lava_alien.png",lava*4, 590],
        ["../Images/lava_alien.png",lava*5, 590],
        ["../Images/lava_alien.png",lava*6, 590],
        ["../Images/lava_alien.png",lava*7, 590],
        ["../Images/lava_alien.png",lava*8, 590],
        ["../Images/lava_alien.png",lava*9, 590],
        ["../Images/lava_alien.png",lava*10, 590],
        ["../Images/lava_alien.png",lava*11, 590],
        ["../Images/lava_alien.png",lava*12, 590],
        ["../Images/lava_alien.png",lava*13, 590],
        ["../Images/lava_alien.png",lava*14, 590],
        ["../Images/lava_alien.png",lava*15, 590],
        ["../Images/lava_alien.png",lava*16, 590],
        ["../Images/lava_alien.png",lava*17, 590],
        ["../Images/lava_alien.png",lava*18, 590],
        ["../Images/lava_alien.png",lava*19, 590],
        ["../Images/lava_alien.png",lava*20, 590],      
        ["../Images/lava_alien.png",lava*21, 590],
        ["../Images/lava_alien.png",lava*22, 590],
        ["../Images/lava_alien.png",lava*23, 590],
        ["../Images/lava_alien.png",lava*24, 590],
        ["../Images/lava_alien.png",lava*25, 590],
        ["../Images/lava_alien.png",lava*26, 590],
        ["../Images/lava_alien.png",lava*27, 590],
        ["../Images/lava_alien.png",lava*28, 590],
        ["../Images/lava_alien.png",lava*29, 590],

        ["../Images/lava_alien.png",lava*30, 590],      
        ["../Images/lava_alien.png",lava*31, 590],
        ["../Images/lava_alien.png",lava*32, 590],
        ["../Images/lava_alien.png",lava*33, 590],
        ["../Images/lava_alien.png",lava*34, 590],
        ["../Images/lava_alien.png",lava*35, 590],
        ["../Images/lava_alien.png",lava*36, 590],
        ["../Images/lava_alien.png",lava*37, 590],
        ["../Images/lava_alien.png",lava*38, 590],
        ["../Images/lava_alien.png",lava*39, 590],


        ["../Images/lava_alien.png",lava*40, 590],      
        ["../Images/lava_alien.png",lava*41, 590],
        ["../Images/lava_alien.png",lava*42, 590],
        ["../Images/lava_alien.png",lava*43, 590],
        ["../Images/lava_alien.png",lava*44, 590],
        ["../Images/lava_alien.png",lava*45, 590],
        ["../Images/lava_alien.png",lava*46, 590],
        ["../Images/lava_alien.png",lava*47, 590],
        ["../Images/lava_alien.png",lava*48, 590],
        ["../Images/lava_alien.png",lava*49, 590],

            


        ["../Images/plataforma_alien21.png", 0, 550],
        ["../Images/plataforma_alien21.png", 250, 550],        
        ["../Images/caja_alien.png", 460, 460],



        ["../Images/plataforma_alien2.png", 750, 550],
        ["../Images/caja_alien.png", 1000, 460],
        ["../Images/caja_alien.png", 1200, 460],
        #["../Images/caja_alien.png", 1200, 370],
        ["../Images/plataforma_alien21.png", 1000, 550],


        ["../Images/plataforma_alien2corta.png", 1400, 230],
        ["../Images/plataforma_alien21corta.png", 1500, 230],

        ["../Images/plataforma_alien2corta.png", 2000, 230],
        ["../Images/plataforma_alien21corta.png",2100, 230],

        ["../Images/plataforma_alien2corta.png", 2600, 230],
        ["../Images/plataforma_alien21corta.png",2700, 230],


        ["../Images/plataforma_alien2muycorta.png",3000, 300],
        ["../Images/plataforma_alien21muycorta.png",3010, 300],

        ["../Images/plataforma_alien2muycorta.png",3200, 400],
        ["../Images/plataforma_alien21muycorta.png",3210, 400],

        ["../Images/plataforma_alien2muycorta.png",3400, 500],
        ["../Images/plataforma_alien21muycorta.png",3410, 500],

        ["../Images/plataforma_alien2.png", 3500, 550],
        ["../Images/plataforma_alien21.png", 3750, 550],

        ["../Images/plataforma_alien2.png", 3750, 550],
        ["../Images/plataforma_alien21.png",4000, 550],

        ["../Images/plataforma_alien2.png", 4000, 550],
        ["../Images/plataforma_alien21.png",4250, 550],
         
    
		]
            
        # Go through the array above and add platforms
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

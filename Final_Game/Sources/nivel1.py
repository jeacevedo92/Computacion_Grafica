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
        self.limite = -3000

        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [


                 
                  ["o3.png", 0, 500],
                  ["o3.png", 500, 500],
                  #["o3.png", 1000, 500],

                  ["o3.png", 1500, 500],
                  #["o3.png", 2000, 500],
                  #["o3.png", 2500, 500],
                  #["o3.png", 3000, 500],

                  ["cajita1.png", 2000, 520],


                  #["arbusto1.png", 500, 100],


                  ["o4.png", 2000, 550],

                  


                  ["cajita.png", 500, 455],                 
                  ["cajita.png", 595, 455],
                  ["cajita.png", 690, 455],

                  ["cajita1.png", 500, 410],                
                  ["cajita1.png", 700, 410],
                  ["cajita1.png", 700, 365],

                  ["cajita1.png", 700, 320],


                  ["cajita.png", 700, 455],                 
                  ["cajita.png", 795, 455],
                  ["cajita.png", 890, 455],

                  ["cajita1.png", 700, 410],                
                  ["cajita1.png", 900, 410],
                  ["cajita1.png", 900, 365],

                  ["puas.png", 2500, 520],
                  ["puas.png", 2620, 520],
                  ["puas.png", 2720, 520],
                  ["puas.png", 2820, 520],
                  #["puas.png", 900, 365],


                 # ["plataforma2.png", 810, 200],

                  #["plataforma1.png", 800, 180],                  
                  ["plataforma1_2.png", 900, 180],                  
                  ["plataforma1_2.png", 1300, 180],            

                

                  #["plataforma2_1.png", 1100, 200],

                  #["plataforma2.png", 1500, 200],


                  ["cajita.png", 1500, 455],                 
                  ["cajita.png", 1595, 455],
                  ["cajita.png", 1690, 455],

                  ["cajita1.png", 1500, 410],                
                  ["cajita1.png", 1700, 410],



                
                  
                  


                  


                 ]
            
        # Go through the array above and add platforms
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0],)
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)
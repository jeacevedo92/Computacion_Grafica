import pygame
from Colors import *
from nivel import *
from plataforma import *
from Enemy import *
# Creamos variasplataformas para un nivel
class Nivel_01(Nivel):
    """ Definition for level 1. """
    
    def __init__(self, jugador):
        """ Creamos nivel 1. """
        
        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite = -4000

        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [
					
                  ["../Images/o3.png", 0, 500],
                  ["../Images/o3.png", 500, 500],
                  ["../Images/o3.png", 1500, 500],
                  
                  ["../Images/o4.png", 2000, 550],
                  
                  ["../Images/bloquepiedra.png", 1900, 350],
                  
                  ["../Images/cajita.png", 500, 455],                 
                  ["../Images/cajita.png", 595, 455],
                  ["../Images/cajita.png", 690, 455],

                  ["../Images/cajita1.png", 500, 410],                
                  ["../Images/cajita1.png", 700, 410],
                  ["../Images/cajita1.png", 700, 365],

                  ["../Images/cajita.png", 700, 455],                 
                  ["../Images/cajita.png", 795, 455],
                  ["../Images/cajita.png", 890, 455],

                  ["../Images/cajita1.png", 700, 410],                
                  ["../Images/cajita1.png", 900, 410],
                  ["../Images/cajita1.png", 900, 365],
                  ["../Images/cajita1.png", 900, 320],
                  
                  ["../Images/plataforma1_2.png", 2500, 400],
                  ["../Images/plataforma1_2.png", 2750, 300],
                  ["../Images/plataforma1_2.png", 3000, 400],

                  ["../Images/puas.png", 2500, 520],
                  ["../Images/puas.png", 2620, 520],
                  ["../Images/puas.png", 2740, 520],
                  ["../Images/puas.png", 2860, 520],
                  ["../Images/puas.png", 2980, 520],
                  
                  ["../Images/o4.png", 3100, 550],
                  ["../Images/o4.png", 3600, 550],
                  
                  ["../Images/puas.png", 4100, 520],
                  ["../Images/puas.png", 4220, 520],
                  ["../Images/roca1.png", 4340, 540],
                  ["../Images/puas.png", 4504, 520],
                  ["../Images/puas.png", 4624, 520],
                  
                  ["../Images/o4.png", 4740, 550],
                                  
                  ["../Images/plataforma1_2.png", 1005, 180],                  
                  ["../Images/plataforma1_2.png", 1400, 180],

                  ["../Images/cajita.png", 1500, 455],                 
                  ["../Images/cajita.png", 1595, 455],
                  ["../Images/cajita.png", 1690, 455],

                  ["../Images/cajita1.png", 1500, 410],                
                  ["../Images/cajita1.png", 1700, 410],  
                 ]
        enemis = [
        ["../Images/robot.png",550,420],
        #["../Images/robot.png",600,0],
        #["../Images/robot.png",700,0]
        ]

            
        # Go through the array above and add platforms
        for plataforma in nivel:

          #Plataformas
          bloque = Plataforma(plataforma[0])
          bloque.rect.x = plataforma[1]
          bloque.rect.y = plataforma[2]
          bloque.jugador = self.jugador
          self.plataforma_lista.add(bloque)


        for enemigo in enemis:
          e = Enemy(enemigo[0],5)
          e.rect.x = enemigo[1]
          e.rect.y = enemigo[2]
          self.enemigos_lista.add(e) 


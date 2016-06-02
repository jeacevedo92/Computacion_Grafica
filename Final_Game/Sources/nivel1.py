import pygame
from Colors import *
from nivel import *
from plataforma import *
from Enemy import *

def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo)
    imagen_ancho, imagen_alto = imagen.get_size()
    tabla_fondos = []  
      
    for fondo_x in range(0, imagen_ancho/ancho):
       linea = []
       tabla_fondos.append(linea)
       for fondo_y in range(0, imagen_alto/alto):
            cuadro = (fondo_x * ancho, fondo_y * alto, ancho, alto)
            linea.append(imagen.subsurface(cuadro))
    return tabla_fondos
    
sec_der_r = cargar_fondo('../Images/robot.png', 46 , 48)
sec_izq_r = cargar_fondo('../Images/robot_izq.png', 46 , 48)

sec_der_a = cargar_fondo('../Images/alien_derecha.png', 148, 75)
sec_izq_a = cargar_fondo('../Images/alien_izquierda.png', 148, 75)

sec_der_m = cargar_fondo('../Images/mutante_der.png', 44, 75)
sec_izq_m = cargar_fondo('../Images/mutante_izq.png', 44, 75)

sec_der_m1 = cargar_fondo('../Images/zombie_der.png', 51, 69)
sec_izq_m1 = cargar_fondo('../Images/zombie_izq.png', 51, 69)

sec_der_z = cargar_fondo('../Images/zoomer.png', 30, 21)

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

                  
                  
                  ["../Images/o4.png", 3100, 550],
                  ["../Images/o4.png", 3600, 550],
                  
                  
                  ["../Images/roca1.png", 4340, 540],
                
                  
                  ["../Images/o4.png", 4740, 550],
                                  
                  ["../Images/plataforma1_2.png", 1005, 180],                  
                  ["../Images/plataforma1_2.png", 1400, 180],

                  ["../Images/cajita.png", 1500, 455],                 
                  ["../Images/cajita.png", 1595, 455],
                  ["../Images/cajita.png", 1690, 455],

                  ["../Images/cajita1.png", 1500, 410],                
                  ["../Images/cajita1.png", 1700, 410] 
                 ]
                 
        enemis = [
        ["../Images/robot.png",550,420,130,sec_der_r,sec_izq_r,6],
        ["../Images/robot.png",750,420,110,sec_der_r,sec_izq_r,6],
        ["../Images/robot.png",1550,440,110,sec_der_z,sec_der_z,6],
        ["../Images/robot.png",1790,485,80,sec_der_z,sec_der_z,6],
        ["../Images/robot.png",2200,485,230,sec_der_m,sec_izq_m,12],
        
        ["../Images/robot.png",3050,485,310,sec_der_m1,sec_izq_m1,8],
        ["../Images/robot.png",3400,485,130,sec_der_m,sec_izq_m,12],
        ["../Images/robot.png",3600,485,180,sec_der_m1,sec_izq_m1,8]
        ]

        fatalplat =[
        ["../Images/puas.png", 2500, 520],
        ["../Images/puas.png", 2620, 520],
        ["../Images/puas.png", 2740, 520],
        ["../Images/puas.png", 2860, 520],
        ["../Images/puas.png", 2980, 520],

        ["../Images/puas.png", 4100, 520],
        ["../Images/puas.png", 4220, 520],
        ["../Images/puas.png", 4504, 520],
        ["../Images/puas.png", 4624, 520],
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
          e = Enemy(enemigo[0],5,enemigo[1],enemigo[2],enemigo[3],enemigo[4],enemigo[5],enemigo[6])
          e.rect.x = enemigo[1]
          e.rect.y = enemigo[2]
          self.enemigos_lista.add(e) 

        for plataformaf in fatalplat:

          #Plataformas
          bloque = Plataforma(plataformaf[0])
          bloque.rect.x = plataformaf[1]
          bloque.rect.y = plataformaf[2]
          bloque.jugador = self.jugador
          self.fatalplat.add(bloque)


import pygame
from Colors import *
from nivel import *
from plataforma import *
from Enemy import *
from nivel import *
from nivel1 import *
from Bresenham1 import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self,imagen,velocidad,x,y,distancia,sec_der,sec_izq,num_sprites):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()#
        self.disparar= random.randrange(200)# tiempo para disparar cada 200 pixeles 
        self.recorrido_ida = Bresenham1(x,y,x+distancia,y)
        self.cont = 0
        self.velocidad = velocidad
        
        self.direccion = True #True = derecha, False = izquierda
        self.desplazamiento = 0
        
        self.sec_der = sec_der
        self.sec_izq = sec_izq
        self.cont_imagen = 0
        self.limit = num_sprites


    def update(self):

        if self.cont < len(self.recorrido_ida):
            
            posicion = self.recorrido_ida[self.cont]
            self.rect.x = posicion[0] + self.desplazamiento
            self.rect.y = posicion[1]
            self.cont += self.velocidad

            if self.cont_imagen < self.limit:
                if self. direccion:
                    self.image = self.sec_der[self.cont_imagen][0]
                else:
                    self.image = self.sec_izq[self.cont_imagen][0]
                self.cont_imagen +=1
            else:
                self.cont_imagen =0

        else:
            self.recorrido_ida = self.recorrido_ida[::-1]
            self.cont = 0

            self.direccion = not self.direccion

        self.disparar-=1#va reduciendo el tiempo de disparo en 1 hasta que llegue a 0 y vuelve a disparar
        
        if self.disparar < 0:
            self.disparar = random.randrange(200)


def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo)
    imagen_ancho, imagen_alto = imagen.get_size()
    #print 'ancho: ', imagen_ancho, ' xmax: ', imagen_ancho/ancho
    #print 'alto: ',imagen_alto, ' ymax: ', imagen_alto/alto
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



class Nivel_02(Nivel):
    """ Definicion para el nivel 2. """
    
    def __init__(self, jugador):
        """ Creamos nivel 2. """
        
        # Llamamos al padre
        Nivel.__init__(self, jugador)
        self.limite=-4000
        # Arreglo con ancho, alto, x, y de la plataforma
        nivel = [      


        ["../Images/plataforma_alien21.png", 0, 520],
        ["../Images/plataforma_alien21.png", 250, 520],        
        ["../Images/caja_alien.png", 460, 430],



        ["../Images/plataforma_alien2.png", 750, 520],
        ["../Images/caja_alien.png", 1000, 430],
        ["../Images/caja_alien.png", 1200, 430],
        ["../Images/caja_alien.png", 1200, 340],
        ["../Images/plataforma_alien21.png", 1000, 520],


        ["../Images/plataforma_alien2corta.png", 1400, 230],
        ["../Images/plataforma_alien21corta.png", 1500, 230],

        ["../Images/plataforma_alien2corta.png", 2000, 230],
        ["../Images/plataforma_alien21corta.png",2100, 230],

        ["../Images/plataforma_alien2muycorta.png",2400, 300],
        ["../Images/plataforma_alien21muycorta.png",2410, 300],

        ["../Images/plataforma_alien2muycorta.png",2600, 400],
        ["../Images/plataforma_alien21muycorta.png",2610, 400],

        ["../Images/plataforma_alien2.png", 2800, 520],
        ["../Images/plataforma_alien21.png", 3050, 520],

        ["../Images/plataforma_alien2.png", 3300, 520],
        ["../Images/plataforma_alien21.png",3550, 520],

        ["../Images/caja_alien1.png",3780, 450],


               
    
		]

        enemys = [
        ["../Images/robot.png",1400,220,170,sec_der_z,sec_der_z,6],
        ["../Images/robot.png",2000,220,170,sec_der_z,sec_der_z,6],

        #["../Images/robot.png",2200,485,230,sec_der_m,sec_izq_m,12],        
        #["../Images/robot.png",3050,485,310,sec_der_m1,sec_izq_m1,8],
        #["../Images/robot.png",3400,485,130,sec_der_m,sec_izq_m,12],
        #["../Images/robot.png",3600,485,180,sec_der_m1,sec_izq_m1,8]
        ]

        fatalplat =[
        ["../Images/lava.png",0, 550],
        ["../Images/lava.png",700, 550],
        ["../Images/lava.png",1400, 550],
        ["../Images/lava.png",2100, 550],
        ["../Images/lava.png",2800, 550],
        ["../Images/lava.png",3500, 550],
        ["../Images/lava.png",4200, 550],
        ]

            
        # Go through the array above and add platforms
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.plataforma_lista.add(bloque)

        for enemigo in enemys:
          e = Enemy (enemigo[0],5,enemigo[1],enemigo[2],enemigo[3],enemigo[4],enemigo[5],enemigo[6])
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

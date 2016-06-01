import pygame, random
from pygame.locals import *
from Main import *
#import Bresenham
from Bresenham1 import *
#from Bresenham2 import *
WIDTH = 800
HIGH = 600

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

secuencia_derecha = cargar_fondo('../Images/robot.png', 46 , 48)
secuencia_izq = cargar_fondo('../Images/robot_izq.png', 46 , 48)

class Enemy(pygame.sprite.Sprite):
	def __init__(self,imagen,velocidad):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()#
		self.direccion = 0#direccion 0 = de izquierda a derecha
		self.disparar= random.randrange(200)# tiempo para disparar cada 200 pixeles	
		#self.tipo = random.randrange(1,4)
		self.recorrido_ida = Bresenham1(550,420,680,420)
		self.cont = 0
		self.velocidad = velocidad
		self.cont_imagen = 0
		self.direccion = 1

	def update(self):

		if self.cont < len(self.recorrido_ida):

			self.rect.x,self.rect.y = self.recorrido_ida[self.cont]
			self.cont += self.velocidad

			if self.cont_imagen < 6:
				if self. direccion == 1:
					self.image = secuencia_derecha [self.cont_imagen][0]
				else:
					self.image = secuencia_izq [self.cont_imagen][0]
				self.cont_imagen +=1
			else:
				self.cont_imagen =0

		else:
			self.recorrido_ida = self.recorrido_ida[::-1]
			self.cont = 0

			self.direccion = 0

		self.disparar-=1#va reduciendo el tiempo de disparo en 1 hasta que llegue a 0 y vuelve a disparar
		
		if self.disparar < 0:
			self.disparar = random.randrange(200)

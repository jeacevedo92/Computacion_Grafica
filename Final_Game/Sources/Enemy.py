import pygame, random
from pygame.locals import *
from Main import *
from Bresenham1 import *
WIDTH = 800
HIGH = 600

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

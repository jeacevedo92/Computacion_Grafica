import pygame, random
#import Bresenham
from Bresenham1 import *
from Bresenham2 import *
WIDTH = 800
HIGH = 600


class Enemy1(pygame.sprite.Sprite):
	def __init__(self,imagen,velocidad):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()#
		self.direccion = 0#direccion 0 = de izquierda a derecha
		self.disparar= random.randrange(200)# tiempo para disparar cada 200 pixeles	
		self.tipo = random.randrange(1,4)
		self.recorrido_ida = CircleMidPoint(random.randrange(100,150))
		self.cont = 0
		self.velocidad = velocidad

	def update(self):
		
		if self.cont < len(self.recorrido_ida):

			self.rect.x,self.rect.y = self.recorrido_ida[self.cont]
			self.cont +=self.velocidad
		else:
			#self.recorrido_ida = self.recorrido_ida[::-1]
			self.cont = 0

		self.disparar-=1#va reduciendo el tiempo de disparo en 1 hasta que llegue a 0 y vuelve a disparar
		
		if self.disparar < 0:
			self.disparar = random.randrange(200)


import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self,imagen,direc):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.velocidad=5
		self.jugador=1
		self.direccion = direc# 1 dispara a la derecha   0 dispara a la izquierda
		
	def update(self):
		if self.direccion == 1:
			if self.jugador == 1:
				self.rect.x+=5     
			else:
				self.rect.x+=5
		else:
			if self.jugador == 1:
				self.rect.x-=5     
			else:
				self.rect.x-=5
			
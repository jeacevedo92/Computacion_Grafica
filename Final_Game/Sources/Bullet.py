import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.velocidad=5
		self.jugador=1
		
	def update(self):
		if self.jugador == 1:  # el jugador 1 es la nave el jugador 0 son los enemigos 
			self.rect.x+=5     
		else:
			self.rect.x+=5
			
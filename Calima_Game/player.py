import pygame

class Player(pygame.sprite.Sprite):	
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.vida = 3   # puntos de vida 
		self.salud = 1000

	def chocar(self):
		self.vida = 0
	def Me_dieron(self):
		self.salud -=5

	def Set_Image(self,imagen):
		self.image = pygame.image.load(imagen).convert_alpha()
	
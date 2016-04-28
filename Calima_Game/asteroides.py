import pygame, random


class Asteroide(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()#

	def update(self):
		self.rect.x +=random.randrange(-1,1)
		self.rect.y += 5 

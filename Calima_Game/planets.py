import pygame, random


class Planets(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()#

	def update(self):		
		dire = random.randrange(0,1)
		self.rect.x +=dire
		self.rect.y += 1

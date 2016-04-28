import pygame
#dimensiones de la pantalla
WIDTH = 800
HIGH = 600

class Player(pygame.sprite.Sprite):	
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.vida = 4   # puntos de vida 
		self.salud = 600  #

	def chocar(self):
		self.vida -= 1
		self.rect.x =WIDTH/2-70
		self.rect.y =HIGH-70

	def Me_dieron(self):
		self.salud -=5

	def Set_Image(self,imagen):
		self.image = pygame.image.load(imagen).convert_alpha()

	def Set_Salud(self,salud):
		self.salud = salud

	def Set_Vidas (self,Vida):
		self.vida= Vida

	def Get_Vidas(self):
		return self.vida

	def Get_salud(self):
		return self.salud
	
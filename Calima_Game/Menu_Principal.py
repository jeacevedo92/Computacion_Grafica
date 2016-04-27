import pygame

ROSADO = (255,105,180)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
GRIS = (150, 150 , 150)


class Menu_Principal:

	ver = False

	def __init__(self,text,pos, pantalla, fuente):
		self.text = text
		self.pos = pos
		self.pantalla = pantalla
		self.fuente = fuente
		self.get_tam()
		self.set_rect()
		self.draw()

	def draw(self):
		self.set_rend()
		self.pantalla.blit(self.rend, self.rect)

	

	def set_rend(self):
		self.rend = self.fuente.render(self.text, True, self.get_color())


	def get_color(self):
		if self.ver:
			return ROSADO
		else:
			return GRIS

	def set_rect(self):
		self.set_rend()
		self.rect = self.rend.get_rect()
		self.rect.topleft = self.pos


	def get_tam(self):
		self.set_rend()
		return self.rend.get_rect()
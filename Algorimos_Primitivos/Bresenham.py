import pygame
import sys

ROJO = (255,0,0)
AZUL = (0,0,255)
BLANCO= (255,255,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)


# ancho y alto de la pantalla
ANCHO=600
ALTO=400

# crear pantalla
pygame.init()
pantalla = pygame.display.set_mode([ANCHO,ALTO])

def Bresenham(x0,y0,x1,y1):


	dx = x1-x0
	dy = y1-y0

	if dy < 0:
		dy = -dy
		stepy = -1
	else:
		stepy = 1

	if dx < 0:
		dx = -dx 
		stepx = -1
	else:
		stepx = 1
	x = x0
	y = y0

	pantalla.set_at((int(x0),int(y0)), AZUL)

	if dx>dy:
		p = 2*dy - dx
		incE = 2*dy
		incNE = 2*(dy-dx)

		while x != x1:
			x = x + stepx

			if p < 0:
				p = p + incE
			else:
				y = y + stepy
				p = p + incNE

			pantalla.set_at((int(x),int(y)), AZUL)

	else:
		p = 2*dx - dy
		incE = 2*dx
		incNE = 2*(dx-dy)

		while y != y1:
			y = y + stepy

			if p < 0:
				p = p + incE

			else:
				x = x + stepx
				p = p + incNE

			pantalla.set_at((int(x),int(y)), AZUL)


punto_inicial = [100,100]
punto_final = [100,300]

Bresenham (punto_inicial[0],punto_inicial[1],punto_final[0],punto_final[1])

#####################
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
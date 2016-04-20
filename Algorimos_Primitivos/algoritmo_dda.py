import pygame
import sys

AZUL = (0,0,255)

# ancho y alto de la pantalla
ANCHO=600
ALTO=400

# crear pantalla
pygame.init()
pantalla = pygame.display.set_mode([ANCHO,ALTO])


def DDA(x0,y0,x1,y1):
	dx = x1-x0
	dy = y1-y0

	steps = 0

	if abs(dx) > abs(dy):
		steps=abs(dx)
	else:
		steps=abs(dy)

	xinc = dx /float(steps)
	yinc = dy /float(steps)

	x = x0
	y = y0

	pantalla.set_at((int(x),int(y)), AZUL)


	for k in range(1,steps): 
		x = x + xinc
		y = y + yinc		
		pantalla.set_at((int(x),int(y)), AZUL)

punto_inicial = [400,100]
punto_final = [100,50]

DDA (punto_inicial[0],punto_inicial[1],punto_final[0],punto_final[1])

#####################
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)



	

import pygame
import random
BLANCO = (255,255,255)

#constantes
WIDTH = 640
HIGH = 512

def cargar_fondo(archivo,ancho,alto):
	imagen =  pygame.image.load(archivo).convert()
	imagen_ancho, imagen_alto = imagen.get_size()

	tabla_fondos = []

	for fondo_x in range (0, imagen_ancho/alto):
		linea = []
		tabla_fondos.append(linea)

		for fondo_y in range (0,imagen_alto/alto):
			cuadro = (fondo_x*ancho,fondo_y*alto,ancho,alto)
			linea.append(imagen.subsurface(cuadro))
	return  tabla_fondos


if __name__ == '__main__':

	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HIGH))
	pantalla.fill(BLANCO)


	fondos = cargar_fondo('Images/terrenogen.png',32,32)
	pantalla.blit(fondos[0][0],(100,100))

	pygame.display.flip()
	terminar = False
	while not terminar:
		tecla = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminar = True

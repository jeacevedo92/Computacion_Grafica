import pygame
import random

#constantes
WIDTH = 1000
HIGH = 700


class Enemy(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()#
		self.direccion = 0#direccion 0 = de izquierda a derecha
		self.disparar=random.randrange(200)# tiempo para disparar cada 200 pixeles 
		
	def update(self):
		if self.rect.x >= (WIDTH-100):
			self.direccion=1  #cuando llega al extremo derecho cambia la direccion! 1 = der a izq 
		if self.rect.x <= 0: 
			self.direccion=0 #cuando llegan al extremo izquierdo cambia la direccion! 
			
		if self.direccion == 0:
			self.rect.x+=3
		else:
			self.rect.x-=3
			
		self.disparar-=1#va reduciendo el tiempo de disparo en 1 hasta que llegue a 0 y vuelve a disparar
		
		if self.disparar < 0:
			self.disparar = random.randrange(200)
			
		
class Player(pygame.sprite.Sprite):	
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.vida = 100   # puntos de vida 
		
	def chocar(self):
		self.vida -=10

class Bullet(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		#self.velocidad=5
		self.jugador=1
		
	def update(self):
		if self.jugador == 1:  # el jugador 1 es la nave el jugador 0 son los enemigos 
			self.rect.y-=5     
		else:
			self.rect.y+=5
		


if __name__ == '__main__':

	#se crea  la pantalla 
	pygame.init()
	SCREEN = pygame.display.set_mode([WIDTH,HIGH])
	
	#Se  cargan las imagenes
	bullet = pygame.image.load('Images/Bullet.png').convert_alpha()
	background = pygame.image.load('Images/Background_3.png').convert_alpha()
	sound = pygame.mixer.Sound('Sound/sound.wav')
	
	#Se coloca la imagen de fondo
	SCREEN.blit(background, [0,0])
	
	#se hace invisible el cursor
	pygame.mouse.set_visible(False)

	#inicializa el reloj 
	reloj = pygame.time.Clock()
	
	#Puntaje del juego
	puntos = 0
	
	############################################################
	#pos = pygame.mouse.get_pos()
	#xship = pos[0]
	#yship = pos[1]
	#ship = pygame.image.load('Player.png').convert_alpha()
	#SCREEN.blit(ship, [xship,yship])
	# enemigo = pygame.image.load.('enemigo.png').convert_alpha()
	###########################################################


	# se crean las listas para todos los objetos 
	ls_todos =  pygame.sprite.Group()
	ls_enemigos =  pygame.sprite.Group()
	ls_balae =  pygame.sprite.Group()
	ls_balas =  pygame.sprite.Group()
	ls_jugadores = pygame.sprite.Group()
 
	#se crea el jugador 
	jugador = Player('Images/sprite_ship.png')
	
	#se obtiene la posicion del mouse 
	pos = pygame.mouse.get_pos()

	#se coloca la nave en la posicion donde se encuentre el mouse
	jugador.rect.x=pos[0]
	jugador.rect.y=pos[1]

	#se agrega el jgador a la lista todos y a la lista jugadores	
	ls_todos.add(jugador)
	ls_jugadores.add(jugador)
	

	#se crean n enemmigos y se agregan a las  listas 
	for i in range(5):
		enemigo = Enemy('Images/enemy.png')
		enemigo.rect.x=random.randrange(WIDTH-100)
		enemigo.rect.y=random.randrange(0,HIGH-300)
		ls_enemigos.add(enemigo)
		ls_todos.add(enemigo)
		
	xbullet = pos[0]+95 
	ybullet = pos[1]+50
	
	pygame.display.flip()
	end = False
	
	while not end:
		pos = pygame.mouse.get_pos()
		xship = pos[0]
		yship = pos[1]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True
			elif event.type == pygame.MOUSEBUTTONDOWN:	# si doy clic se crea una bala			
				#shot = True
				#xbullet = pos[0] + 170
				#ybullet = pos[1]
				sound.play()
				bala = Bullet('Images/Bullet.png')
				bala.rect.x= pos[0]+95
				bala.rect.y= pos[1]+50
				ls_balas.add(bala)
				ls_todos.add(bala)
		
		#para los impactos entre las balas de la nave y los enemigos
		for b in ls_balas:
			ls_impactos = pygame.sprite.spritecollide(b,ls_enemigos,True)
			for impacto in ls_impactos:
				ls_balas.remove(b)
				ls_todos.remove(b)
				puntos+=1
				print puntos


		#choques entre el jugador y los enemigos 
		ls_choque = pygame.sprite.spritecollide(jugador,ls_enemigos,False)
		
		for elemento in ls_choque:			
			jugador.chocar()
		#########################################


		#impactos de las balas enemigas al jugador 
		for be in ls_balae:
			impactos = pygame.sprite.spritecollide(be,ls_jugadores,False)
			
			for imp in impactos:
				jugador.chocar()
				ls_balae.remove(be)
				ls_todos.remove(be)
				
			
		#actualiza el fondo y el movimiento del jugador	
		SCREEN.blit(background, [0,0])
		jugador.rect.x= pos[0]
		jugador.rect.y= pos[1]
		
		
		#para los disparos de los enemigos
		for e in ls_enemigos:
			if e.disparar ==0:
				balae = Bullet('Images/Bullet.png')
				balae.jugador = 0
				balae.rect.x = e.rect.x+50
				balae.rect.y = e.rect.y+90
				ls_balae.add(balae)
				ls_todos.add(balae)
		

		#se actualiza el juego !!!!	
		ls_todos.update()
		ls_todos.draw(SCREEN)
	
		
		pygame.display.flip()
		reloj.tick(80)
	

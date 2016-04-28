import pygame
import random
import sys
import Enemy
from Menu_Principal import *
from Bullet import *
from Enemy import *
from Enemy1 import *
from player import *
from pygame.locals import *
import time
from asteroides import *



#dimensiones de la pantalla
WIDTH = 800
HIGH = 600

contador = 0
#se crean n enemmigos y se agregan a las  listas 	
def crearOrda(ls_enemigos,ls_todos,num,vel):
	for i in range(num):
		enemigo = Enemy('Images/enemy'+str(random.randrange(1,4))+'.png',vel)
		enemigo.rect.x=random.randrange(WIDTH-64)
		enemigo.rect.y=random.randrange(HIGH-200)
		ls_enemigos.add(enemigo)
		ls_todos.add(enemigo)

def crearOrda1(ls_enemigos,ls_todos,num,vel):
	for i in range(num):
		enemigo = Enemy1('Images/enemy'+str(random.randrange(1,4))+'.png',vel)
		enemigo.rect.x=random.randrange(WIDTH-64)
		enemigo.rect.y=random.randrange(HIGH-200)
		ls_enemigos.add(enemigo)
		ls_todos.add(enemigo)

def animacion_explocion(fondo,ls_todos,pantalla,archivo,x,y):

	reloj = pygame.time.Clock()
	imagen =  pygame.image.load(archivo).convert_alpha()
	imagen_ancho, imagen_alto = imagen.get_size()

	tabla_fondos = []

	for fondo_x in range (0, imagen_ancho/192):
		linea = []
		tabla_fondos.append(linea)

		for fondo_y in range (0,imagen_alto/192):
			cuadro = (fondo_x*192,fondo_y*192,192,192)
			linea.append(imagen.subsurface(cuadro))
	#for i in tabla_fondos:
	#	for j in i:
	pantalla.blit(tabla_fondos,(x,y))
	pygame.display.flip()
	#pantalla.blit(fondo,(0,0))
	#ls_todos.update()	

if __name__ == '__main__':

	#CREA PANTALLA --------------------------------------------
	pygame.init()
	SCREEN = pygame.display.set_mode([WIDTH,HIGH])
	pygame.display.set_caption(" Calima Game ")


	#PARA PUNTAJES---------------------------------------------
	guardar_p = open("puntajes.txt","a")
	ver_p = open ("puntajes.txt","r")
	listado = ver_p.readline()
	listapn = []

	while listado != "":
		resul = int(listado)
		listapn.append(resul)
		listado = ver_p.readline()
	listapn.sort()
	listapn.reverse()
	ver_p.close()
	#-------------------------------------------------------------

	#CARGA DE IMAGENES --------------------------------------------------------------------
	
	bullet = pygame.image.load('Images/Bullet.png').convert_alpha()	
	lifemask = pygame.image.load('Images/lifemask.png').convert_alpha()


	#imagenes barra de salud
	barra_vida1 = pygame.image.load('Images/barra_vida1.png').convert_alpha()
	barra_vida2 = pygame.image.load('Images/barra_vida2.png').convert_alpha()
	barra_vida3 = pygame.image.load('Images/barra_vida3.png').convert_alpha()
	barra_vida4 = pygame.image.load('Images/barra_vida4.png').convert_alpha()
	barra_vida5 = pygame.image.load('Images/barra_vida5.png').convert_alpha()
	barra_vida6 = pygame.image.load('Images/barra_vida6.png').convert_alpha()

	#Se crea el Objeto jugador
	jugador = Player('Images/sprite_ship.png')
	
	#imagenes vidas 
	vida1 = pygame.image.load('Images/vida1.png').convert_alpha()
	vida2 = pygame.image.load('Images/vida2.png').convert_alpha()
	vida3 = pygame.image.load('Images/vida3.png').convert_alpha()
	vida4 = pygame.image.load('Images/vida4.png').convert_alpha()


	#jugador_nivel2 = Player('Images/sprite_ship_shooting_laser.png')	
	
	#fondos
	background_nivel1 = pygame.image.load('Images/Background2.png').convert_alpha()
	background_neblina = pygame.image.load('Images/backgroundtransp.png').convert_alpha()
	fondoMenu_principal = pygame.image.load('Images/fondo_Menu.png')
	background_nivel2 = pygame.image.load('Images/Background1.png').convert_alpha()
	
	#tipoFuente ------------------------------------
	fuente_Menu = pygame.font.Font(None, 40)
	fuente_instrucciones = pygame.font.Font(None, 30)

	
	#Se cargan los sonidos---------------------------------------------
	sound = pygame.mixer.Sound('Sounds/sound.wav')#sonido del disparo 
	explosion = pygame.mixer.Sound('Sounds/explosion.wav')
	Me_dieron = pygame.mixer.Sound('Sounds/Me_dieron.wav')
	Loser = pygame.mixer.Sound('Sounds/loser.wav')
	disparo_enemigo = pygame.mixer.Sound('Sounds/laser4.wav')


	#Se coloca la imagen de fondo-----------
	SCREEN.blit(background_nivel1, [0,0])
	SCREEN.blit(lifemask,[0,HIGH-70])

	#se hace invisible el cursor------------
	pygame.mouse.set_visible(False)

	#inicializa el reloj-------------------- 
	reloj = pygame.time.Clock()

	

	# se crean las listas para todos los objetos----------------- 
	ls_todos =  pygame.sprite.Group()
	ls_jugadores = pygame.sprite.Group()
	ls_enemigos = pygame.sprite.Group()
	ls_balas = pygame.sprite.Group()
	ls_balae =  pygame.sprite.Group()
	ls_asteroides = pygame.sprite.Group()
	ls_planetas = pygame.sprite.Group()
		
	#SE POSICIONA EL JUGADOR ------------------------------------------------------------
	jugador.rect.x =WIDTH/2-70
	jugador.rect.y =HIGH-70

	#se agrega el jugador creado a las listas---------------------
	ls_todos.add(jugador)
	ls_jugadores.add(jugador)


	#Menu_principal----------------------------------------------------------------
	nuevo = Menu_Principal("NUEVA PARTIDA", (198,94), SCREEN, fuente_Menu)
	nuevo_tam = nuevo.get_tam()

	cargar = Menu_Principal("REGISTRO DE PUNTAJE", (145,212), SCREEN, fuente_Menu)
	cargar_tam = cargar.get_tam()

	intr = Menu_Principal("INSTRUCCIONES", (180,400), SCREEN, fuente_Menu)
	intr_tam = intr.get_tam()
	#----------------------------------------------------------------------------


	#------------------------ menu instrucciones--------------------------------------------
	sig = Menu_Principal("SIGUIENTE", (550,550), SCREEN, fuente_instrucciones)
	sig_tam = sig.get_tam()

	iniciar_partida = Menu_Principal("INICIAR PARTIDA", (300,550), SCREEN, fuente_instrucciones)
	iniciar_tam = iniciar_partida.get_tam()

	volver_ini = Menu_Principal("VOLVER AL INICIO", (50,550), SCREEN, fuente_instrucciones)
	volver_tam = volver_ini.get_tam()
	#-----------------------------------------------------------------------------------------


	#variables de control del juego ---------------------------------------------------------

	num_enemigos = 0
	end = False
	#Puntaje del juego-----------------------
	puntos = 0

	opciones = [nuevo, cargar, intr]
	opciones_int = [sig, iniciar_partida, volver_ini ]
	inicio_j = False
	inst_j = False
	pausa = False
	registro = False 
	inst_c = 0
	fin_instruccion = False
	inteCont = 0
	intro = False

	nivel1 = True
	nivel2 = False

	time_ast = 0


	SCREEN.blit(fondoMenu_principal,(0,0))# pantallazo inicial----------------------------------

	#CICLO DEL JUEGO ----------------------------------------------
	while not end:

		keys_down = pygame.key.get_pressed()

		#MENU PRINCIPAL ---------------------------------------------------------------------

	#----------------------menu principal---------------------------------------------------------
		if not inicio_j and not inst_j :
			#se hace invisible el cursor------------
			pygame.mouse.set_visible(True)
			SCREEN.blit(fondoMenu_principal,(0,0))
			pygame.event.pump()
			for opc in opciones:
				if opc.rect.collidepoint(pygame.mouse.get_pos()):
					opc.ver = True
				else:
					opc.ver = False

				opc.draw()
			pygame.display.update()	
	#----------------------------------------------------------------------------------------------	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True

			if keys_down[K_SPACE]:
				Bala = Bullet('Images/sprite_laser_1.png')
				sound.play()
				Bala.rect.x = jugador.rect.x+15
				Bala.rect.y = jugador.rect.y
				ls_balas.add(Bala)
				ls_todos.add(Bala)
			
		#----boton nueva partida-------------------------------------------------------------------------------
		if not inicio_j and not inst_j and not registro:
			if event.type == pygame.MOUSEBUTTONDOWN and 198 <= event.pos[0] <= (198 + nuevo_tam.width) and 94 <= event.pos[1] <= (94 + nuevo_tam.height) :
				inicio_j = True
				intro = True
				inteCont = 0
				puntos = 0
#------------------------------------------------------------------------------------------------------------		
			if event.type == pygame.MOUSEBUTTONDOWN and 145 <= event.pos[0] <= (145 + cargar_tam.width) and 212 <= event.pos[1] <= (212 + cargar_tam.height) :
				registro = True
#-------boton instrucciones-----------------------------------------------------------------------------------
			if event.type == pygame.MOUSEBUTTONDOWN and 180 <= event.pos[0] <= (180 + intr_tam.width) and 400 <= event.pos[1] <= (400 + intr_tam.height) :
				inst_j = True
				fin_instruccion = False
				inst_c = 0

		#INSTRUCCIONES DEL JUEGO----------------------------------------------------------------
		if inst_j and inst_c <= 1:
			pygame.mouse.set_visible(True)
			SCREEN.fill(NEGRO)
			instru = pygame.image.load('Images/'+str(inst_c)+'.png')
			SCREEN.blit(instru,(0,0))
			pygame.event.pump()

			for op in opciones_int:
				if op.rect.collidepoint(pygame.mouse.get_pos()):
					op.ver = True
				else:
					op.ver = False

				op.draw()

			pygame.display.update()	
			pygame.display.flip()

			
			if inst_j:
				if event.type == pygame.MOUSEBUTTONDOWN and not fin_instruccion and 550 <= event.pos[0] <= (550 + sig_tam.width) and 550 <= event.pos[1] <= (550 + sig_tam.height) :
					inst_c += 1
					fin_instruccion = True

				if event.type == pygame.MOUSEBUTTONDOWN  and 300 <= event.pos[0] <= (300 + iniciar_tam.width) and 550 <= event.pos[1] <= (550 + iniciar_tam.height) :
					inicio_j = True
					inst_j = False
					intro = True
					puntos = 0
					inteCont = 0


				if event.type == pygame.MOUSEBUTTONDOWN  and 50 <= event.pos[0] <= (50 + volver_tam.width) and 550 <= event.pos[1] <= (550 + volver_tam.height) :
					inst_j = False


		#INICIA EL JUEGO --------------------------------------------------
		#------------------------------nivel 1 ---------------------------
		
		if inicio_j and nivel1:
			time_ast = random.randrange(0,400)
			if time_ast == 3:
				asteroide = Asteroide('Images/asteroid'+str(random.randrange(1,3))+'.png')
				asteroide.rect.x=random.randrange(WIDTH-100)
				asteroide.rect.y=0
				ls_asteroides.add(asteroide)
				ls_todos.add(asteroide)

			pygame.mouse.set_visible(False)

			intro = False

			if keys_down[K_UP]:
				if jugador.rect.y > 0 :
					jugador.rect.y -=2
			if keys_down[K_DOWN]:
				if jugador.rect.y < HIGH-70 :
					jugador.rect.y += 2
			if keys_down[K_LEFT]:
				if jugador.rect.x > 0:
					jugador.rect.x -=2
			if keys_down[K_RIGHT]:
				if jugador.rect.x < WIDTH-70:
					jugador.rect.x +=2


			if num_enemigos <25:
				if len(ls_enemigos)==0:
					crearOrda(ls_enemigos,ls_todos,num_enemigos,1)
					crearOrda1(ls_enemigos,ls_todos,num_enemigos,1)
					num_enemigos+=5
			else:
				num_enemigos = 0
				nivel2 = True
				nivel1 = False
				jugador.Set_Image('Images/sprite_ship_shooting_plasma.png')


			#para los impactos entre las balas de la nave y los enemigos
			for b in ls_balas:
				ls_impactos = pygame.sprite.spritecollide(b,ls_enemigos,True)			
				for impacto in ls_impactos:
					ls_balas.remove(b)
					ls_todos.remove(b)
					#animacion_explocion(background,ls_todos,SCREEN,'Images/explosion_enemigos.png',b.rect.x-100,b.rect.y-100)
					explosion.play()
					puntos+=1

			#choques entre el jugador y los enemigos 
			ls_choque = pygame.sprite.spritecollide(jugador,ls_enemigos,False)
			
			for elemento in ls_choque:			
				jugador.chocar()
				explosion.play()



			#para los disparos de los enemigos
			for e in ls_enemigos:
				if e.disparar == 0:
					disparo_enemigo.play()
					balae = Bullet('Images/Bullet.png')
					balae.jugador = 0
					balae.rect.x = e.rect.x+50
					balae.rect.y = e.rect.y+90
					ls_balae.add(balae)
					ls_todos.add(balae)

			#impactos de las balas enemigas al jugador 
			for be in ls_balae:
				impactos = pygame.sprite.spritecollide(be,ls_jugadores,False)			
				for imp in impactos:
					#print jugador.salud
					jugador.Me_dieron()
					ls_balae.remove(be)
					ls_todos.remove(be)
					Me_dieron.play()

			if jugador.salud <= 0:
				jugador.vida-=1
				jugador.salud = 600
				#print "jugador.salud"
				#print jugador.salud

			if jugador.vida == 0 :
				#print "termino el juego"
				explosion.play()
				Loser.play()
				end = True
				#print "jugador.vida"
				#print jugador.vida
			
			
			#se actualiza el juego !!!!	
			SCREEN.blit(background_nivel1, [0,0])
			SCREEN.blit(background_neblina, [0,0])		
			SCREEN.blit(lifemask,[0,HIGH-70])
			if jugador.vida == 1:
				SCREEN.blit(vida1,(10,550))
			elif jugador.vida == 2:
				SCREEN.blit(vida1,(10,550))
				SCREEN.blit(vida2,(40,550))
			elif jugador.vida == 3:
				SCREEN.blit(vida1,(10,550))
				SCREEN.blit(vida2,(40,550))
				SCREEN.blit(vida3,(70,550))
			elif jugador.vida == 4:
				SCREEN.blit(vida1,(10,550))
				SCREEN.blit(vida2,(40,550))
				SCREEN.blit(vida3,(70,550))
				SCREEN.blit(vida4,(100,550))

			if jugador.salud <= 600 and jugador.salud >= 500:
				SCREEN.blit(barra_vida1,(700,550))
			elif jugador.salud <= 500 and jugador.salud >= 400:
				SCREEN.blit(barra_vida2,(700,550))
			elif jugador.salud <= 400 and jugador.salud >= 300:
				SCREEN.blit(barra_vida3,(700,550))
			elif jugador.salud <= 300 and jugador.salud >= 200:
				SCREEN.blit(barra_vida4,(700,550))
			elif jugador.salud <= 200 and jugador.salud >= 100:
				SCREEN.blit(barra_vida5,(700,550))
			elif jugador.salud <= 100 and jugador.salud >= 0:
				SCREEN.blit(barra_vida6,(700,550))


			ls_todos.update()
			ls_todos.draw(SCREEN)
			pygame.display.flip()
			reloj.tick(80)


		# nivel 2  ----------------------------------------------------------------------------------
		if inicio_j and nivel2:
			pygame.mouse.set_visible(False)	

			if keys_down[K_UP]:
				if jugador.rect.y > 0 :
					jugador.rect.y -=2
			if keys_down[K_DOWN]:
				if jugador.rect.y < HIGH-70 :
					jugador.rect.y += 2
			if keys_down[K_LEFT]:
				if jugador.rect.x > 0:
					jugador.rect.x -=2
			if keys_down[K_RIGHT]:
				if jugador.rect.x < WIDTH-70:
					jugador.rect.x +=2


			if num_enemigos <20:
				if len(ls_enemigos)==0:
					crearOrda(ls_enemigos,ls_todos,num_enemigos,3)
					crearOrda1(ls_enemigos,ls_todos,num_enemigos,3)
					num_enemigos+=5
			else:
				end = True
				#print "FIn juego"

			#para los impactos entre las balas de la nave y los enemigos
			for b in ls_balas:
				ls_impactos = pygame.sprite.spritecollide(b,ls_enemigos,True)			
				for impacto in ls_impactos:
					ls_balas.remove(b)
					ls_todos.remove(b)
					#animacion_explocion(background,ls_todos,SCREEN,'Images/explosion_enemigos.png',b.rect.x-100,b.rect.y-100)
					explosion.play()
					puntos+=1

			#choques entre el jugador y los enemigos 
			ls_choque = pygame.sprite.spritecollide(jugador,ls_enemigos,False)
			
			for elemento in ls_choque:			
				jugador.chocar()


			#para los disparos de los enemigos
			for e in ls_enemigos:
				if e.disparar == 0:
					disparo_enemigo.play()
					balae = Bullet('Images/Bullet.png')
					balae.jugador = 0
					balae.rect.x = e.rect.x+50
					balae.rect.y = e.rect.y+90
					ls_balae.add(balae)
					ls_todos.add(balae)

			#impactos de las balas enemigas al jugador 
			for be in ls_balae:
				impactos = pygame.sprite.spritecollide(be,ls_jugadores,False)			
				for imp in impactos:
					jugador.Me_dieron()
					ls_balae.remove(be)
					ls_todos.remove(be)
					Me_dieron.play()

			if jugador.salud == 0:
				jugador.vida-=1
				jugador.salud = 600
				#print "jugador.salud"
				#print jugador.salud

			if jugador.vida == 0 :
				#print "termino el juego"
				explosion.play()
				Loser.play()
				reloj.tick(5)
				end = True
				#print "jugador.vida"
				#print jugador.vida


			print jugador.salud

			#se actualiza el juego !!!!	
			SCREEN.blit(background_nivel2, [0,0])
			SCREEN.blit(background_neblina, [0,0])		
			SCREEN.blit(lifemask,[0,HIGH-70])
			ls_todos.update()
			ls_todos.draw(SCREEN)
			pygame.display.flip()
			reloj.tick(80)


 
		           



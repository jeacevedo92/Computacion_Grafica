import pygame
from pygame.locals import *
import sys
import pygame.locals

from Colors import *
from Bullet import *

from nivel1 import *
from Player import *
from plataforma import *
from nivel import *

import random


#dimensiones de la pantalla
ALTO = 600
ANCHO = 800


def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo).convert_alpha()
    imagen_ancho, imagen_alto = imagen.get_size()
    #print 'ancho: ', imagen_ancho, ' xmax: ', imagen_ancho/ancho
    #print 'alto: ',imagen_alto, ' ymax: ', imagen_alto/alto
    tabla_fondos = []  
      
    for fondo_x in range(0, imagen_ancho/ancho):
       linea = []
       tabla_fondos.append(linea)
       for fondo_y in range(0, imagen_alto/alto):
            cuadro = (fondo_x * ancho, fondo_y * alto, ancho, alto)
            linea.append(imagen.subsurface(cuadro))
    return tabla_fondos 
  

 
if __name__ == '__main__':

  #CREA PANTALLA --------------------------------------------
  pygame.init()
  pantalla = pygame.display.set_mode([ANCHO,ALTO])
  pygame.display.set_caption(" Super Space Smash ")

  #Se cargan los sonidos---------------------------------------------
  sound = pygame.mixer.Sound("sound.wav")#sonido del disparo 

  #player = pygame.image.load('Player1.png').convert_alpha() #quieto
  secuenciaderecha = cargar_fondo("secuenciaderecha.png", 48 , 57) #movimiento


  secuenciaizquierda = cargar_fondo("secuenciaizquierda.png",48,57)
  secuenciasalto = cargar_fondo("secuenciasalto.png",51,63,)
  secuenciadisparo_der = cargar_fondo("secuenciadisparo_der.png",71,53)
  secuenciadisparo_izq = cargar_fondo("secuenciadisparo_izq.png",71,53)



  agachado = pygame.image.load("agachado.png").convert_alpha()
  parado = pygame.image.load("Player1.png").convert_alpha()
  parado_izq = pygame.image.load("Player1_izq.png").convert_alpha()

  bajando = secuenciasalto[2][0]

  # Creamos jugador
  jugador = Jugador('Player1.png')

  # Creamos los niveles
  nivel_lista = []
  nivel_lista.append( Nivel_01(jugador) )

  # Establecemos nivel actual
  nivel_actual_no = 0
  nivel_actual = nivel_lista[nivel_actual_no]


  # Lista de sprites activos
  activos_sp_lista = pygame.sprite.Group()
  # Indicamos a la clase jugador cual es el nivel
  jugador.nivel = nivel_actual


  ##############################
  # se crean las listas para todos los objetos----------------- 
  ls_todos =  pygame.sprite.Group()
  #ls_jugadores = pygame.sprite.Group()
  #ls_enemigos = pygame.sprite.Group()
  ls_balas = pygame.sprite.Group()
  #ls_balae =  pygame.sprite.Group()
  #ls_asteroides = pygame.sprite.Group()
  #ls_planetas = pygame.sprite.Group()


  jugador.rect.x = 300
  jugador.rect.y = 40
  activos_sp_lista.add(jugador) 

  fin = False
    
  # Controlamos que tan rapido actualizamos pantalla
  reloj = pygame.time.Clock()

  contador_moverderecha = 0
  contador_moverizquierda = 0
  contador_disparo_derecha = 0
  contador_disparo_izquierda = 0
  contador_salto = 0
  
  tiempo = 10
  actual = 0
  
  # -------- Ciclo del juego -----------
  while not fin:

      keys_down = pygame.key.get_pressed()

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              fin = True

          if keys_down[K_SPACE]:
            if jugador.direccion == 1:
              jugador.disparo_derecha(secuenciadisparo_der,contador_disparo_derecha)
            else:
              jugador.disparo_izquierda(secuenciadisparo_izq,contador_disparo_izquierda)

            Bala = Bullet('bullet.png')
            sound.play()
            Bala.rect.x = jugador.rect.x+15
            Bala.rect.y = jugador.rect.y
            ls_balas.add(Bala)
            #activos_sp_lista.add(Bala)
            ls_todos.add(Bala)

      if keys_down[K_LEFT]:
        jugador.direccion = 0
        jugador.ir_izq(secuenciaizquierda,contador_moverizquierda)

        if contador_moverizquierda < 5:
          contador_moverizquierda += 1
        else:
          contador_moverizquierda = 0

      if keys_down[K_RIGHT]:
        jugador.direccion = 1

        jugador.ir_der(secuenciaderecha,contador_moverderecha)
                   
        if contador_moverderecha < 5:
          contador_moverderecha += 1
        else:
          contador_moverderecha = 0

      if keys_down[K_UP]:

        jugador.salto(secuenciasalto)

        if contador_salto < 5:
          contador_salto += 1
        else:
          contador_salto = 0


      if keys_down[K_DOWN]:
        jugador.agacharse(agachado)

      if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT and jugador.vel_x < 0:
              jugador.no_mover(parado,parado_izq)
          if event.key == pygame.K_RIGHT and jugador.vel_x > 0:
              jugador.no_mover(parado,parado_izq)

      # Actualizamos al jugador.
      activos_sp_lista.update(parado,bajando)
  
      # Actualizamos elementos en el nivel
      nivel_actual.update()

      #  Si el jugador se aproxima al limite derecho de la pantalla (-x)
      if jugador.rect.x >= 500:
          dif = jugador.rect.x - 500
          jugador.rect.x = 500
          nivel_actual.Mover_fondo(-dif)

      # Si el jugador se aproxima al limite izquierdo de la pantalla (+x)
      if jugador.rect.x <= 120:
         dif = 120 - jugador.rect.x
         jugador.rect.x = 120
         nivel_actual.Mover_fondo(dif)

      #Si llegamos al final del nivel
      pos_actual=jugador.rect.x + nivel_actual.mov_fondo
      if pos_actual < nivel_actual.limite:
         jugador.rect.x=120
         if nivel_actual_no < len(nivel_lista)-1:
            nivel_actual_no += 1
            nivel_actual = nivel_lista[nivel_actual_no]
            jugador.nivel=nivel_actual

      # Dibujamos y refrescamos
      ls_todos.update()
      ls_todos.draw(pantalla)
      pygame.display.flip()

      nivel_actual.draw(pantalla)
      activos_sp_lista.draw(pantalla)
      reloj.tick(60)
      pygame.display.flip()

if __name__ == "__main__":
  main()
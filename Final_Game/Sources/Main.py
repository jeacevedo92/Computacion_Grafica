import pygame
from pygame.locals import *
import sys
import pygame.locals

from Colors import *
from Bullet import *

from nivel1 import *
from nivel2 import *
from Player import *
from plataforma import *
from nivel import *
from Menu import *
from Enemy import *
import time

import random


#dimensiones de la pantalla
ALTO = 600
ANCHO = 800

imagen_bala = '../Images/bullet.png'
imagen_bala_normal = '../Images/bullet.png'
imagen_gun1 = '../Images/gun_1.png'
imagen_gun2 = '../Images/gun_2.png'
imagen_gun3 = '../Images/gun_3.png'
imagen_gun4 = '../Images/gun_4.png'

imagen_gun5 = '../Images/bala_traje.png'

def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo)
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


jugador_der_n = pygame.image.load('../Images/Player1.png')
jugador_izq_n = pygame.image.load('../Images/Player1_izq.png')
jugador_der_t = pygame.image.load('../Images/traje_der.png')
jugador_izq_t = pygame.image.load('../Images/traje_izq.png')
agachado_dern = pygame.image.load('../Images/agachado.png')
agachado_izqn = pygame.image.load('../Images/agachado_izq.png')
agachado_dert = pygame.image.load('../Images/traje_agachado_der.png')
agachado_izqt = pygame.image.load('../Images/traje_agachado_izq.png')
jugador_disparo_dern = pygame.image.load('../Images/disparo.png')
jugador_disparo_izqn = pygame.image.load('../Images/disparo_izq.png')
jugador_disparo_dert = pygame.image.load('../Images/traje_disparo_der.png')
jugador_disparo_izqt = pygame.image.load('../Images/traje_disparo_izq.png')
jugador_saltoder_n = pygame.image.load('../Images/bajando_derecha.png')
jugador_saltoizq_n = pygame.image.load('../Images/bajando_izq.png')
jugador_saltoder_t = pygame.image.load('../Images/salto_traje_der.png')
jugador_saltoizq_t = pygame.image.load('../Images/salto_traje_izq.png')
caminata_der_n = cargar_fondo('../Images/secuenciaderecha.png', 48, 57)
caminata_izq_n = cargar_fondo('../Images/secuenciaizquierda.png', 48, 57)
caminata_der_t = cargar_fondo('../Images/caminatatraje.png', 76, 69)
caminata_izq_t = cargar_fondo('../Images/caminatatraje_izq.png', 76, 69)
cont_mover_dern = 5
cont_mover_izqn = 5
cont_mover_dert = 27
cont_mover_izqt = 27

jugador_der = jugador_der_n
jugador_izq = jugador_izq_n
jugadordisparo_der = jugador_disparo_dern
jugadordisparo_izq = jugador_disparo_izqn
salto_der = jugador_saltoder_n
salto_izq = jugador_saltoizq_n
caminata_der = caminata_der_n
caminata_izq = caminata_izq_n
agachado_der = agachado_dern
agachado_izq = agachado_izqn
contador_moverdertotal = cont_mover_dern
contador_moverizqtotal = cont_mover_izqn
  

 
if __name__ == '__main__':

  #CREA PANTALLA ------------------------------------------------------------------
  pygame.init()
  pantalla = pygame.display.set_mode([ANCHO,ALTO])
  pygame.display.set_caption(" Super Space Smash ")


  #Se cargan los sonidos------------------------------------------------------------
  sound = pygame.mixer.Sound('../Sounds/sound.wav')#sonido del disparo 
  explosion = pygame.mixer.Sound('../Sounds/explosion.wav')
  Me_dieron = pygame.mixer.Sound('../Sounds/Me_dieron.wav')
  Loser = pygame.mixer.Sound('../Sounds/loser.wav')
  disparo_enemigo = pygame.mixer.Sound('../Sounds/laser4.wav')
  sonido_fondo = pygame.mixer.Sound('../Sounds/Thunderstruck.wav')
  mod = pygame.mixer.Sound('../Sounds/life.wav')

  sonido_fondo = pygame.mixer.Sound('../Sounds/Thunderstruck.wav')



  #Menu Principal--------------------------------------------------------------------
  menu=Menu()
  opciones=['Nuevo', 'Continuar', 'Salir']
  menu.opciones=opciones

  menu_pause = Menu()
  opciones_pause = ['Reanudar' ,'opciones ', 'Salir']
  menu_pause.opciones = opciones_pause



  game_over = gaste =pygame.image.load('../Images/game_over.png').convert_alpha()


  #player = pygame.image.load('Player1.png').convert_alpha() #quieto
  #secuenciaderecha = cargar_fondo('../Images/secuenciaderecha.png', 48, 57) #movimiento
  #secuenciaizquierda = cargar_fondo('../Images/secuenciaizquierda.png',48,57)

  #disparo = pygame.image.load('../Images/disparo.png')
  #disparo_izquierda = pygame.image.load('../Images/disparo_izq.png')

  #agachado = pygame.image.load('../Images/agachado.png').convert_alpha()
  #agachado_izq = pygame.image.load('../Images/agachado_izq.png').convert_alpha()

  #parado = pygame.image.load('../Images/Player1.png').convert_alpha()
  #parado_izq = pygame.image.load('../Images/Player1_izq.png').convert_alpha()

  #subiendo = pygame.image.load('../Images/subiendo_derecha.png').convert_alpha()
  #subiendo_izq = pygame.image.load('../Images/subiendo_izq.png').convert_alpha()

  #bajando = pygame.image.load('../Images/bajando_derecha.png').convert_alpha()
  #bajando_izq = pygame.image.load('../Images/bajando_izq.png').convert_alpha()


  #secuenciasalto = cargar_fondo("../Images/secuenciasalto.png",51,63,)
  #secuenciadisparo_der = cargar_fondo('../Images/secuenciadisparo_der.png',71,53)
  #secuenciadisparo_izq = cargar_fondo('../Images/secuenciadisparo_izq.png',71,53)
  
  fondonivel2 = pygame.image.load('../Images/fondonivel2.jpg')

  history_1 = pygame.image.load('../Images/metabaron/history_1.png')
  history_2 = pygame.image.load('../Images/metabaron/history_2.png')
  history_3 = pygame.image.load('../Images/metabaron/history_3.png')
  history_4 = pygame.image.load('../Images/metabaron/history_4.png')



  #imagenes barra de salud
  barra_vida1 = pygame.image.load('../Images/barra_vida1.png').convert_alpha()
  barra_vida2 = pygame.image.load('../Images/barra_vida2.png').convert_alpha()
  barra_vida3 = pygame.image.load('../Images/barra_vida3.png').convert_alpha()
  barra_vida4 = pygame.image.load('../Images/barra_vida4.png').convert_alpha()
  barra_vida5 = pygame.image.load('../Images/barra_vida5.png').convert_alpha()
  barra_vida6 = pygame.image.load('../Images/barra_vida6.png').convert_alpha()


  vida1 = pygame.image.load('../Images/vida1.png').convert_alpha()
  vida2 = pygame.image.load('../Images/vida2.png').convert_alpha()
  vida3 = pygame.image.load('../Images/vida3.png').convert_alpha()
  
  lifemask = pygame.image.load('../Images/lifemask.png').convert_alpha()
  background_neblina = pygame.image.load('../Images/backgroundtransp.png').convert_alpha()


  fondoMenu_principal = pygame.image.load('../Images/metabaron/menu_ppl.png')
  fondo_pause = pygame.image.load('../Images/metabaron/menu_pause.png')

  
  #bajando = secuenciasalto[2][0]

  # Creamos jugador
  jugador = Jugador('../Images/Player1.png')

  # Creamos los niveles
  nivel_lista = []
  nivel_lista.append( Nivel_01(jugador) )
  nivel_lista.append( Nivel_02(jugador) )

  # Establecemos nivel actual
  nivel_actual_no = 1
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

  game_init = False
  history = False
  pausa = False

  #posiciones del check point
  cp_x = 300
  cp_y = 40

  menu_principal = True

  
  sonido_fondo.play()
  # -------- Ciclo del juego -----------
  while not fin:
      
      keys_down = pygame.key.get_pressed()

      #Menu Principal-------------------------------------------------------------

      if menu_principal:
        
        pygame.mouse.set_visible(True)
        pantalla.blit(fondoMenu_principal,(0,0))
       

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            fin = True

          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
              menu.abajo()
            if event.key == pygame.K_UP:
              menu.arriba()
            if event.key == pygame.K_RETURN:
              menu.seleccion=menu.nop

        #nuevo juego
        if menu.seleccion==1:          
          print"nuevo"
          menu.seleccion=0
          menu_principal = False
          history = True

        if menu.seleccion==2:
          print"nuevo"
          menu.seleccion=0
          menu_principal = False
          history = True

        if menu.seleccion==3:
          print"salir"
          menu.seleccion=0
          fin=True

        menu.draw(pantalla)
        pygame.display.flip()
         

      #----------------------------------------------------------------------------

      if history:
        pantalla.blit(history_1,(0,0))
        pygame.display.flip() 
        #time.sleep(3)
        pantalla.blit(history_2,(0,0))
        pygame.display.flip() 
        #time.sleep(3)
        pantalla.blit(history_3,(0,0))
        pygame.display.flip() 
        #time.sleep(3)
        pantalla.blit(history_4,(0,0))
        pygame.display.flip() 
        #time.sleep(3)
        game_init = True
        history = False
             

      if game_init:

       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if keys_down[K_SPACE]:
              if jugador.direccion == 1:
                jugador.disparo_derecha(jugadordisparo_der,contador_disparo_derecha)
              else:
                jugador.disparo_izquierda(jugadordisparo_izq,contador_disparo_izquierda)
              Bala = Bullet(imagen_bala,jugador.direccion)
              #print Bala.direccion
              sound.play()
              Bala.rect.x = jugador.rect.x+35
              Bala.rect.y = jugador.rect.y+5
              ls_balas.add(Bala)
              #activos_sp_lista.add(Bala)
              #ls_todos.add(Bala)

        if keys_down[K_LEFT]:
          jugador.direccion = 0
          jugador.ir_izq(caminata_izq,contador_moverizquierda)

          if contador_moverizquierda < contador_moverizqtotal:
            contador_moverizquierda += 1
          else:
            contador_moverizquierda = 0

        if keys_down[K_RIGHT]:
          jugador.direccion = 1

          jugador.ir_der(caminata_der,contador_moverderecha)
                     
          if contador_moverderecha < contador_moverdertotal:
            contador_moverderecha += 1
          else:
            contador_moverderecha = 0

        if keys_down[K_UP]:

          if jugador.direccion == 0:
            jugador.salto(salto_izq)
          else:          
            jugador.salto(salto_der)


          if contador_salto < 5:
            contador_salto += 1
          else:
            contador_salto = 0


        if keys_down[K_DOWN]:
          if jugador.direccion == 0:
            jugador.agacharse(agachado_izq)
          else:          
            jugador.agacharse(agachado_der)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and jugador.vel_x < 0:
                jugador.no_mover(jugador_der,jugador_izq)
            if event.key == pygame.K_RIGHT and jugador.vel_x > 0:
                jugador.no_mover(jugador_der,jugador_izq)

        #PAUSE-------------------------------------------------------------

        if keys_down[K_p]:
          pausa = True

          while pausa:
            game_init = False

            pygame.mouse.set_visible(True)
            pantalla.blit(fondo_pause,(0,0))

            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                fin = True

              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                  menu_pause.abajo()
                if event.key == pygame.K_UP:
                  menu_pause.arriba()
                if event.key == pygame.K_RETURN:
                  menu_pause.seleccion=menu_pause.nop

            #reanudar
            if menu_pause.seleccion==1:
              print "reanudar"
              menu_pause.seleccion=0
              pausa = False
              game_init = True


            #salir
            if menu_pause.seleccion==3:
              print "salir"
              menu_pause.seleccion=0
              pausa = False
              game_init = False
              menu_principal = True

            menu_pause.draw(pantalla)
            pygame.display.flip()


        # Actualizamos al jugador.
        activos_sp_lista.update(salto_der,salto_izq)
    
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
           
        if nivel_actual_no == 1:
          nivel_actual.fondo = fondonivel2

        #Si llegamos al final del nivel
        pos_actual=jugador.rect.x + nivel_actual.mov_fondo
        if pos_actual < nivel_actual.limite:
           jugador.rect.x=120
           if nivel_actual_no < len(nivel_lista)-1:
              nivel_actual_no += 1
              nivel_actual = nivel_lista[nivel_actual_no]
              jugador.nivel=nivel_actual

        #para los impactos entre las balas y los enemigos
        #for b in ls_balas:
          #ls_impactos = pygame.sprite.spritecollide(b,nivel_actual.enemigos_lista,True)     
          #for impacto in ls_impactos:
            #ls_balas.remove(b)
            #ls_todos.remove(b)

        for e in nivel_actual.enemigos_lista:
          ls_impactos = pygame.sprite.spritecollide(e,ls_balas,True)
          for impacto in ls_impactos:
            if e.dureza < 1:
              nivel_actual.enemigos_lista.remove(e)
            else:
              e.dureza -= 1




        #impactos entre  jugador y las plataformas fatales
        for p in activos_sp_lista:
          ls_impactos = pygame.sprite.spritecollide(p,nivel_actual.fatalplat,False)     
          for impacto in ls_impactos:
            #ls_todos.remove(p)
            #activos_sp_lista.remove(p)
            jugador.vida -=1
            jugador.rect.x = nivel_actual.checkpoint[0]
            jugador.rect.y = nivel_actual.checkpoint[1]
            imagen_bala = imagen_bala_normal           
            explosion.play()
            Loser.play() 
            reloj.tick(0.5)
            jugador_der = jugador_der_n
            jugador_izq = jugador_izq_n
            jugadordisparo_der = jugador_disparo_dern
            jugadordisparo_izq = jugador_disparo_izqn
            salto_der = jugador_saltoder_n
            salto_izq = jugador_saltoizq_n
            caminata_der = caminata_der_n
            caminata_izq = caminata_izq_n
            agachado_der = agachado_dern
            agachado_izq = agachado_izqn
            contador_moverdertotal = cont_mover_dern
            contador_moverizqtotal = cont_mover_izqn


        #impactos entre el jugador y los enemigos 
        for p in activos_sp_lista:
          ls_impactos = pygame.sprite.spritecollide(p,nivel_actual.enemigos_lista,False)
          for impacto in ls_impactos:
            jugador.salud -= 10
            jugador.rect.x = nivel_actual.checkpoint[0]
            jugador.rect.y = nivel_actual.checkpoint[1]
            explosion.play()
            Loser.play()
            reloj.tick(0.5)


        # impactos entre el jugador y los check point
        for p in nivel_actual.checkpoin_lista:
          ls_impactos = pygame.sprite.spritecollide(p,activos_sp_lista,False)
          for impacto in ls_impactos:
            nivel_actual.checkpoin_lista.remove(p)
            nivel_actual.checkpoint[0] = p.rect.x
            nivel_actual.checkpoint[1] = p.rect.y


        # colisiones entre el jugador y los modificadores
        for p in nivel_actual.modificadores:
          ls_impactos = pygame.sprite.spritecollide(p,activos_sp_lista,False)     
          for impacto in ls_impactos:
            mod.play()
            nivel_actual.modificadores.remove(p)
            if p.tipo_plataforma == 1:
              imagen_bala = imagen_gun1
            if p.tipo_plataforma == 2:
              imagen_bala = imagen_gun2
            if p.tipo_plataforma == 3:
              imagen_bala = imagen_gun3
            if p.tipo_plataforma == 4:
              imagen_bala = imagen_gun4
            if p.tipo_plataforma == 5:
              imagen_bala = imagen_gun5

              jugador_der = jugador_der_t
              jugador_izq = jugador_izq_t
              jugadordisparo_der = jugador_disparo_dert
              jugadordisparo_izq = jugador_disparo_izqt
              salto_der = jugador_saltoder_t
              salto_izq = jugador_saltoizq_t
              caminata_der = caminata_der_t
              caminata_izq = caminata_izq_t
              agachado_der = agachado_dert
              agachado_izq = agachado_izqt
              contador_moverder = cont_mover_dert
              contador_moverizq = cont_mover_izqt

        #for e in nivel_actual.enemigos_lista:
         # if e.disp == 1:



        if jugador.salud <= 0:
          imagen_bala = imagen_bala_normal
          jugador.vida-=1
          jugador.salud = 60        
          explosion.play()      
          reloj.tick(1)

          jugador_der = jugador_der_n
          jugador_izq = jugador_izq_n
          jugadordisparo_der = jugador_disparo_dern
          jugadordisparo_izq = jugador_disparo_izqn
          salto_der = jugador_saltoder_n
          salto_izq = jugador_saltoizq_n
          caminata_der = caminata_der_n
          caminata_izq = caminata_izq_n
          agachado_der = agachado_dern
          agachado_izq = agachado_izqn
          contador_moverdertotal = cont_mover_dern
          contador_moverizqtotal = cont_mover_izqn

        if jugador.vida == 0 :          
          pantalla.blit(game_over,[0,0])
          pygame.display.flip()
          reloj.tick(0.2)
          explosion.play()
          Loser.play()
          game_init = False
          menu_principal = True

          
        nivel_actual.draw(pantalla)
        activos_sp_lista.draw(pantalla)
        #ls_todos.update()
        #ls_todos.draw(pantalla)
        ls_balas.update()
        ls_balas.draw(pantalla)


        #se actualiza el juego !!!! 
        #pantalla.blit(background_nivel1, [0,0])
        pantalla.blit(background_neblina, [0,0])    
        #pantalla.blit(lifemask,[0,HIGH-70])


        if jugador.vida == 1:
          pantalla.blit(vida1,(20,20))
        elif jugador.vida == 2:
          pantalla.blit(vida1,(20,20))
          pantalla.blit(vida2,(40,20))
        elif jugador.vida == 3:
          pantalla.blit(vida1,(20,20))
          pantalla.blit(vida2,(40,20))
          pantalla.blit(vida3,(60,20))

        if jugador.salud <= 60 and jugador.salud >= 50:
          pantalla.blit(barra_vida1,(700,20))
        elif jugador.salud <= 50 and jugador.salud >= 40:
          pantalla.blit(barra_vida2,(700,20))
        elif jugador.salud <= 40 and jugador.salud >= 30:
          pantalla.blit(barra_vida3,(700,20))
        elif jugador.salud <= 30 and jugador.salud >= 20:
          pantalla.blit(barra_vida4,(700,20))
        elif jugador.salud <= 20 and jugador.salud >= 10:
          pantalla.blit(barra_vida5,(700,20))
        elif jugador.salud <= 10 and jugador.salud >= 0:
          pantalla.blit(barra_vida6,(700,20))

        
        pygame.display.flip()
        reloj.tick(60)
       

   



import pygame
from Colors import *

import random

    
# Controlamos que tan rapido actualizamos pantalla
reloj = pygame.time.Clock()

  

class Jugador(pygame.sprite.Sprite):
    
    # Atributos
    # velocidad del jugador
    vel_x = 0
    vel_y = 0
    
    # Lista de elementos con los cuales chocar
    nivel = None
    
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()
        self.direccion = 1   #mira hacia adelante con 1, mira hacia atras con 0
    
    def update(self,bajando,bajando_izq):
        """ Mueve el jugador. """
        # Gravedad
        self.calc_grav(bajando,bajando_izq)
        
        # Mover izq/der
        self.rect.x += self.vel_x
        
        # Revisar si golpeamos con algo (bloques con colision)
        bloque_col_list = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in bloque_col_list:
            # Si nos movemos a la derecha,
            # ubicar jugador a la izquierda del objeto golpeado
            if self.vel_x > 0:
                self.rect.right = bloque.rect.left
            elif self.vel_x < 0:
                # De otra forma nos movemos a la izquierda
                self.rect.left = bloque.rect.right
        
        # Mover arriba/abajo
        self.rect.y += self.vel_y
        
        # Revisamos si chocamos
        bloque_col_list = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        for bloque in bloque_col_list:
            
            # Reiniciamos posicion basado en el arriba/bajo del objeto
            if self.vel_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.vel_y < 0:
                self.rect.top = bloque.rect.bottom
            
            # Detener movimiento vertical
            self.vel_y = 0

    def calc_grav(self,bajando,bajando_izq):
        """ Calculamos efecto de la gravedad. """
        if self.vel_y == 0:
            self.vel_y = 1
           #self.image=parado
        else:
            self.vel_y += .35
            if self.direccion == 0:
                self.image=bajando_izq
            else:
                self.image=bajando

        
        # Revisamos si estamos en el suelo
        if self.rect.y >= ALTO - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = ALTO - self.rect.height

    def salto(self,subiendo):
        """ saltamos al pulsar boton de salto """
        #print "en salto"
        # Nos movemos abajo un poco y revisamos si hay una plataforma bajo el jugador
        self.rect.y += 1
        plataforma_col_lista = pygame.sprite.spritecollide(self, self.nivel.plataforma_lista, False)
        self.rect.y -= 1
        
        # Si es posible saltar, aumentamos velocidad hacia arriba
        if len(plataforma_col_lista) > 0 or self.rect.bottom >= ALTO:
            self.vel_y = -10
            self.image=subiendo

    # Control del movimiento
    def ir_izq(self,secuenciaizquierda,cont):
        """ Usuario pulsa flecha izquierda """
        self.vel_x = -6
        self.image=secuenciaizquierda[cont][0]
       

    def ir_der(self,secuenciaderecha,cont):
        """ Usuario pulsa flecha derecha """
        self.vel_x = 6        
        self.image=secuenciaderecha[cont][0]

    def disparo_derecha(self,sec,cont):
        self.image=sec

    def disparo_izquierda(self,sec,cont):
        self.image=sec

    def agacharse(self,imagen):
        self.image = imagen

    def no_mover(self,imagen_der,imagen_izq):
        """ Usuario no pulsa teclas """
        self.vel_x = 0
        if self.direccion == 1:
            self.image= imagen_der
        else:
            self.image= imagen_izq
import pygame
import sys

AZUL = (0,0,255)


# ancho y alto de la pantalla
ANCHO=600
ALTO=400

CentroX = int(ANCHO/2)
CentroY = int(ALTO/2)

# crear pantalla
pygame.init()
pantalla = pygame.display.set_mode([ANCHO,ALTO])

#xc = 100
#yc = 100

r = 50

def transformada(punto):
  nx=CentroX+punto[0]
  ny=CentroY-punto[1]
  return (int(nx),int(ny))


def CircleMidPoint(r):
  x = 0
  y = r
  p = 1 - r

  pantalla.set_at([x,y], AZUL)

#PlotPoint(g,xc,yc,x,y)
 # se cicla hasta trazar todo un octante
  while (x < y):
    x = x + 1
    if p < 0:
      p = p + 2*x + 1
    else :
      y = y - 1
      p = p + 2*(x - y) + 1
    x1 = x
    y1 = y
  
    pantalla.set_at(transformada([x1,y1]), AZUL)
    pantalla.set_at(transformada([-x1,y1]), AZUL)
    pantalla.set_at(transformada([x1,-y1]), AZUL)
    pantalla.set_at(transformada([-x1,-y1]), AZUL)
    pantalla.set_at(transformada([y1,x1]), AZUL)
    pantalla.set_at(transformada([-y1,x1]), AZUL)
    pantalla.set_at(transformada([y1,-x1]), AZUL)
    pantalla.set_at(transformada([-y1,-x1]), AZUL)


    #PlotPoint(g,xc,yc,x,y);
CircleMidPoint(r)
#####################
pygame.display.flip()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)
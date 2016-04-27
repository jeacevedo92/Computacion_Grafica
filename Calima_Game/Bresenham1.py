
def Bresenham1(x0,y0,x1,y1):

	lista = []


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

	lista.append([x0,y0])
	#pantalla.set_at((int(x0),int(y0)), AZUL)

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

			#pantalla.set_at((int(x),int(y)), AZUL)
			lista.append([x,y])
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

			#pantalla.set_at((int(x),int(y)), AZUL)
			lista.append([x,y])
	#print lista
	return lista


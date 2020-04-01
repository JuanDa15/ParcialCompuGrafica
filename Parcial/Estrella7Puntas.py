import pygame
from Libreria import *

pygame.init()

ventana=pygame.display.set_mode([1080,720])
pygame.display.set_caption("Parcial Computacion Grafica")
Medio = [540,360]
MovimientoAngulo = 360/7
angulo = 0

i = 0
ListaPuntos = []


if __name__ == '__main__':
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        i = 0
        ListaPuntos = []
              
        while i < 7:
            PuntoCartesiano = PolaresACartesianas([300, angulo])
            PuntoPantalla = CartesianoAPantalla(Medio, PuntoCartesiano)
            ListaPuntos.append(PuntoPantalla)
            angulo += MovimientoAngulo
            i += 1
        
            
        pygame.draw.polygon(ventana, BLANCO, ListaPuntos, 2)
        
        ventana.fill([0,0,0])
        pygame.draw.line(ventana, BLANCO, ListaPuntos[0], ListaPuntos[4], 2)
        pygame.draw.line(ventana, BLANCO, ListaPuntos[4], ListaPuntos[1], 2)
        pygame.draw.line(ventana, BLANCO, ListaPuntos[1], ListaPuntos[5], 2)
        pygame.draw.line(ventana, BLANCO, ListaPuntos[5], ListaPuntos[2], 2)
        pygame.draw.line(ventana, BLANCO, ListaPuntos[2], ListaPuntos[6], 2)
        pygame.draw.line(ventana, BLANCO, ListaPuntos[6], ListaPuntos[3], 2)
        pygame.draw.line(ventana, BLANCO, ListaPuntos[3], ListaPuntos[0], 2) 
        angulo += 0.2


        pygame.display.flip()
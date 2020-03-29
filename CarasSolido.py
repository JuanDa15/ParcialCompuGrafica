import pygame

pygame.init()

ventana=pygame.display.set_mode([1080,720])
pygame.display.set_caption("Parcial Computacion Grafica")
Medio = [540,600]
BLANCO = [255,255,255]

Superior1 = [880,200]
Superior2 = [930,200]
Superior3 = [980,200]
Superior4 = [1030,200]

Superior5 = [880,150]
Superior6 = [930,150]
Superior7 = [980,150]
Superior8 = [1030,150]

Superior9 = [880,100]
Superior10 = [930,100]
Superior11 = [980,100]
Superior12 = [1030,100]

Superior13 = [880,50]
Superior14 = [930,50]
Superior15 = [980,50]
Superior16 = [1030,50]

PuntosSuperior = [Superior1, Superior2,Superior3, Superior4,Superior5, Superior6,Superior7, Superior8,Superior9,Superior10, Superior11,Superior12, Superior13,Superior14, Superior15,Superior16]

#VISTA SUPERIOR
#columna inferior izq
pygame.draw.polygon(ventana, BLANCO, [PuntosSuperior[0], PuntosSuperior[1],PuntosSuperior[5], PuntosSuperior[4]], 2)
#columna inferior der
pygame.draw.polygon(ventana, BLANCO, [PuntosSuperior[2], PuntosSuperior[3],PuntosSuperior[7], PuntosSuperior[6]], 2)
#columna superior izq
pygame.draw.polygon(ventana, BLANCO, [PuntosSuperior[8], PuntosSuperior[9],PuntosSuperior[13], PuntosSuperior[12]], 2)
#columna superior der
pygame.draw.polygon(ventana, BLANCO, [PuntosSuperior[10], PuntosSuperior[11],PuntosSuperior[15], PuntosSuperior[14]], 2)
#cruz central
pygame.draw.polygon(ventana, BLANCO, [PuntosSuperior[1], PuntosSuperior[2],PuntosSuperior[6], PuntosSuperior[7], PuntosSuperior[11],PuntosSuperior[10],PuntosSuperior[14], PuntosSuperior[13], PuntosSuperior[9],PuntosSuperior[8], PuntosSuperior[4], PuntosSuperior[5]], 2)


#VISTA LATERAL
Lateral1 = [880,400]
Lateral2 = [1030,400]

Lateral3 = [930,350]
Lateral4 = [980,350]

Lateral5 = [880,250]
Lateral6 = [930,250]
Lateral7 = [980,250]
Lateral8 = [1030,250]

PuntosLateral = [Lateral1, Lateral2,Lateral3, Lateral4, Lateral5, Lateral6, Lateral7, Lateral8]

pygame.draw.polygon(ventana, BLANCO, [PuntosLateral[0], PuntosLateral[1], PuntosLateral[7],PuntosLateral[6], PuntosLateral[3], PuntosLateral[2],PuntosLateral[5], PuntosLateral[4]],2)


#VISTA INFERIOR
Inferior1 = [880,600]
Inferior2 = [1030,600]

Inferior3 = [880,450]
Inferior4 = [1030,450]

PuntosInferior = [Inferior1, Inferior2, Inferior3, Inferior4]

pygame.draw.polygon(ventana, BLANCO, [PuntosInferior[0], PuntosInferior[1], PuntosInferior[3], PuntosInferior[2]],2)


#TEXTO EN PANTALLA

fuente = pygame.font.Font(None, 25)
TextoSuperior = "Vista Superior"
TextoLateral = "Vista Lateral"
TextoInferior = "Vista Inferior"

TextoPantallaSuperior = fuente.render(TextoSuperior, 1, (255, 255, 255))
TextoPantallaLateral = fuente.render(TextoLateral, 1, (255, 255, 255))
TextoPantallaInferior = fuente.render(TextoInferior, 1, (255, 255, 255))
ventana.blit(TextoPantallaSuperior, (880, 30))
ventana.blit(TextoPantallaLateral, (880, 230))
ventana.blit(TextoPantallaInferior, (880, 430))

if __name__ == '__main__':
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        
        pygame.display.flip()
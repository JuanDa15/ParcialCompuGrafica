import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1280
high =920
window = pygame.display.set_mode([width,high])
pygame.display.set_caption("Parcial Computacion Grafica")
middle = [width/2,600]
end = False
porcentaje = 1
angulo = 1

#PRIMERA CARA
aux1 = PolarToCartesian(100,30)
aux2 = PolarToCartesian(50,30)
a1 = [0,0]
a2 = PolarToCartesian(150,30)
a3 = Traslacion(a2,0,150)
a4 = Traslacion(aux1,0,150)
a5 = Traslacion(aux1,0,50)
a6 = Traslacion(aux2,0,50)
a7 = Traslacion(aux2,0,150)
a8 = Traslacion(a1,0,150)
a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a1s,a4)
a5s = CartToScreen(a1s,a5)
a6s = CartToScreen(a1s,a6)
a7s = CartToScreen(a1s,a7)
a8s = CartToScreen(a1s,a8)
PrimerCara = [a1s,a2s,a3s,a4s,a5s,a6s,a7s,a8s]
##SEGUNDA CARA
baux1 = PolarToCartesian(100,150)
baux2 = PolarToCartesian(50,150)
b1 = PolarToCartesian(150,150)
b2 = Traslacion(b1,0,150)
b3 = Traslacion(baux1,0,150)
b4 = Traslacion(baux1,0,50)
b5 = Traslacion(baux2,0,50)
b6 = Traslacion(baux2,0,150)
b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)
b3s = CartToScreen(a1s,b3)
b4s = CartToScreen(a1s,b4)
b5s = CartToScreen(a1s,b5)
b6s = CartToScreen(a1s,b6)
SegundaCara = [a1s,b1s,b2s,b3s,b4s,b5s,b6s,a8s]
#TERCER POLIGONO
c1 = Traslacion(aux1,0,200)
c2 = Traslacion(aux2,0,200)
c1s = CartToScreen(a1s,c1)
c2s = CartToScreen(a1s,c2)
TercerCara = [a3s,c1s,c2s,a4s]
#CUARTO POLIGONO
d1 = Traslacion(aux2,0,100)
d1s = CartToScreen(a1s,d1)
CuartaCara = [a4s,a5s,d1s,c2s]
#quinta cara
QuintaCara = [a5s,d1s,a6s]
#sexta cara
e1 = Traslacion(a1,0,200)
e1s = CartToScreen(a1s,e1)
SextaCara = [a7s,a8s,b6s,e1s]
#septima cara
f1 = Traslacion(baux1,0,200)
f2 = Traslacion(baux2,0,200)
f1s = CartToScreen(a1s,f1)
f2s = CartToScreen(a1s,f2)
SeptimaCara = [b2s,f1s,f2s,b3s]
#octava cara
g1 = Traslacion(baux2,0,100)
g1s = CartToScreen(a1s,g1)
OctavaCara = [b3s,b4s,g1s,f2s]
#NOVENA CARA
NovenaCara = [b4s,b5s,g1s]
#decima cara
h1 = Traslacion(baux2,0,250)
h2 = Traslacion(a1,0,300)
h3 = Traslacion(aux2,0,250)
h4 = Traslacion(a1,0,250)
h1s = CartToScreen(a1s,h1)
h2s = CartToScreen(a1s,h2)
h3s = CartToScreen(a1s,h3)
h4s = CartToScreen(a1s,h4)
DecimaCara = [h1s,h2s,h3s,h4s]
#onceaba cara
OnceavaCara = [h1s,h4s,e1s,b6s]
#doceaba cara
DoceavaCara = [e1s,h4s,h3s,a7s]

#posiciones isometrico cartesianas
PrimerCaraCart = [a1,a2,a3,a4,a5,a6,a7,a8]
SegundaCaraCart = [a1,b1,b2,b3,b4,b5,b6,a8]
TercerCaraCart = [a3,c1,c2,a4]
CuartaCaraCart = [a4,a5,d1,c2]
QuintaCaraCart = [a5,d1,a6]
SextaCaraCart = [a7,a8,b6,e1]
SeptimaCaraCart = [b2,f1,f2,b3]
OctavaCaraCart = [b3,b4,g1,f2]
NovenaCaraCart = [b4,b5,g1]
DecimaCaraCart = [h1,h2,h3,h4]
OnceavaCaraCart = [h1,h4,e1,b6]
DoceavaCaraCart = [e1,h4,h3,a7]
#---------------------------------------------------------------------------------------
def escalarLista(List,porcentaje):
    posEscaladaScreen = []
    for pos in List:
        posEscalada = escalar(pos,porcentaje)
        posEscaladaScreen.append(CartToScreen(middle,posEscalada))
    return posEscaladaScreen

def DrawSolido(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12):
    drawPolygonSolid(window,SelectColor('Gray1'),x1)
    drawPolygonSolid(window,SelectColor('Gray2'),x2)
    drawPolygonSolid(window,SelectColor('White'),x3)
    drawPolygonSolid(window,SelectColor('Gray2'),x4)
    drawPolygonSolid(window,SelectColor('White'),x5)
    drawPolygonSolid(window,SelectColor('White'),x6)
    drawPolygonSolid(window,SelectColor('White'),x7)
    drawPolygonSolid(window,SelectColor('Gray1'),x8)
    drawPolygonSolid(window,SelectColor('White'),x9)
    drawPolygonSolid(window,SelectColor('White'),x10)
    drawPolygonSolid(window,SelectColor('Gray2'),x11)
    drawPolygonSolid(window,SelectColor('Gray1'),x12)

def vistas():
     #---------------------------------------------------------------------------------------
    BLANCO = [255,255,255]

    Superior1 = [980,200]
    Superior2 = [1030,200]
    Superior3 = [1080,200]
    Superior4 = [1130,200]

    Superior5 = [980,150]
    Superior6 = [1030,150]
    Superior7 = [1080,150]
    Superior8 = [1130,150]

    Superior9 = [980,100]
    Superior10 = [1030,100]
    Superior11 = [1080,100]
    Superior12 = [1130,100]

    Superior13 = [980,50]
    Superior14 = [1030,50]
    Superior15 = [1080,50]
    Superior16 = [1130,50]

    PuntosSuperior = [Superior1, Superior2,Superior3, Superior4,Superior5, Superior6,Superior7, Superior8,Superior9,Superior10, Superior11,Superior12, Superior13,Superior14, Superior15,Superior16]

    #VISTA SUPERIOR
    #columna inferior izq
    pygame.draw.polygon(window, BLANCO, [PuntosSuperior[0], PuntosSuperior[1],PuntosSuperior[5], PuntosSuperior[4]], 2)
    #columna inferior der
    pygame.draw.polygon(window, BLANCO, [PuntosSuperior[2], PuntosSuperior[3],PuntosSuperior[7], PuntosSuperior[6]], 2)
    #columna superior izq
    pygame.draw.polygon(window, BLANCO, [PuntosSuperior[8], PuntosSuperior[9],PuntosSuperior[13], PuntosSuperior[12]], 2)
    #columna superior der
    pygame.draw.polygon(window, BLANCO, [PuntosSuperior[10], PuntosSuperior[11],PuntosSuperior[15], PuntosSuperior[14]], 2)
    #cruz central
    pygame.draw.polygon(window, BLANCO, [PuntosSuperior[1], PuntosSuperior[2],PuntosSuperior[6], PuntosSuperior[7], PuntosSuperior[11],PuntosSuperior[10],PuntosSuperior[14], PuntosSuperior[13], PuntosSuperior[9],PuntosSuperior[8], PuntosSuperior[4], PuntosSuperior[5]], 2)


    #VISTA LATERAL
    Lateral1 = [980,400]
    Lateral2 = [1130,400]

    Lateral3 = [1030,350]
    Lateral4 = [1080,350]

    Lateral5 = [980,250]
    Lateral6 = [1030,250]
    Lateral7 = [1080,250]
    Lateral8 = [1130,250]

    PuntosLateral = [Lateral1, Lateral2,Lateral3, Lateral4, Lateral5, Lateral6, Lateral7, Lateral8]

    pygame.draw.polygon(window, BLANCO, [PuntosLateral[0], PuntosLateral[1], PuntosLateral[7],PuntosLateral[6], PuntosLateral[3], PuntosLateral[2],PuntosLateral[5], PuntosLateral[4]],2)


    #VISTA INFERIOR
    Inferior1 = [980,600]
    Inferior2 = [1130,600]

    Inferior3 = [980,450]
    Inferior4 = [1130,450]

    PuntosInferior = [Inferior1, Inferior2, Inferior3, Inferior4]

    pygame.draw.polygon(window, BLANCO, [PuntosInferior[0], PuntosInferior[1], PuntosInferior[3], PuntosInferior[2]],2)


    #TEXTO EN PANTALLA

    fuente = pygame.font.Font(None, 25)
    TextoSuperior = "Vista Superior"
    TextoLateral = "Vista Lateral"
    TextoInferior = "Vista Inferior"

    TextoPantallaSuperior = fuente.render(TextoSuperior, 1, (255, 255, 255))
    TextoPantallaLateral = fuente.render(TextoLateral, 1, (255, 255, 255))
    TextoPantallaInferior = fuente.render(TextoInferior, 1, (255, 255, 255))
    window.blit(TextoPantallaSuperior, (980, 30))
    window.blit(TextoPantallaLateral, (980, 230))
    window.blit(TextoPantallaInferior, (980, 430))
    #--------------------------------------------------------------------------------------
    pygame.display.flip()
    
def rotarLista(List,Angle):
    ListaRotadaScreen = []
    for pos in List:
        posrotada = RotacionHoraria(pos,angulo)
        ListaRotadaScreen.append(CartToScreen(middle,posrotada))
    return ListaRotadaScreen

def Rotar(angulo):
    PrimerCaraRotada = rotarLista(PrimerCaraCart,angulo)
    SegundaCaraRotada = rotarLista(SegundaCaraCart,angulo)
    TercerCaraRotada = rotarLista(TercerCaraCart,angulo)
    CuartaCaraRotada = rotarLista(CuartaCaraCart,angulo)
    QuintaCaraRotada = rotarLista(QuintaCaraCart,angulo)
    SextaCaraRotada = rotarLista(SextaCaraCart,angulo)
    SeptimaCaraRotada = rotarLista(SeptimaCaraCart,angulo)
    OctavaCaraRotada = rotarLista(OctavaCaraCart,angulo)
    NovenaCaraRotada = rotarLista(NovenaCaraCart,angulo)
    DecimaCaraRotada = rotarLista(DecimaCaraCart,angulo)
    OnceavaCaraRotada = rotarLista(OnceavaCaraCart,angulo)
    DoceavaCaraRotada = rotarLista(DoceavaCaraCart,angulo)
    window.fill([0,0,0])
    DrawSolido(PrimerCaraRotada,SegundaCaraRotada,TercerCaraRotada,CuartaCaraRotada,QuintaCaraRotada,SextaCaraRotada,SeptimaCaraRotada,OctavaCaraRotada,NovenaCaraRotada,DecimaCaraRotada,OnceavaCaraRotada,DoceavaCaraRotada)

def escalarIso(porcentaje):
    PrimerCaraEscalada = escalarLista(PrimerCaraCart,porcentaje)
    SegundaCaraEscalada = escalarLista(SegundaCaraCart,porcentaje)
    TercerCaraEscalada = escalarLista(TercerCaraCart,porcentaje)
    CuartaCaraEscalada = escalarLista(CuartaCaraCart,porcentaje)
    QuintaCaraEscalada = escalarLista(QuintaCaraCart,porcentaje)
    SextaCaraEscalada = escalarLista(SextaCaraCart,porcentaje)
    SeptimaCaraEscalada = escalarLista(SeptimaCaraCart,porcentaje)
    OctavaCaraEscalada = escalarLista(OctavaCaraCart,porcentaje)
    NovenaCaraEscalada = escalarLista(NovenaCaraCart,porcentaje)
    DecimaCaraEscalada = escalarLista(DecimaCaraCart,porcentaje)
    OnceavaCaraEscalada = escalarLista(OnceavaCaraCart,porcentaje)
    DoceavaCaraEscalada = escalarLista(DoceavaCaraCart,porcentaje)  
    window.fill([0,0,0])
    DrawSolido(PrimerCaraEscalada,SegundaCaraEscalada,TercerCaraEscalada,CuartaCaraEscalada,QuintaCaraEscalada,SextaCaraEscalada,SeptimaCaraEscalada,OctavaCaraEscalada,NovenaCaraEscalada,DecimaCaraEscalada,OnceavaCaraEscalada,DoceavaCaraEscalada)

if __name__ == "__main__":
    drawPlane(window,middle)
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window.fill([0,0,0])
                    DrawSolido(PrimerCara,SegundaCara,TercerCara,CuartaCara,QuintaCara,SextaCara,SeptimaCara,OctavaCara,NovenaCara,DecimaCara,OnceavaCara,DoceavaCara)
                if event.button == 4:
                    escalarIso(porcentaje)
                    porcentaje = porcentaje + 0.01
                if event.button == 5:
                    escalarIso(porcentaje)
                    porcentaje = porcentaje - 0.01
                    if porcentaje < 0:
                        porcentaje = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Rotar(angulo)
                    angulo+=1
                    if angulo >= 360:
                        angulo = 0
                if event.key == pygame.K_LEFT:
                    Rotar(angulo)
                    angulo-=1
                    if angulo <= 0:
                        angulo = 360
        vistas()
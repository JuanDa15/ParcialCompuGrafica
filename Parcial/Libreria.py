import pygame
import math

#Settings Windows and Colors
ANCHO = 1080
ALTO = 720
NEGRO = [0,0,0]
BLANCO = [225,225,225]
RED = [225,0,0]
GREEN = [0,225,0]
BLUE = [0,0,225]

Medio = []



#DIbujar Punto
def DibujarPunto (ventana,Punto, Color):
    pygame.draw.circle(ventana,Color,Punto, 2)
    pygame.display.flip()


#Dibujar plano coordenado en el punto del mouse.
def plano(ventana, p):
    posy=p[1]
    posx=p[0]

    ventana.fill([0,0,0])
    pygame.draw.line(ventana,[225, 0 ,0],[0,posy],[ANCHO,posy], 2)
    pygame.draw.line(ventana,[225, 0 ,0],[posx,0],[posx,ALTO], 2)


#--------------------------------------------------------------------------------------------------
#Une los puntos de 2 triangulos dibujados
def unirpuntos(ventana, Positions, lista):
    pygame.draw.line(ventana, BLANCO, lista, Positions, 2)
    pygame.draw.line(ventana, BLANCO, [(lista[0] + 100), (lista[1] + 100)], [(Positions[0]+ 100), (Positions[1] + 100)], 2)
    pygame.draw.line(ventana, BLANCO,  [(lista[0]- 100), (lista[1] + 100)], [(Positions[0]- 100), (Positions[1] + 100)], 2)


#--------------------------------------------------------------------------------------------------
#Dibuja un triangulo dado los puntos
def DibujarTrianguloVentana(ventana, Positions):
    pygame.draw.line(ventana, BLANCO, Positions[0], Positions[1], 2)
    pygame.draw.line(ventana, BLANCO, Positions[1], Positions[2], 2)
    pygame.draw.line(ventana, BLANCO, Positions[2], Positions[0], 2)

def DibujarTrianguloPlano(ventana, Positions):
    pygame.draw.line(ventana, BLANCO, Positions[0], Positions[1], 2)
    pygame.draw.line(ventana, BLANCO, Positions[1], Positions[2], 2)
    pygame.draw.line(ventana, BLANCO, Positions[2], Positions[0], 2)


#--------------------------------------------------------------------------------------------------
#Dibuja triangulo predefinido.
def Triangulo(ventana, Positions):
    pygame.draw.line(ventana, BLANCO, Positions, [(Positions[0]+ 100), (Positions[1] + 100)], 2)
    pygame.draw.line(ventana, BLANCO, [(Positions[0] + 100), (Positions[1] + 100)], [(Positions[0]- 100), (Positions[1] + 100)], 2)
    pygame.draw.line(ventana, BLANCO,  [(Positions[0]- 100), (Positions[1] + 100)], Positions, 2)


#--------------------------------------------------------------------------------------------------
#Dibujar patron en pantalla
def dibujarpatron(ventana, posx, ANCHO):
    pygame.draw.line(ventana, BLANCO, [posx + 5, (ALTO - 20)], [posx +20, (ALTO - 20)], 1)
    pygame.draw.line(ventana, BLANCO, [posx +20, (ALTO - 20)], [posx +20, (ALTO - 5)], 1)
    pygame.draw.line(ventana, BLANCO, [posx +20, (ALTO - 5)], [posx +5, (ALTO - 5)], 1)
    pygame.draw.line(ventana, BLANCO, [posx +5, (ALTO - 5)], [posx +5, (ALTO - 15)], 1)
    pygame.draw.line(ventana, BLANCO, [posx +5, (ALTO - 15)], [posx +15, (ALTO - 15)], 1)
    pygame.draw.line(ventana, BLANCO,  [posx +15, (ALTO - 15)], [posx +15, (ALTO - 10)], 1)
    pygame.draw.line(ventana, BLANCO,  [posx +15, (ALTO - 10)], [posx +10, (ALTO - 10)], 1)

#--------------------------------------------------------------------------------------------------
#Borde del triangulo relleno
def TrianguloRelleno(ventana, ANCHO, ALTO):
    pygame.draw.line(ventana, BLANCO, [(ANCHO / 2), 50],[(ANCHO - 50), (ALTO - 50)], 2)
    pygame.draw.line(ventana, BLANCO, [(ANCHO - 50), (ALTO - 50)],[50, (ALTO - 50)], 2)
    pygame.draw.line(ventana, BLANCO, [50, ALTO - 50],[(ANCHO / 2), 50], 2)

#lineas interiores del triangulo relleno
def RellenarTriangulo(ventana, Positions, ANCHO, ALTO):
    indiceSumador = ((ANCHO - 100) / 20)
    i = 50 + indiceSumador
    Contador = 1
    while (Contador < 20):
        pygame.draw.line(ventana, GREEN, [Positions[0][0], Positions[0][1]],[i, (ALTO - 50)], 2)
        i = i + indiceSumador
        Contador = Contador + 1

    Contador = 1

    indiceSumadorX = float(((float(ANCHO) - 100) / 20) / 2)
    indiceSumadorY = ((float(ALTO) - 100) / 20)

    indicex = 50 + indiceSumadorX
    indicey = ALTO - 50 - indiceSumadorY
    while (Contador < 20):
        pygame.draw.line(ventana, RED, [Positions[1][0], Positions[1][1]],[indicex, indicey], 2)
        indicex = indicex + indiceSumadorX
        indicey = indicey - indiceSumadorY
        Contador = Contador + 1

    indicex = ANCHO - 50 - indiceSumadorX
    indicey = ALTO - 50 - indiceSumadorY
    Contador = 1
    while (Contador < 20):
        pygame.draw.line(ventana, BLUE, [Positions[2][0], Positions[2][1]],[indicex, indicey], 2)
        indicex = indicex - indiceSumadorX
        indicey = indicey - indiceSumadorY
        Contador = Contador + 1

#define los puntos del triangulo relleno
def IngresarPuntos(ventana, ANCHO, ALTO, Positions):
    Positions.append([(ANCHO / 2), 50])
    Positions.append([(ANCHO - 50), (ALTO - 50)])
    Positions.append([50, (ALTO - 50)])


#--------------------------------------------------------------------------------------------------

def ActualizarMedio(medio, Centro):
    medio[0] = Centro[0]
    medio[1] = Centro[1]




def MoverHaciaIzquierda(Positionswindow, PositionsCartesian):
    for i in range (len(Positionswindow)):
        Positionswindow[i][0] = Positionswindow[i][0] - 4
        PositionsCartesian[i][0] = PositionsCartesian[i][0] - 4

def MoverHaciaDerecha(Positionswindow, PositionsCartesian):
    for i in range (len(Positionswindow)):
        Positionswindow[i][0] = Positionswindow[i][0] + 4
        PositionsCartesian[i][0] = PositionsCartesian[i][0] + 4

def MoverHaciaArriba(Positionswindow, PositionsCartesian):
    for i in range (len(Positionswindow)):
        Positionswindow[i][1] = Positionswindow[i][1] - 4
        PositionsCartesian[i][1] = PositionsCartesian[i][1] + 4

def MoverHaciaAbajo(Positionswindow, PositionsCartesian):
    for i in range (len(Positionswindow)):
        Positionswindow[i][1] = Positionswindow[i][1] + 4
        PositionsCartesian[i][1] = PositionsCartesian[i][1] - 4






#Transformaciones

#translacion en el plano cartesiano
def CartesianoAPantalla(Centro,Punto): #pasa de coordenadas cartesianas a pantalla
    PuntoX = Centro[0] + Punto[0]
    PuntoY = Centro[1] - Punto[1]
    PuntoFinal = [PuntoX,PuntoY]
    return PuntoFinal


def ListaAPantalla(Medio, Puntos, PuntosEscalados):
    for i in range (len(PuntosEscalados)):
        Puntos[i] = CartesianoAPantalla(Medio, PuntosEscalados[i])



def PantallaACartesiano(Medio, Punto):
    C = 0
    if Punto[0] >= Medio[0] and Punto[1] <= Medio[1]:
        C = 1
    if Punto[0] < Medio[0] and Punto[1] <= Medio[1]:
        C = 2
    if Punto[0] < Medio[0] and Punto[1] > Medio[1]:
        C = 3
    if Punto[0] >= Medio[0] and Punto[1] > Medio[1]:
        C = 4

    if C == 1:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 2:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 3:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 4:
        PuntoX = Punto[0] - Medio[0]
        PuntoY = Medio[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal



def ListaACartesiano (Medio, Puntos, PuntosEscalados):
    for i in range (len(Puntos)):
        PuntosEscalados[i] = PantallaACartesiano(Medio, Puntos[i])

#-------------------------------------------------------------------------------
#Vectores

def DibujarVectores(ventana,medio, Vector):
    pygame.draw.line(ventana,BLANCO,medio,Vector, 2)

def SumarVectores(Vector1, Vector2):
    VecX = Vector1[0] + Vector2[0]
    VecY = Vector1[1] + Vector2[1]
    vectorFinal = [VecX, VecY]
    return vectorFinal

#-------------------------------------------------------------------------------
#Linea Recta

def DibujarRecta(ventana, Medio,  LimiteSuperiorX, LimiteInferiorX, Pendiente, Sumando):
    variableX = 0
    variableY = 0
    i = LimiteInferiorX
    while (i <= LimiteSuperiorX):

        variableX = i
        variableY = (Pendiente * variableX) + Sumando
        variableX = Medio[0] + i
        variableY = Medio[1] - variableY

        pygame.draw.circle(ventana, BLANCO, [int(variableX), int(variableY)], 2)
        i =i + 1
        pygame.display.flip()


def Pendiente(Punto1, Punto2):
    Pendientey = float(Punto2[1] - Punto1[1])
    Pendientex = float(Punto2[0] - Punto1[0])
    Pendiente = float(Pendientey / Pendientex)
    return Pendiente

def Desfase(Punto, pendiente):
    Corte = float(Punto[1] - (pendiente * Punto[0]))
    return Corte



#-------------------------------------------------------------------------------
#Escalamiento

def escalar(Escalado, Puntos, PuntosEscalados):
    for i in range (len(Puntos)):
        PuntoEscaladoX = Puntos[i][0] * Escalado
        PuntoEscaladoY = Puntos[i][1] * Escalado
        PuntosEscalados[i] = [PuntoEscaladoX, PuntoEscaladoY]

def escalarLista(Escalado, Puntos):
    for i in range (len(Puntos)):
        PuntoEscaladoX = Puntos[i][0] * Escalado
        PuntoEscaladoY = Puntos[i][1] * Escalado
        Puntos[i] = ([PuntoEscaladoX, PuntoEscaladoY])


#-------------------------------------------------------------------------------
#Rotacion

def RotarLista(Puntos, Angulo):
    ListaRotada = Puntos
    for i in (ListaRotada):
        x = i[0]
        y = i[1]
        i[0] = (x * math.cos(math.radians(Angulo))) + (y * math.sin(math.radians(Angulo)))
        i[1] = ((-x) * math.sin(math.radians(Angulo))) + (y * math.cos(math.radians(Angulo)))
    return ListaRotada


def RotarListaPuntoFijo(Puntos, Angulo):
    ListaRotada = Puntos
    for i in range(1,len(ListaRotada)):
        x = ListaRotada[i][0]
        y = ListaRotada[i][1]
        ListaRotada[i][0] = (x * math.cos(math.radians(Angulo))) + (y * math.sin(math.radians(Angulo)))
        ListaRotada[i][1] = ((-x) * math.sin(math.radians(Angulo))) + (y * math.cos(math.radians(Angulo)))
    return ListaRotada


def RotarPunto(Punto, Angulo):
    x = Punto[0]
    y = Punto[1]
    CoorX = (x * math.cos(math.radians(Angulo))) + (y * math.sin(math.radians(Angulo)))
    CoorY = (-x * math.sin(math.radians(Angulo))) + (y * math.cos(math.radians(Angulo)))
    return [int(CoorX), int(CoorY)]


#-------------------------------------------------------------------------------
#Traslacion

def Traslacion(Punto, Mover):
    X = Punto[0] + Mover[0]
    Y = Punto[1] + Mover[1]
    return [X,Y]


#-------------------------------------------------------------------------------
#polares

def RadioCaracolesPolares(polar, a, b):
    r = a + b * math.cos(math.radians(polar[0]))
    return r


def PolaresACartesianas(polar):
    x = polar[0] * math.cos(math.radians(polar[1]))
    y = polar[0] * math.sin(math.radians(polar[1]))
    pp = [int(x),int(y)]
    return pp


def RadioRosaPolar(polar, n, a):
    r = a* math.cos(n * (math.radians(polar[0])))
    return r

def RadioCirculosPolares(polar):
    A = polar[1] * 2
    r = A * math.cos(math.radians(polar[0]))
    return r

def RadioLemniscatasPolares(polar):
    r = (math.pow(polar[1] , 2)) * math.sin(2 * (math.radians(polar[0])))
    try:
        r = math.sqrt(r)
    except:
        print("")
    return r

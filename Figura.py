import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1280
high =920
window = pygame.display.set_mode([width,high])
middle = [width/2,600]
end = False

#PRIMERA CARA
a1 = [0,0]
a2 = PolarToCartesian(300,30)
a3 = Traslacion(a2,0,300)
a4 = PolarToCartesian(100,210)
a5 = Traslacion(a4,0,-200)
a6 = PolarToCartesian(100,210)
a7 = Traslacion(a6,0,200)
a8 = PolarToCartesian(100,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)
a5s = CartToScreen(a3s,a5)
a6s = CartToScreen(a5s,a6)
a7s = CartToScreen(a5s,a7)
a8s = CartToScreen(a7s,a8)

PrimerCara = [a1s,a2s,a3s,a4s,a5s,a6s,a7s,a8s]

##SEGUNDA CARA
b1 = PolarToCartesian(300,150)
b2 = Traslacion(b1,0,300)
b3 = PolarToCartesian(100,330)
b4 = Traslacion(b3,0,-200)
b5 = PolarToCartesian(100,330)
b6 = Traslacion(b5,0,200)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)
b3s = CartToScreen(b2s,b3)
b4s = CartToScreen(b2s,b4)
b5s = CartToScreen(b4s,b5)
b6s = CartToScreen(b4s,b6)

SegundaCara = [a1s,b1s,b2s,b3s,b4s,b5s,b6s,a8s]

#TERCER POLIGONO
c1 = PolarToCartesian(100,150)
c2 = PolarToCartesian(100,30)

c1s = CartToScreen(a4s,c1)
c2s = CartToScreen(c1s,c2)

TercerCara = [a4s,c1s,c2s,a3s]

#CUARTO POLIGONO
d1 = PolarToCartesian(100,150)

d1s = CartToScreen(a5s,d1)

CuartaCara = [a4s,a5s,d1s,c1s]

#quinta cara
QuintaCara = [a5s,d1s,a6s]

#sexta cara
e1 = PolarToCartesian(100,150)

e1s = CartToScreen(a7s,e1)

SextaCara = [a7s,a8s,b6s,e1s]

#septima cara
f1 =PolarToCartesian(100,30)
f2 = PolarToCartesian(100,330)

f1s = CartToScreen(b2s,f1)
f2s = CartToScreen(f1s,f2)

SeptimaCara = [b2s,f1s,f2s,b3s]

#octava cara

g1 = PolarToCartesian(100,30)

g1s = CartToScreen(b4s,g1)


OctavaCara = [b3s,b4s,g1s,f2s]

#NOVENA CARA
NovenaCara = [b4s,b5s,g1s]

#decima cara
h1 = PolarToCartesian(200,30)
h2 = PolarToCartesian(300,30)
h3 = PolarToCartesian(100,330)
h4 = PolarToCartesian(100,210)

h1s = CartToScreen(b2s,h1)
h2s = CartToScreen(b2s,h2)
h3s = CartToScreen(h2s,h3)
h4s = CartToScreen(h3s,h4)

DecimaCara = [h1s,h2s,h3s,h4s]

#onceaba cara

OnceavaCara = [h1s,h4s,e1s,b6s]

#doceaba cara

DoceavaCara = [e1s,h4s,h3s,a7s]

def DrawSolido():
    drawPolygonSolid(window,SelectColor('Gray1'),PrimerCara)
    drawPolygonSolid(window,SelectColor('Gray2'),SegundaCara)
    drawPolygonSolid(window,SelectColor('White'),TercerCara)
    drawPolygonSolid(window,SelectColor('Gray2'),CuartaCara)
    drawPolygonSolid(window,SelectColor('White'),QuintaCara)
    drawPolygonSolid(window,SelectColor('White'),SextaCara)
    drawPolygonSolid(window,SelectColor('White'),SeptimaCara)
    drawPolygonSolid(window,SelectColor('Gray1'),OctavaCara)
    drawPolygonSolid(window,SelectColor('White'),NovenaCara)
    drawPolygonSolid(window,SelectColor('White'),DecimaCara)
    drawPolygonSolid(window,SelectColor('Gray2'),OnceavaCara)
    drawPolygonSolid(window,SelectColor('Gray1'),DoceavaCara)
    
if __name__ == "__main__":
    drawPlane(window,middle)
    DrawSolido()
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
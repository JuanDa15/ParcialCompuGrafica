import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1080
high =720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
radius = 300
angle = 0
end = False
Positionspolygon = []
FinalLinePosition = []

def drawStar():
    createLine(window,Positionspolygon[0], Positionspolygon[2],SelectColor('Gray1'))
    createLine(window,Positionspolygon[0], Positionspolygon[5],SelectColor('Gray1'))
    
if __name__ == "__main__":
    drawPlane(window,middle)
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawStar()
        Createcircle(window,middle,SelectColor('White'),radius)
        AngleMovement = 360/7
        CartesianPos = PolarToCartesian(radius,angle)
        ScreenPos = CartToScreen(middle,CartesianPos)
        Positionspolygon.append(ScreenPos)
        if len(Positionspolygon) == 7:
            drawPolygon(window,SelectColor('Yellow'),Positionspolygon)
        angle += AngleMovement
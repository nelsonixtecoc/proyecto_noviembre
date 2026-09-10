import pygame 
import constantes
from personaje import Personaje

jugador = Personaje (x=50, y=50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("Zebe Pluss")


run = True
while run:
    
    jugador.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.update()

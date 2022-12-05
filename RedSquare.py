import pygame
import sys

pygame.init()

# Definir colores

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Crear ventana para el juego
size = (800, 500)
screen = pygame.display.set_mode(size)

# Controlar FPS
clock = pygame.time.Clock()

# Coordenadas
coord_x = 400
coord_y = 200

# Velocidad
speed_x = 8
speed_y = 8

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Animación
    if (coord_x > 720 or coord_x < 0):
        speed_x *= -1

    coord_x += speed_x

    if (coord_y > 420 or coord_y < 0):
        speed_y *= -1

    coord_y += speed_y

    # Color fondo
    screen.fill(WHITE)

    # Dibujar
    # pygame.draw.line(screen, GREEN, [0, 120], [100, 520], 5)
    # pygame.draw.rect(screen, BLACK, (400, 120, 90, 80))

    # for x in range(1, 700, 100):
        # pygame.draw.line(screen, GREEN, (x, 0), (x, 100), 5)
        # pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))

    coord_x += speed_x
    pygame.draw.rect(screen, RED, (coord_x, coord_y, 80, 80))

    # Actualiza pantalla
    pygame.display.flip()
    clock.tick(60)


import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Coordenadas cuadrado
coord_x = 10
coord_y = 10

# Velocidad
speed_x = 0
speed_y = 0

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Eventos teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
            if event.key == pygame.K_DOWN:
                speed_y = 3
            if event.key == pygame.K_UP:
                speed_y = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0
            if event.key == pygame.K_UP:
                speed_y = 0

    screen.fill(WHITE)

    coord_x += speed_x
    coord_y += speed_y

    pygame.draw.rect(screen, RED, (coord_x, coord_y, 100, 100))

    pygame.display.flip()
    clock.tick(60)
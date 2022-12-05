import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

player_width = 15
player_height = 90

game_over = False

# Coordenadas y velocidad del jugador 1
player1_coord_x = 50
player1_coord_y = 300 - 45
player1_speed_y = 0

# Coordenadas y velocidad del jugador 2
player2_coord_x = 750 - player_width
player2_coord_y = 300 - 45
player2_speed_y = 0

# Coordenadas  y velocidad pelota
pelota_coord_x = 400
pelota_coord_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Eventos teclado
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                player1_speed_y = -3
            if event.key == pygame.K_s:
                player1_speed_y = 3

            # Jugador 2
            if event.key == pygame.K_UP:
                player2_speed_y = -3
            if event.key == pygame.K_DOWN:
                player2_speed_y = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_speed_y = 0
            if event.key == pygame.K_s:
                player1_speed_y = 0
            if event.key == pygame.K_UP:
                player2_speed_y = 0
            if event.key == pygame.K_DOWN:
                player2_speed_y = 0

    if pelota_coord_y > 590 or pelota_coord_y < 10:
        pelota_speed_y *= -1

    # Comprueba si la pelota se sale por el lado izquierdo o derecho
    if pelota_coord_x > 800 or pelota_coord_x < 0:
        pelota_coord_x = 400
        pelota_coord_y = 300
        # Si sale de la pantalla, invierte la dirección
        pelota_speed_x *= -1
        pelota_speed_x *= -1

    # Movimiento jugadores y pelota
    player1_coord_y += player1_speed_y
    player2_coord_y += player2_speed_y

    pelota_coord_x += pelota_speed_x
    pelota_coord_y += pelota_speed_y

    screen.fill(BLACK)

    jugador1 = pygame.draw.rect(screen, WHITE, (player1_coord_x, player1_coord_y, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, WHITE, (player2_coord_x, player2_coord_y, player_width, player_height))
    pelota = pygame.draw.circle(screen, WHITE, (pelota_coord_x, pelota_coord_y), 10)

    # Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
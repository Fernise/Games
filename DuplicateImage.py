import pygame

pygame.init()

screen_size = (720, 720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

done = False

# Cargar imagen (Cambiar su imagen)
background = pygame.image.load("dino.jpg").convert()
player = pygame.image.load("tesla AI.jpg").convert()

# Borra colores
player.set_colorkey([0, 0, 0])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.blit(background, [80, 120])
    screen.blit(player, [x, y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
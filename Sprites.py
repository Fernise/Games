import pygame
import random

# It is necessary to change the images.
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino.jpg").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tesla AI.jpg").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen_size = (900, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

done = False

score = 0

dino_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    dino = Dino()
    dino.rect.x = random.randrange(900)
    dino.rect.y = random.randrange(600)

    dino_list.add(dino)
    all_sprite_list.add(dino)

player = Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.update()

    dino_hit_list = pygame.sprite.spritecollide(player, dino_list, True)

    for dino in dino_hit_list:
        score += 1
        print(score)


    screen.fill(WHITE)

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
import random
import time

pygame.init()

# surface of game
WIDTH = 1080
HEIGHT = 1000
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
road_g = pygame.image.load("image/road.png")

run = True
FPS = 60
SPEED = 5
SCORE = 0

# my picture is looking for left so I need rotate picture
def rotation_p(image, angle):
    return pygame.transform.rotate(image, angle)

# create player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/blue_car.png")  # load picture
        self.image = pygame.transform.scale(self.image, (200, 140))  # do picture 200x140
        self.image = rotation_p(self.image, 90)  # rotate
        self.rect = self.image.get_rect()  # get coordinate
        self.rect.center = (450, 800)
    
    def move(self):
        pressed_key = pygame.key.get_pressed()

        if self.rect.left > 130 and pressed_key[pygame.K_LEFT]:
            self.rect.x -= 10
        if self.rect.right < 950 and pressed_key[pygame.K_RIGHT]:
            self.rect.x += 10

# create Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/yellow_car.png")
        self.image = pygame.transform.scale(self.image, (200, 140))
        self.image = rotation_p(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(140, WIDTH - 140), 0)

    def move(self):
        self.rect.y += SPEED
        if self.rect.bottom > 1200:
            self.rect.top = 0
            self.rect.center = (random.randint(130, 950), 0)

# create Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/coin.png")
        self.image = pygame.transform.scale(self.image, (77, 77))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(135, WIDTH - 135), 0)
    
    def move(self):
        self.rect.y += 6
        if self.rect.bottom > 1200:
            self.rect.top = 0
            self.rect.center = (random.randint(135, WIDTH - 135), 0)

P1 = Player()
E1 = Enemy()
C = Coin()

# Creating Sprites Group
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1 

pygame.time.set_timer(INC_SPEED, 1000)


while run:
    tickrate = pygame.time.Clock()
    

    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.12
        if event.type == pygame.QUIT:
            run = False
    
    surface.blit(road_g, (0, -10))

    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()

 
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += 1
        C.rect.center = (random.randint(135, WIDTH - 135), 0)  # Respawn the coin because coin need to start y = 0 and with random

    
    if pygame.sprite.spritecollideany(P1, enemies):
        surface.fill((255, 0, 0)) 
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        
        time.sleep(2)
        run = False


    pygame.display.update()
    tickrate.tick(FPS)

pygame.quit()
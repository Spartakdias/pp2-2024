import pygame
import random
import time

pygame.init()


WIDTH = 1080
HEIGHT = 1000
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
road_g = pygame.image.load("image/road.png")
WEIGHTED_COINS = [(1, 'image/coin.png'), (2, 'image/cash.png')]
LEVEL = 1


run = True
FPS = 60
SPEED = 5
SCORE = 0


def rotation_p(image, angle):
    return pygame.transform.rotate(image, angle)

# create player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/blue_car.png")  
        self.image = pygame.transform.scale(self.image, (200, 140))  
        self.image = rotation_p(self.image, 90)  
        self.rect = self.image.get_rect()  
        self.rect.center = (450, 800)
    
    def move(self):
        pressed_key = pygame.key.get_pressed()

        if self.rect.left > 130 and pressed_key[pygame.K_LEFT]:
            self.rect.x -= 10
        if self.rect.right < 950 and pressed_key[pygame.K_RIGHT]:
            self.rect.x += 10


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


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight, self.image_path = random.choice(WEIGHTED_COINS)
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (88, 88))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(135, WIDTH - 135), 0)
    
    def move(self):
        self.rect.y += 6
        if self.rect.bottom > 1200:
            self.rect.top = 0
            self.rect.center = (random.randint(135, WIDTH - 135), 0)

    def update_coin(self):
        self.weight, self.image_path = random.choice(WEIGHTED_COINS)
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (77, 77))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(135, WIDTH - 135), 0)


P1 = Player()
E1 = Enemy()
C = Coin()


enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)


INC_SPEED = pygame.USEREVENT + 1 
pygame.time.set_timer(INC_SPEED, 1000)

font = pygame.font.Font('font/Roboto-Light.ttf', 55)  

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
        SCORE += C.weight
        C.update_coin()  
    if pygame.sprite.spritecollideany(P1, enemies):
        surface.fill((255, 0, 0)) 
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        run = False


    score_text = font.render('Score: ' + str(SCORE), True, (0,10,0))
    surface.blit(score_text, (120, 60))

   
    if SCORE == 10 and LEVEL == 1:  
        SPEED += 2  
        LEVEL += 1
    if SCORE == 20 and LEVEL == 2:  
        SPEED += 2
        LEVEL += 1
    if SCORE == 30 and LEVEL == 3:  
        SPEED += 2
        LEVEL += 1
    if SCORE == 40 and LEVEL == 4:  
        SPEED += 2
        LEVEL += 1

    pygame.display.update()
    tickrate.tick(FPS)

pygame.quit()
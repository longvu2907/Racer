import pygame
pygame.init()

display_width = 800
display_height = 600

FPS = 60
fpsClock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
animation = [pygame.image.load('R1.png'),pygame.image.load('R2.png')]
default = pygame.image.load('R1.png')

right = False
x = 1

def armorman():
    pygame.time.delay(100)
    global x
    global walkcount
    gameDisplay.fill((0,0,0))
    pygame.time.delay(100)

    if right:
        print(walkcount//3)
        gameDisplay.blit(animation[x%2], (x, 10))
    else:
        gameDisplay.blit(default, (x, 10))
    pygame.display.update()
    fpsClock.tick(FPS)
        



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 5
        right = True
    else:
        right = False
        walkcount = 0
    armorman()
    pygame.display.update()
    fpsClock.tick(FPS)


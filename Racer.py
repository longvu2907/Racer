import pygame
import random

display_width = 1080
display_height = 720

FPS = 144
fpsClock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racer')

car_width = 90
pos_y = [100,200,300,400,500]

class Car(object):
    def __init__(self, source):
        global pos_y
        self.x = 0
        self.y = random.choice(pos_y)
        self.speed = random.randrange(300,500,10) / 1000
        pos_y.remove(self.y)
        self.source = source
    def display(self):
        self.carIMG = pygame.image.load(self.source)
        gameDisplay.blit(self.carIMG, (self.x, self.y))
    def run(self):
        self.x += self.speed
        return self.x + car_width


def game():
    set = 'set1/' 
    Car1 = Car(set + 'car1.png' )
    Car2 = Car(set + 'car2.png' )
    Car3 = Car(set + 'car3.png' )
    Car4 = Car(set + 'car4.png' )
    Car5 = Car(set + 'car5.png' )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        gameDisplay.fill((0,0,0))
        Car1.display()
        Car2.display()
        Car3.display()
        Car4.display()
        Car5.display()
        if Car1.run() > display_width: 
            print("car 1 win")
            quit()
        elif Car2.run() > display_width:
            print("car 2 win")
            quit()
        elif Car3.run() > display_width: 
            print("car 3 win")
            quit()
        elif Car4.run() > display_width: 
            print("car 4 win")
            quit()
        elif Car5.run() > display_width: 
            print("car 5 win")
            quit()
        
        pygame.display.update()
        fpsClock.tick(FPS)
 

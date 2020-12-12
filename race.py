import pygame
import random

from pygame.constants import RESIZABLE, VIDEORESIZE


#initial window display
display_width = 1080
display_height = 720
FPS = 144
fpsClock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height), RESIZABLE)
pygame.display.set_caption('Racer')

#variable initial
car_width = 90
pos_y = [100,200,300,400,500]
skin = 'set1/' 
choice = 1
pointer = pygame.image.load('pointer.png')

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

class Car_choice():
    def __init__(self): 
        self.car_bet
        self.choice
        self.isChoice = False 
        self.yourChoice = 0

    def choice(self, x, source):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x <= mouse[0] <= x + car_width and gameDisplay.get_height()/2 - 50 <= mouse[1] <= gameDisplay.get_height()/2:
            self.isChoice = True
            self.car_bet(x, source)
            if click[0]:
                if x == self.x1:
                    return 1
                elif x == self.x2:
                    return 2
                elif x == self.x3:
                    return 3
                elif x == self.x4:
                    return 4
                elif x == self.x5:
                    return 5
        else:
            self.isChoice = False
            self.car_bet(x, source)

    def car_bet(self, x, source):
        carIMG = pygame.image.load(source)    
        if self.isChoice:
            carIMG = pygame.transform.smoothscale(carIMG, (150, 110))
            gameDisplay.blit(carIMG, (x, gameDisplay.get_height()/2 - 50))
        gameDisplay.blit(carIMG, (x, gameDisplay.get_height()/2 - 50))
        

    def bet(self):
        global choice
        global gameDisplay
        global display_height, display_width
        while True:
            mouse = pygame.mouse.get_pos()
            
            self.x1 = gameDisplay.get_width()/5 * 0 + 100
            self.x2 = gameDisplay.get_width()/5 * 1 + 90
            self.x3 = gameDisplay.get_width()/5 * 2 + 90
            self.x4 = gameDisplay.get_width()/5 * 3 + 90
            self.x5 = gameDisplay.get_width()/5 * 4 + 70
            gameDisplay.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()  
                if event.type == VIDEORESIZE:
                    display_width = event.w
                    display_height = event.h
                    gameDisplay = pygame.display.set_mode((display_width, display_height), RESIZABLE)                     
            self.car_bet(self.x1, skin + 'car1.png')
            self.car_bet(self.x2, skin + 'car2.png')
            self.car_bet(self.x3, skin + 'car3.png')
            self.car_bet(self.x4, skin + 'car4.png')
            self.car_bet(self.x5, skin + 'car5.png')
            gameDisplay.fill((0,0,0))
            if self.choice(self.x1, skin + 'car1.png') == 1:
                choice = 1
                break
            elif self.choice(self.x2, skin + 'car2.png') == 2:
                choice = 2
                break
            elif self.choice(self.x3, skin + 'car3.png') == 3:
                choice = 3
                break
            elif self.choice(self.x4, skin + 'car4.png') == 4:
                choice = 4
                break
            elif self.choice(self.x5, skin + 'car5.png') == 5:
                choice = 5
                break
            gameDisplay.blit(pointer, (mouse[0], mouse[1])) 
            pygame.display.update()
            fpsClock.tick(FPS)

def game():
    Car1 = Car(skin + 'car1.png' )
    Car2 = Car(skin + 'car2.png' )
    Car3 = Car(skin + 'car3.png' )
    Car4 = Car(skin + 'car4.png' )
    Car5 = Car(skin + 'car5.png' )
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
            if choice == 1: 
                print("YOU WIN")
            else: 
                print("YOU LOSE")
            quit()
        elif Car2.run() > display_width:
            if choice == 2:
                print("YOU WIN")
            else: 
                print("YOU LOSE")
            quit()
        elif Car3.run() > display_width:
            if choice == 3: 
                print("YOU WIN")
            else: 
                print("YOU LOSE")
            quit()
        elif Car4.run() > display_width: 
            if choice == 4: 
                print("YOU WIN")
            else: 
                print("YOU LOSE")
            quit()
        elif Car5.run() > display_width: 
            if choice == 5: 
                print("YOU WIN")
            else: 
                print("YOU LOSE")
            quit()
        
        pygame.display.update()
        fpsClock.tick(FPS)
 

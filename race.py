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
set = 'set1/' 
choice = 1

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
        self.x1 = 100
        self.x2 = 300
        self.x3 = 500
        self.x4 = 700
        self.x5 = 900
    def choice(self, x, source):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x <= mouse[0] <= x + car_width and 300 <= mouse[1] <= 350:
            pygame.draw.rect(gameDisplay, (255,255,255), [x,300,90,50])
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

    def car_bet(self, x, source):
        carIMG = pygame.image.load(source)
        gameDisplay.blit(carIMG, (x, 300))

    def bet(self):
        global set
        global choice
        while True:
            gameDisplay.fill((25,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()                       
            self.car_bet(self.x1, set + 'car1.png')
            self.car_bet(self.x2, set + 'car2.png')
            self.car_bet(self.x3, set + 'car3.png')
            self.car_bet(self.x4, set + 'car4.png')
            self.car_bet(self.x5, set + 'car5.png')
            if self.choice(self.x1, set + 'car1.png') == 1:
                choice = 1
                break
            elif self.choice(self.x2, set + 'car2.png') == 2:
                choice = 2
                break
            elif self.choice(self.x3, set + 'car3.png') == 3:
                choice = 3
                break
            elif self.choice(self.x4, set + 'car4.png') == 4:
                choice = 4
                break
            elif self.choice(self.x5, set + 'car5.png') == 5:
                choice = 5
                break
            pygame.display.update()
            fpsClock.tick(FPS)

        

def game():
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
 
run = Car_choice()
run.bet()
game()
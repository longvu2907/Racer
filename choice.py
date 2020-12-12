import pygame
import race

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
            pygame.display.update()
            fpsClock.tick(FPS)
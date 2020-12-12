import pygame
import login
import race

pygame.init()

screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)

run = True
login = login.login(screen)
pointer = pygame.image.load('pointer.png')
choice = race.Car_choice()


while True:
    pygame.mouse.set_visible(False)
    mouse = pygame.mouse.get_pos()
    screen.fill((20,20,20))
    result = login.screen_login(screen.get_width(), screen.get_height()) 
    if result == '(login successfully)':
        choice.bet()
        race.game()
    screen.blit(pointer, (mouse[0], mouse[1])) 
    pygame.display.update()
    
import pygame
from menu import GameMenu
from login import Login


class Game:
    def __init__(self):
        self.username = str
        self.FPS = 144
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
        pygame.display.set_caption('Racing bet')
        self.login_success = True
    def login_screen(self):
        login = Login(self.screen)
        while True:
            result =  login.login_diplay()
            if result == 'Login successfully':
                self.login_success = True
                self.username = login.username
                break
            pygame.display.update()
    def menu_screen(self):
        self.menu_display = GameMenu(self.screen, self.username)
        self.menu_display.bg_music.play()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            if self.login_success:
                self.menu_display.main_menu()
                pygame.display.update()
                self.login_success = not self.menu_display.log_out
            else:
                break
            
    def game_loop(self):
        pygame.init()
        print(self.login_screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.login_screen()
            self.menu_screen()
            
game = Game()
game.game_loop()
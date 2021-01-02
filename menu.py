import pygame
import time
from miniGame import mini_game
from newGame import NewGame
from data import userdata
from Profile import profile
from Shop import shop
from Setting import setting

class GameMenu:
    def __init__(self, screen ,name):
        pygame.init()
        self.screen = screen
        self.background = pygame.image.load('image/bg_menu.png')
        self.username = name
        self.data = userdata()
        self.userdata = self.data.get(self.username)
        self.money = self.userdata['money']
        self.log_out = False
        self.mini_game = True
        self.sound = True
        self.bg_music = pygame.mixer.Sound('sound/bg_music.mp3')

    def button(self, rect, radius=0, action=None, color_inactive = (149,144,118), color_active = (255,215,0)):
        click = pygame.mouse.get_pressed()
        if rect.collidepoint(pygame.mouse.get_pos()):
            color = color_active
            pygame.draw.rect(self.screen, color, rect, 5, border_radius = radius)
            if click[0] and action != None:
                pygame.event.wait()
                action()
        else:
            color = color_inactive
            pygame.draw.rect(self.screen, color, rect, 3, border_radius = radius)      

    def text(self, txt, x, y, size, color=(255,255,255),charfont='calibri',format='left'):
        font = pygame.font.SysFont(charfont, size)
        text = font.render(txt, True, color)
        if format == 'left':
            self.screen.blit(text, (x, y))
        elif format == 'center':
            text_rect = text.get_rect(center = (x,y))
            self.screen.blit(text, text_rect)

    def main_menu(self):
        if self.sound:
            self.bg_music.play()
        else:
            self.bg_music.stop()
        self.screen.blit(pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height())), (0,0))
        screenw = self.screen.get_width()
        screenh = self.screen.get_height()
        mid_w = screenw/2
        mid_h = screenh/2
        self.data = userdata()
        self.userdata = self.data.get(self.username)
        self.money = self.userdata['money']

        # Init button properties
        btn_w = mid_w/3.2
        btn_h = mid_h/7.2
        btn_logout = pygame.Rect(screenw-btn_w/2, 10, btn_w/2.5, btn_h/2)
        btn_start = pygame.Rect(mid_w-btn_w/2, mid_h*3/5, btn_w, btn_h)
        btn_minigame = pygame.Rect(mid_w-btn_w/2, btn_start.y+mid_h/4.32, btn_w, btn_h)
        btn_profile = pygame.Rect(mid_w-btn_w/2, btn_minigame.y+mid_h/4.32, btn_w, btn_h) 
        btn_shop = pygame.Rect(mid_w-btn_w/2, btn_profile.y+mid_h/4.32, btn_w, btn_h)  
        btn_setting = pygame.Rect(mid_w-btn_w/2, btn_shop.y+mid_h/4.32, btn_w, btn_h)     
        btn_quit = pygame.Rect(mid_w-btn_w/2, btn_setting.y+mid_h/4.32, btn_w, btn_h)

        # Create button
        self.text('MAIN MENU', mid_w, mid_h/7.2, int(mid_w/6.5), (220,210,160), 'algerian', 'center')
        self.text('Welcome ' + self.username, 5, 5, 30, (220,210,160), 'timenewroman')
        self.button(btn_logout, 10, self.logout)
        self.text('Logout', btn_logout.x+btn_logout.w/2, btn_logout.y+btn_logout.h/2, 25, (220,210,160), 'timenewroman','center')
        self.button(btn_start, 10, self.start)
        self.text('Start', btn_start.x+btn_start.w/2, btn_start.y+btn_start.h/2, int(mid_w/16),(220,210,160), 'algerian','center')
        self.button(btn_minigame, 10, self.minigame)
        self.text('Minigame', btn_minigame.x+btn_minigame.w/2, btn_minigame.y+btn_minigame.h/2, int(mid_w/16),(220,210,160), 'algerian','center')
        self.button(btn_profile, 10, self.profile)
        self.text('Profile', btn_profile.x+btn_profile.w/2, btn_profile.y+btn_profile.h/2, int(mid_w/16),(220,210,160), 'algerian','center')
        self.button(btn_shop, 10, self.shop)
        self.text('Shop', btn_shop.x+btn_shop.w/2, btn_shop.y+btn_shop.h/2, int(mid_w/16),(220,210,160), 'algerian','center')
        self.button(btn_setting, 10, self.setting)
        self.text('Setting', btn_setting.x+btn_setting.w/2, btn_setting.y+btn_setting.h/2, int(mid_w/16),(220,210,160), 'algerian','center')
        self.button(btn_quit, 10, pygame.quit)
        self.text('Quit', btn_quit.x+btn_quit.w/2, btn_quit.y+btn_quit.h/2, int(mid_w/16),(220,210,160), 'algerian','center')
        if not self.mini_game:
            self.text('Your money > 50000$', mid_w, mid_h/7.2+100, 30, (220,210,160), 'algerian', 'center')
            pygame.display.update()
            pygame.time.delay(1000)
            self.mini_game = True
            
    def logout(self):
        self.bg_music.stop()
        self.log_out = True

    def start(self):
        self.bg_music.stop()
        play = NewGame(self.screen, self.username)
        play.start()

    def minigame(self):
        if self.money < 50000:
            self.bg_music.stop()
            minigame = mini_game(self.screen, self.username)
            minigame.start()
        else:
            self.mini_game = False        

    def profile(self):      
        self.bg_music.stop()
        stat = profile(self.screen, self.username)
        stat.main()

    def shop(self):
        self.bg_music.stop()
        Shop = shop(self.screen, self.username)
        Shop.main()
        
    def setting(self):
        self.bg_music.stop()
        Setting = setting(self.screen, self.sound)
        Setting.main()
        self.sound = Setting.sound
        
             


import pygame
from data import userdata

class shop:
    def __init__(self, screen, username):
        self.screen = screen
        self.username = username
        self.data = userdata()
        self.userdata = self.data.get(username)
        self.money_init = self.userdata['money']
        self.money = self.userdata['money']
        self.items = self.userdata['items']
        self.mainmenu = False
    def text(self, txt, x, y, size, color=(255,255,255),charfont='calibri',format='left'):
            font = pygame.font.SysFont(charfont, size)
            text = font.render(txt, True, color)
            if format == 'left':
                self.screen.blit(text, (x, y))
            elif format == 'center':
                text_rect = text.get_rect(center = (x,y))
                self.screen.blit(text, text_rect)    
    def button(self, rect, radius=0, action=None, color_inactive = (149,144,118), color_active = (255,215,0)):
        click = pygame.mouse.get_pressed()
        if rect.collidepoint(pygame.mouse.get_pos()):
            color = color_active
            pygame.draw.rect(self.screen, color, rect, 0, border_radius = radius)
            if click[0] and action != None:
                action()
        else:
            color = color_inactive
            pygame.draw.rect(self.screen, color, rect, 3, border_radius = radius)

    def update(self):
        self.data.update(self.username, self.userdata['password'], self.money, self.items)

    def back(self):
        self.mainmenu = True
    def display(self):
        screen_w = self.screen.get_width()
        screen_h = self.screen.get_height()
        #Background
        background = pygame.transform.scale(pygame.image.load('image/bg_menu.png'),(self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background, (0,0))
        #Title
        self.text('SHOP', screen_w/2, screen_h/14.4, int(screen_w/13), (220,210,160), 'algerian', 'center')
        #Back button
        btn_back = pygame.Rect(10,10,120,35)
        self.button(btn_back, 10, self.back)
        self.text('Back', btn_back.x+btn_back.w/2, btn_back.y+btn_back.h/2, 30, (255,255,255), 'algerian', 'center')
        pygame.display.update()
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.display()
            if self.mainmenu:
                break
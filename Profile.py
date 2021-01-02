import pygame
from data import userdata

class profile:
    def __init__(self, screen, name):
        self.screen = screen
        self.data = userdata()
        self.userdata = self.data.get(name)
        self.name = self.userdata['name']
        self.money = self.userdata['money']
        self.item = self.userdata['items']
        self.bg = pygame.image.load('image/bg_profile.png')
        self.Back = False
        
    def button(self, rect, radius=0, action=None, color_inactive = (149,144,118), color_active = (255,215,0)):
        click = pygame.mouse.get_pressed()
        if rect.collidepoint(pygame.mouse.get_pos()):
            color = color_active
            pygame.draw.rect(self.screen, color, rect, 5, border_radius = radius)
            if click[0] and action != None:
                pygame.event.wait()
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
    def stat(self):
        #Background
        self.screen.blit(pygame.transform.scale(self.bg,
        (self.screen.get_width(), self.screen.get_height())), (0,0))
        mid_w = self.screen.get_width()/2
        mid_h = self.screen.get_height()/2
        #Button Back
        btn_back = pygame.Rect(10,10,120,35)
        self.button(btn_back, 10, self.back)
        self.text('Back', btn_back.x+btn_back.w/2, btn_back.y+btn_back.h/2, 30, (220,210,160), 'algerian', 'center')
        #Stat
        self.text('PROFILE', mid_w, mid_h/7.2, int(mid_w/6.5), (220,210,160), 'algerian', 'center')
        self.text('name:   ' + self.name, mid_w/1.5, mid_h/7.2+mid_h/3.6, 40, (220,210,160), 'algerian', 'left')
        self.text('money: ' + str(self.money) + ' $', mid_w/1.5, mid_h/7.2+mid_h/2.4, 40, (220,210,160), 'algerian', 'left') 
        self.text('history', mid_w, mid_h/7.2+mid_h/1.36, 40, (220,210,160), 'algerian', 'center')
        history_data = self.data.history(self.name)
        y = mid_h/1.044
        for i in range(len(history_data)):
            self.text(history_data[i], mid_w/1.5+5, y, int(mid_h/22.5))
            y += mid_h/18
        pygame.display.update()
    def back(self):
        self.Back = True
    def main(self):
        while not self.Back:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.stat()


import pygame

class setting:
    def __init__(self, screen, sound):
        self.screen = screen
        self.mainmenu = False
        self.sound = sound 
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
                pygame.event.wait()
                action()
        else:
            color = color_inactive
            pygame.draw.rect(self.screen, color, rect, 3, border_radius = radius)

    def display(self):
        sound_on = pygame.transform.scale(pygame.image.load('image/sound_on.png'), (int(self.screen.get_width()/11.01), int(self.screen.get_width()/11.01)))
        sound_off = pygame.transform.scale(pygame.image.load('image/sound_off.png'), (int(self.screen.get_width()/11.01), int(self.screen.get_width()/11.01)))
        screen_w = self.screen.get_width()
        screen_h = self.screen.get_height()
        #Background
        background = pygame.transform.scale(pygame.image.load('image/bg_menu.png'),(self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background, (0,0))
        #Title
        self.text('SETTING', screen_w/2, screen_h/14.4, int(screen_w/13), (220,210,160), 'algerian', 'center')
        #Back button
        btn_back = pygame.Rect(10,10,120,35)
        self.button(btn_back, 10, self.back)
        self.text('Back', btn_back.x+btn_back.w/2, btn_back.y+btn_back.h/2, 30, (255,255,255), 'algerian', 'center')
        #Sound button
        btn_sound = pygame.Rect(screen_w/2.45, screen_h/3.07, screen_w/5.5, screen_h/6.51)
        if self.sound:
            self.screen.blit(sound_on, (screen_w/3.243, screen_h/3.07))
            self.button(btn_sound, 40, self.Sound)
            self.text('On', btn_sound.x+btn_sound.w/2, btn_sound.y+btn_sound.h/2, 60, (255,255,255), 'comicsansms', 'center')
        else:
            self.screen.blit(sound_off, (screen_w/3.243, screen_h/3.07))
            self.button(btn_sound, 40, self.Sound)
            self.text('Off', btn_sound.x+btn_sound.w/2, btn_sound.y+btn_sound.h/2, 60, (255,255,255), 'comicsansms', 'center')
        pygame.display.update()
    def back(self):
        self.mainmenu = True
    def Sound(self):
        self.sound = not self.sound
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            if self.mainmenu:
                break
            self.display()
import pygame
import data

data = data.loginData()
class Login:
    def __init__(self, screen):
        self.username = ''
        self.password = ''
        self.hiddenpass = ''
        self.screen = screen
        self.color_inactive = (149,144,118)
        self.color_active = (235,210,80)
        self.color_name = self.color_inactive
        self.color_pass = self.color_inactive
        self.input_name = False
        self.input_pass = False
        self.result = ''

    def text(self, txt, x, y, size, color=(255,255,255), charfont='calibri', format='left'):
        font = pygame.font.SysFont(charfont, size)
        text = font.render(txt, True, color)
        if format == 'left':
            self.screen.blit(text, (x, y))
        elif format == 'center':
            text_rect = text.get_rect(center=(x,y))
            self.screen.blit(text, text_rect)
    
    def button(self, rect, radius=0, action=None, color_inactive = (149,144,118), color_active = (255,215,0)):
        click = pygame.mouse.get_pressed()
        if rect.collidepoint(pygame.mouse.get_pos()):
            color = color_active
            pygame.draw.rect(self.screen, color, rect, 5, border_radius = radius)
            if click[0] == 1 and action != None:
                action()
        else:
            color = color_inactive
            pygame.draw.rect(self.screen, color, rect, 3, border_radius = radius)

    def login_diplay(self): 
        screenw = self.screen.get_width()
        screenh = self.screen.get_height()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mid_x = screenw/2 
        mid_y = screenh/2

        #Background
        background = pygame.image.load('image/bg_login.png')
        self.screen.blit(pygame.transform.scale(background, (screenw, screenh)), (0,0))

        #Title
        self.text('Racing bet',mid_x, mid_y-175,125,(234,224,174),'algerian','center')

        #Input Username, Password:      
        width = 300
        height = 40
        NameRect = pygame.Rect(mid_x-width/2, mid_y*2/3 + 100, width, height)
        PassRect = pygame.Rect(mid_x-width/2, mid_y*2/3 + 185, width, height)
        self.text('UserName',NameRect.x, NameRect.y - 30,27)
        pygame.draw.rect(self.screen, self.color_name, NameRect, 2, border_radius=5)
        self.text('Password',PassRect.x, PassRect.y - 30,27)
        pygame.draw.rect(self.screen, self.color_pass, PassRect, 2, border_radius=5)
        if click[0]:
            if NameRect.x<=mouse[0]<=NameRect.x+NameRect.w and NameRect.y<=mouse[1]<=NameRect.y+NameRect.h:
                self.input_name = True
            else:
                self.input_name = False
            if PassRect.x<=mouse[0]<=PassRect.x+PassRect.w and PassRect.y<=mouse[1]<=PassRect.y+PassRect.h:
                self.input_pass = True
            else:
                self.input_pass = False
        self.color_name = self.color_active if self.input_name else self.color_inactive
        self.color_pass = self.color_active if self.input_pass else self.color_inactive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if self.input_name:
                    if event.key == pygame.K_RETURN:
                        self.input_name = False
                        self.input_pass = True
                    elif event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    else:
                        if event.unicode.isalnum():
                            self.username += event.unicode 
                elif self.input_pass:
                    if event.key == pygame.K_RETURN:
                        self.input_pass = False
                        if len(self.username) == 0 and len(self.password) == 0:
                            self.result = 'Not be empty'
                        elif len(self.username) < 3:
                            self.result = 'Username must be at least 3 characters'
                        elif len(self.password) < 3:
                            self.result = 'Password must be at least 3 characters'
                        else: 
                            self.result = data.login(self.username, self.password)
                    elif event.key == pygame.K_BACKSPACE:
                        self.password = self.password[:-1]
                        self.hiddenpass = self.hiddenpass[:-1]
                    else:
                        if event.unicode.isalnum():
                            self.password += event.unicode
                            self.hiddenpass += '*'
                else:
                    if event.key == pygame.K_RETURN:
                        self.input_name = True
        self.text(self.username,NameRect.x+7, NameRect.y+7,27,(234,224,174))
        self.text(self.hiddenpass,PassRect.x+7, PassRect.y+13,27,(234,224,174))
        if len(self.username) >= 22:
            self.username = self.username[:-1]
        if len(self.password) >= 23:
            self.password = self.password[:-1]
            self.hiddenpass = self.hiddenpass[:-1]

        #Login button, Register button
        LoginButton = pygame.Rect(PassRect.x+60, PassRect.y+75, 180, 50)
        RegisterButton = pygame.Rect(PassRect.x+35, PassRect.y+175, 230, 40)
        self.button(LoginButton, 10)
        self.button(RegisterButton, 10) 
        self.text('----------OR----------', mid_x, LoginButton.y+75, 20, (180,180,180), 'calibri', 'center')  
        if LoginButton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.color_active, LoginButton, border_radius=15)
            self.text('Login',LoginButton.x+LoginButton.w/2,LoginButton.y+LoginButton.h/2,50,(255,255,255),'calibri-bold','center')
            if click[0]:
                pygame.event.wait()
                if len(self.username) == 0 or len(self.password) == 0:
                    self.result = 'Not be empty'
                elif len(self.username) < 3:
                    self.result = 'Username must be at least 3 characters'
                elif len(self.password) < 3:
                    self.result = 'Password must be at least 3 characters'
                else: 
                    self.result = data.login(self.username, self.password)
        else:
            self.text('Login',LoginButton.x+LoginButton.w/2,LoginButton.y+LoginButton.h/2,50,(234,224,174),'calibri-bold','center')
        if RegisterButton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.color_active, RegisterButton, border_radius=15)
            self.text('Register',RegisterButton.x+RegisterButton.w/2,RegisterButton.y+RegisterButton.h/2,40,(255,255,255),'calibri-bold','center')
            if click[0]:
                pygame.event.wait()
                if len(self.username) == 0 or len(self.password) == 0:
                    self.result = 'Not be empty'
                elif len(self.username) < 3:
                    self.result = 'Username must be at least 3 characters'
                elif len(self.password) < 3:
                    self.result = 'Password must be at least 3 characters'
                else:
                    self.result = data.register(self.username, self.password)        
        else:   
            self.text('Register',RegisterButton.x+RegisterButton.w/2,RegisterButton.y+RegisterButton.h/2,40,(234,224,174),'cilibri-bold','center')
        self.text (self.result, mid_x, PassRect.y+55, 15,(255,255,255),'calibri','center')
        return self.result

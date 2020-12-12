import pygame
import test
pygame.init()
data = test.loginData()
class login(object):
    def __init__(self, screen):
        self.username = ''
        self.password = ''
        self.hiddenpass = ''
        self.screen = screen
        self.color_inactive = (141,182,205)
        self.color_active = (28,134,238)
        self.color_name = self.color_inactive
        self.color_pass = self.color_inactive
        self.input_name = False
        self.input_pass = False
        self.result = ''
    def text(self, txt, x, y, color, size):
        font = pygame.font.SysFont('calibri', size)
        text = font.render(txt, True, color)
        self.screen.blit(text, (x, y))
    def screen_login(self, screenw, screenh):
        font = pygame.font.SysFont('calibri', 27) 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #input username, password:
        centerscreenx = screenw/2 
        centerscreeny = screenh/2
        width = 300
        height = 40
        NameRect = pygame.Rect(centerscreenx-width/2, centerscreeny*2/3, width, height)
        PassRect = pygame.Rect(centerscreenx-width/2, centerscreeny*2/3 + 75, width, height)
        self.text('User Name',NameRect.x, NameRect.y - 30,(255,255,255),27)
        pygame.draw.rect(self.screen, self.color_name, NameRect, 2, border_radius=5)
        self.text('Password',PassRect.x, PassRect.y - 30,(255,255,255),27)
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
                        if len(self.username) < 5 and len(self.password) < 5:
                            self.result = '(username and password must be at least 5 characters)'
                        elif len(self.username) < 5:
                            self.result = '(username must be at least 5 characters)'
                        elif len(self.password) < 5:
                            self.result = '(password must be at least 5 characters)'
                        else: 
                            self.result = data.login(self.username, self.password)
                    elif event.key == pygame.K_BACKSPACE:
                        self.password = self.password[:-1]
                        self.hiddenpass = self.hiddenpass[:-1]
                    else:
                        if event.unicode.isalnum():
                            self.password += event.unicode
                            self.hiddenpass += '*'
        self.text(self.username,NameRect.x+7, NameRect.y+7,(255,255,255),27)
        self.text(self.hiddenpass,PassRect.x+7, PassRect.y+13,(255,255,255),27)
        if len(self.username) >= 23:
            self.username = self.username[:-1]
        if len(self.password) >= 23:
            self.password = self.password[:-1]
            self.hiddenpass = self.hiddenpass[:-1]

        #login button, register button
        LoginBox = pygame.Rect(PassRect.x-75, PassRect.y+100, 150, 60)
        RegisterBox = pygame.Rect(PassRect.x+225, PassRect.y+100, 150, 60)
        pygame.draw.rect(self.screen, self.color_inactive, LoginBox, border_radius=15)
        pygame.draw.rect(self.screen, self.color_inactive, RegisterBox, border_radius=15)     
        if LoginBox.x<=mouse[0]<=LoginBox.x+LoginBox.w and LoginBox.y<=mouse[1]<=LoginBox.y+LoginBox.h:
            pygame.draw.rect(self.screen, self.color_active, LoginBox, border_radius=15)
            if click[0]:
                pygame.event.wait()
                if len(self.username) < 5 and len(self.password) < 5:
                    self.result = '(username and password must be at least 5 characters)'
                elif len(self.username) < 5:
                    self.result = '(username must be at least 5 characters)'
                elif len(self.password) < 5:
                    self.result = '(password must be at least 5 characters)'
                else: 
                    self.result = data.login(self.username, self.password)
        if RegisterBox.x<=mouse[0]<=RegisterBox.x+RegisterBox.w and RegisterBox.y<=mouse[1]<=RegisterBox.y+RegisterBox.h:
            pygame.draw.rect(self.screen, self.color_active, RegisterBox, border_radius=15)
            if click[0]:
                pygame.event.wait()
                if len(self.username) < 5 and len(self.password) < 5:
                    self.result = '(username and password must be at least 5 characters)'
                elif len(self.username) < 5:
                    self.result = '(username must be at least 5 characters)'
                elif len(self.password) < 5:
                    self.result = '(password must be at least 5 characters)'
                else:
                    self.result = data.register(self.username, self.password)           
        self.text('Login',LoginBox.x+45,LoginBox.y+15,(255,255,255),27)
        self.text('Register',RegisterBox.x+32,RegisterBox.y+15,(255,255,255),27)
        self.text (self.result, centerscreenx-len(self.result)*6/2, PassRect.y+50,(255,255,255), 15)
        return self.result
                
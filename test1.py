import pygame as pg
import test
import race
from pygame.constants import RESIZABLE, VIDEORESIZE

pg.init()

screen = pg.display.set_mode((1080, 720), RESIZABLE)

def main():
    global screen
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()  
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color1 = color_inactive
    color2 = color_inactive
    nameActive = False
    passwActive = False
    username = ''
    password = ''
    passwdisplay = ''
    done = False
    choice = True
    isLogin = False
    isRegister = False
    data = test.loginData()
    while not done:
        while choice:
            screen.blit(pointer, (mouse[0], mouse[1])) 
            login_box = pg.Rect(screen.get_width()/2 - 75, screen.get_height()/2 - 50, 150, 50)
            register_box = pg.Rect(screen.get_width()/2 - 75, screen.get_height()/2 + 50, 150, 50)     
            txt_login = font.render("Login", True, (255,255,255))
            txt_register = font.render("Register", True, (255,255,255))
            pg.draw.rect(screen, (0,255,0), login_box)
            pg.draw.rect(screen, (255,0,10), register_box)
            screen.blit(txt_login, (login_box.x+45,login_box.y+15))
            screen.blit(txt_register, (register_box.x+30,register_box.y+15))           
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == VIDEORESIZE:
                    displaywidth = event.w
                    displayheight = event.h
                    screen = pg.display.set_mode((displaywidth, displayheight), RESIZABLE)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if login_box.collidepoint(event.pos):
                        isLogin = True
                        choice = False
                    elif register_box.collidepoint(event.pos):
                        isRegister = True
                        choice = False
            pg.display.update()
            clock.tick(144)
        nameInput_box = pg.Rect(screen.get_width()/2 - 75, screen.get_height()/2 - 30, 140, 32)
        passwInput_box = pg.Rect(screen.get_width()/2 - 75, screen.get_height()/2 + 30, 140, 32)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if nameInput_box.collidepoint(event.pos):
                    nameActive = not nameActive   
                else:    
                    nameActive = False
                if passwInput_box.collidepoint(event.pos):
                    passwActive = not passwActive
                else:    
                    passwActive = False
                color1 = color_active if nameActive else color_inactive
                color2 = color_active if passwActive else color_inactive
            if event.type == pg.KEYDOWN:
                if nameActive:
                    if event.key == pg.K_RETURN:
                        nameActive = False
                        passwActive = True
                    elif event.key == pg.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif passwActive:
                    if event.key == pg.K_RETURN:
                        if isLogin:
                            while True:
                                islogin = data.login(username, password)
                                if islogin:
                                    race.game()
                                else:
                                    main()
                        elif isRegister:
                            while True:
                                if data.register(username, password):
                                    main()
                                else: 
                                    main()
                                
                    elif event.key == pg.K_BACKSPACE:
                        password = password[:-1]
                        passwdisplay = passwdisplay[:-1]
                    else:
                        password += event.unicode
                        passwdisplay += '*'
            color1 = color_active if nameActive else color_inactive
            color2 = color_active if passwActive else color_inactive

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface1 = font.render(username, True, color1)
        txt_surface2 = font.render(passwdisplay, True, color1)
        # Resize the box if the text is too long.
        width1 = max(200, txt_surface1.get_width()+10)
        width2 = max(200, txt_surface2.get_width()+10)
        nameInput_box.w = width1
        passwInput_box.w = width2
        # Blit the text.
        txt_username = font.render("User Name", True, (255,255,255))
        txt_password = font.render("Password", True, (255,255,255))
        screen.blit(txt_username, ((nameInput_box.x, nameInput_box.y-25)))
        screen.blit(txt_password, ((passwInput_box.x, passwInput_box.y-25)))
        screen.blit(txt_surface1, (nameInput_box.x+5, nameInput_box.y+5))
        screen.blit(txt_surface2, (passwInput_box.x+5, passwInput_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color1, nameInput_box, 2)
        pg.draw.rect(screen, color2, passwInput_box, 2)

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    while True:
        main()

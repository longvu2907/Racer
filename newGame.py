import pygame 
import random
from datetime import datetime
from data import userdata


class NewGame:
    def __init__(self, screen, username):
        self.screen = screen
        self.username = username
        self.data = userdata()
        self.userdata = self.data.get(username)
        self.money_init = self.userdata['money']
        self.money = self.userdata['money']
        self.init = self.before_racing(screen, self.money)
        self.mode = self.init.mode
        self.skin = self.init.skin
        self.choice = self.init.choice
        self.money_bet = self.init.money_bet
        self.play = self.racing(screen, self.skin, self.choice, self.mode, self.username)
        self.fpsClock = pygame.time.Clock()
        self.now = datetime.now()


    def update(self, money):
        self.money = money
        self.mode = self.init.mode
        self.skin = self.init.skin
        self.choice = self.init.choice
        self.money_bet = self.init.money_bet
        self.data.update(self.userdata['name'], self.userdata['password'], self.money, self.userdata['items'] )
              
    def start(self):
        while True:
            self.init = self.before_racing(self.screen, self.money)
            self.play = self.racing(self.screen, self.skin, self.choice, self.mode, self.username)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                self.update(self.init.money)
                if self.init.picking():
                    break
                if self.init.mainmenu:
                    break
                pygame.display.update()
                self.fpsClock.tick(144)

            if not self.init.mainmenu:
                self.play = self.racing(self.screen, self.skin, self.choice, self.mode, self.username)
                self.play.start_effect()
            else:
                break

            while True:
                self.play.start()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                if self.play.finished:
                    break
                pygame.display.update()
                self.fpsClock.tick(144)

            if not self.init.mainmenu:
                rank = self.play.your_car.rank
                self.result = self.after_racing(self.money, self.money_bet, rank)
                self.result.update_data()
                self.update(self.result.money)
                res = self.result.money - self.money_init
                if res > 0:
                    sign = '+'
                else:
                    sign = ''  
                history_data = self.now.strftime("%d/%m/%Y(%H:%M:%S): ") + "Betting, rank " + str(rank) + " " + sign + str(res) + '$' + ' -> ' + str(self.result.money) + '$'
                self.data.update_history(self.username, history_data)   

            while True:
                if not self.init.mainmenu:
                    self.play.finished_effect()
                if self.play.playagain:
                    break
                if self.play.mainmenu:
                    break

            if self.play.mainmenu:
                break

            

    class items:
        def __init__(self):
            pass

    class car:
        def __init__(self, screen, source, x, y):
            self.source = source
            self.screen = screen
            self.x = x
            self.y = y
            self.speed = random.randint(int(self.screen.get_width()/10.5),int(self.screen.get_width()/8.5))/100
            self.original_speed = self.speed
            self.rank = int
            self.car_w = int(self.screen.get_width()/6.3)
            self.car_h = int(self.screen.get_height()/7.5)
            self.car = pygame.image.load(self.source)
            self.car = pygame.transform.scale(self.car, (self.car_w, self.car_h))
            self.random_item = random.randint(1, 100)
            self.go_back = 0
            self.stun_time = 0
            self.boost_time = 0
            self.slow_time = 0
            self.teleport_time = 0
            self.teleback_time = 0
        def display(self, a = 12, b = 14.4):
            self.car_w = int(self.screen.get_width()/a)
            self.car_h = int(self.screen.get_height()/b)
            self.screen.blit(pygame.transform.scale(self.car, (self.car_w, self.car_h)), (self.x, self.y)) 
        def run(self):
            self.car_w = int(self.screen.get_width()/12)
            self.car_h = int(self.screen.get_height()/14.4)
            self.screen.blit(pygame.transform.scale(self.car, (self.car_w, self.car_h)), (self.x, self.y)) 
            if self.x < self.screen.get_width()/1.1:
                self.x += self.speed

        def stun(self):
            self.speed = 0
            effect_stun = pygame.image.load('image/stun.png')
            self.screen.blit(pygame.transform.scale(effect_stun, (self.car_w, self.car_h)), (self.x, self.y))
        def boost(self):
            self.speed = self.original_speed*1.5
            effect_boost = pygame.image.load('image/boost.png')
            self.screen.blit(pygame.transform.scale(effect_boost, (self.car_w, self.car_h)), (self.x, self.y))
        def slow(self):
            self.speed = self.original_speed*0.5
            effect_slow = pygame.image.load('image/slow.png')
            self.screen.blit(pygame.transform.scale(effect_slow, (self.car_w, self.car_h)), (self.x, self.y))
        def run_back(self):
            self.speed = -self.speed
        def teleport(self):
            effect_teleport = pygame.image.load('image/teleport1.png')
            self.screen.blit(pygame.transform.scale(effect_teleport, (self.car_w, self.car_h)), (self.x, self.y))
            self.speed = 0
            self.teleport_time += 1
            if self.teleport_time == 20:
                self.x = 5000
        def start_again(self):
            effect_teleport = pygame.image.load('image/teleport2.png')
            self.screen.blit(pygame.transform.scale(effect_teleport, (self.car_w, self.car_h)), (self.x, self.y))
            self.speed = 0
            self.teleback_time += 1
            if self.teleback_time == 20:
                self.x = 0
            
        def finished(self, rank):
            if self.x > self.screen.get_width()/1.1:
                self.rank = rank
                self.x = self.screen.get_width()/1.1
                return True
            return False
            
    class road:
        def __init__(self, screen, mode):
            self.screen = screen
            self.mode = mode
            if mode == 'long':
                self.road = pygame.image.load('image/countryside1.png')
                self.item1_lane1 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane2 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane3 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane4 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane5 = random.randint(200, self.screen.get_width()-200)
            elif mode == 'short':
                self.road = pygame.image.load('image/beach.png')
                self.item1_lane1 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane2 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane3 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane4 = random.randint(200, self.screen.get_width()-200)
                self.item1_lane5 = random.randint(200, self.screen.get_width()-200)
            self.road_finished = pygame.image.load('image/finished.png')
            self.x = 0
        def display(self):
            if self.mode == 'long':
                self.screen.blit(pygame.transform.scale(self.road, 
                (self.screen.get_width(),self.screen.get_height())), (self.x, 0))
            elif self.mode == 'short':
                self.screen.blit(pygame.transform.scale(self.road, 
                (self.screen.get_width(),self.screen.get_height())), (self.x, 0))
        def move(self, speed):
            if self.x > -self.screen.get_width():
                self.x -= speed
            self.screen.blit(pygame.transform.scale(self.road[0], 
            (self.screen.get_width(),self.screen.get_height())), (self.x, 0))
            self.screen.blit(pygame.transform.scale(self.road[1], 
            (self.screen.get_width(),self.screen.get_height())), (self.x + self.screen.get_width(),0))
            
    class before_racing:
        def __init__(self, screen, money):
            self.screen = screen
            self.mode = str
            self.choice = int
            self.bg = pygame.image.load('image/bg_picking.png')
            self.skin = 'image/set1/'
            self.money_bet = int
            self.money = money
            self.road_choice = False
            self.skin_choice = False
            self.car_choice = False
            self.money_choice = False
            self.error = False
            self.mainmenu = False

        def choose_effect(self, img, loc):
            mask = pygame.mask.from_surface(img)
            mask_surface = mask.to_surface()
            mask_surface.set_colorkey((0,0,0))
            self.screen.blit(mask_surface, (loc[0]-3, loc[1]))
            self.screen.blit(mask_surface, (loc[0]+3, loc[1]))
            self.screen.blit(mask_surface, (loc[0], loc[1]-3))
            self.screen.blit(mask_surface, (loc[0], loc[1]+3))
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
                    pygame.event.wait()
                    action()
            else:
                color = color_inactive
                pygame.draw.rect(self.screen, color, rect, 3, border_radius = radius)

        def pick_road(self):
            click = pygame.mouse.get_pressed()
            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            #Button back
            btn_back = pygame.Rect(10,50,120,35)
            self.button(btn_back, 10, self.back)
            self.text('Back', btn_back.x+btn_back.w/2, btn_back.y+btn_back.h/2, 30, (255,255,255), 'algerian', 'center')
            #Init image
            sroad_rect = pygame.Rect(screen_w/11.3, screen_h/2.8, screen_w/3, screen_h/3)
            lroad_rect = pygame.Rect(screen_w/1.67, screen_h/2.8, screen_w/3, screen_h/3)
            self.text('CHOOSE ROAD', screen_w/2, screen_h/7.2, 70, (255,255,255), 'comicsansms', 'center')
            self.text('Beach', sroad_rect.x+sroad_rect.w/2, sroad_rect.y-50, 50, (255,255,255), 'comicsansms', 'center')
            self.text('Countryside', lroad_rect.x+lroad_rect.w/2, lroad_rect.y-50, 50, (255,255,255), 'comicsansms', 'center')
            sroad = pygame.transform.scale(pygame.image.load('image/beach.png'), (sroad_rect.w, sroad_rect.h))
            lroad = pygame.transform.scale(pygame.image.load('image/countryside1.png'), (sroad_rect.w, sroad_rect.h))
            #Choice
            if sroad_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(sroad, [sroad_rect.x, sroad_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.mode = 'short'
                    self.road_choice = True
            elif lroad_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(lroad, [lroad_rect.x, lroad_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.mode = 'long'
                    self.road_choice = True
            self.screen.blit(sroad, (sroad_rect.x, sroad_rect.y))        
            self.screen.blit(lroad, (lroad_rect.x, lroad_rect.y))

        def pick_skin(self):
            click = pygame.mouse.get_pressed()
            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            #Button back
            btn_back = pygame.Rect(10,50,120,35)
            self.button(btn_back, 10, self.back)
            self.text('Back', btn_back.x+btn_back.w/2, btn_back.y+btn_back.h/2, 30, (255,255,255), 'algerian', 'center')
            #Init image
            set1_rect = pygame.Rect(screen_w/35.5, screen_h/2-100, screen_w/6, screen_w/6)
            set2_rect = pygame.Rect(screen_w/4.5, screen_h/2-100, screen_w/6, screen_w/6)
            set3_rect = pygame.Rect(screen_w/2.4, screen_h/2-100, screen_w/6, screen_w/6)
            set4_rect = pygame.Rect(screen_w/1.6, screen_h/2-100, screen_w/6, screen_w/6)
            set5_rect = pygame.Rect(screen_w/1.24, screen_h/2-100, screen_w/6, screen_w/6)
            self.text('CHOOSE SKIN', screen_w/2, screen_h/7.2, 70, (255,255,255), 'comicsansms', 'center')
            self.text('normal car', set1_rect.x+set1_rect.w/2, set1_rect.y-20, 30, (255,255,255), 'comicsansms', 'center')
            self.text('truck', set2_rect.x+set2_rect.w/2, set2_rect.y-20, 30, (255,255,255), 'comicsansms', 'center')
            self.text('motorcycle', set3_rect.x+set3_rect.w/2, set3_rect.y-20, 30, (255,255,255), 'comicsansms', 'center')
            self.text('super car', set4_rect.x+set4_rect.w/2, set4_rect.y-20, 30, (255,255,255), 'comicsansms', 'center')
            self.text('dev surf', set5_rect.x+set5_rect.w/2, set5_rect.y-20, 30, (255,255,255), 'comicsansms', 'center')
            set1 = pygame.transform.scale(pygame.image.load('image/set1/set1.png'), (set1_rect.w, set1_rect.h))
            set2 = pygame.transform.scale(pygame.image.load('image/set2/set2.png'), (set2_rect.w, set2_rect.h))
            set3 = pygame.transform.scale(pygame.image.load('image/set3/set3.png'), (set3_rect.w, set3_rect.h))
            set4 = pygame.transform.scale(pygame.image.load('image/set4/set4.png'), (set4_rect.w, set4_rect.h))
            set5 = pygame.transform.scale(pygame.image.load('image/set5/set5.png'), (set5_rect.w, set5_rect.h))
            #Choice
            if set1_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(set1, [set1_rect.x, set1_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.skin = 'image/set1/'
                    self.skin_choice = True
            elif set2_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(set2, [set2_rect.x, set2_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.skin = 'image/set2/'
                    self.skin_choice = True
            elif set3_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(set3, [set3_rect.x, set3_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.skin = 'image/set3/'
                    self.skin_choice = True
            elif set4_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(set4, [set4_rect.x, set4_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.skin = 'image/set4/'
                    self.skin_choice = True
            elif set5_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(set5, [set5_rect.x, set5_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.skin = 'image/set5/'
                    self.skin_choice = True
            #Display
            self.screen.blit(set1, (set1_rect.x, set1_rect.y))        
            self.screen.blit(set2, (set2_rect.x, set2_rect.y))
            self.screen.blit(set3, (set3_rect.x, set3_rect.y))  
            self.screen.blit(set4, (set4_rect.x, set4_rect.y))
            self.screen.blit(set5, (set5_rect.x, set5_rect.y))
            
        def pick_car(self):
            click = pygame.mouse.get_pressed()
            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            #Button back
            btn_back = pygame.Rect(10,50,120,35)
            self.button(btn_back, 10, self.back)
            self.text('Back', btn_back.x+btn_back.w/2, btn_back.y+btn_back.h/2, 30, (255,255,255), 'algerian', 'center')
            #Display car_choice
            self.text('CHOOSE CAR', screen_w/2, screen_h/7.2, 70, (255,255,255), 'comicsansms', 'center')
            car1 = NewGame.car(self.screen, self.skin + 'car1.png', screen_w/29.5, screen_h/2-30)
            car2 = NewGame.car(self.screen, self.skin + 'car2.png', screen_w/4.4, screen_h/2-30)
            car3 = NewGame.car(self.screen, self.skin + 'car3.png', screen_w/2.4, screen_h/2-30)
            car4 = NewGame.car(self.screen, self.skin + 'car4.png', screen_w/1.6, screen_h/2-30)
            car5 = NewGame.car(self.screen, self.skin + 'car5.png', screen_w/1.24, screen_h/2-30)
            #Get car Rect
            car1_rect = pygame.Rect(car1.x, car1.y, car1.car_w, car1.car_h)
            car2_rect = pygame.Rect(car2.x, car1.y, car2.car_w, car2.car_h)
            car3_rect = pygame.Rect(car3.x, car3.y, car3.car_w, car3.car_h)
            car4_rect = pygame.Rect(car4.x, car4.y, car4.car_w, car4.car_h)
            car5_rect = pygame.Rect(car5.x, car5.y, car5.car_w, car5.car_h)
            #Choice
            if car1_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(car1.car, [car1_rect.x, car1_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.choice = 1
                    self.car_choice = True
            elif car2_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(car2.car, [car2_rect.x, car2_rect.y])    
                if click[0]:
                    pygame.event.wait()
                    self.choice = 2
                    self.car_choice = True
            elif car3_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(car3.car, [car3_rect.x, car3_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.choice = 3
                    self.car_choice = True
            elif car4_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(car4.car, [car4_rect.x, car4_rect.y])
                if click[0]:
                    pygame.event.wait()
                    self.choice = 4
                    self.car_choice = True
            elif car5_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(car5.car, [car5_rect.x, car5_rect.y])
                if click[0]:
                    self.choice = 5
                    self.car_choice = True
            #Display car
            car1.display(6.3, 7.5)  
            car2.display(6.3, 7.5)
            car3.display(6.3, 7.5)
            car4.display(6.3, 7.5)
            car5.display(6.3, 7.5)
            
        def pick_money(self):
            button_w = int(self.screen.get_width()/6.4)
            button_h = int(self.screen.get_height()/14.4)
            mid_w = self.screen.get_width()/2
            mid_h = self.screen.get_height()/2
            #Button back
            btn_back = pygame.Rect(10,50,120,35)
            self.button(btn_back, 10, self.back)
            self.text('Back', btn_back.x+btn_back.w/2, btn_back.y+btn_back.h/2, 30, (255,255,255), 'algerian', 'center')
            #Init button
            money1_rect = pygame.Rect(mid_w-button_w/2,mid_h/1.309,button_w,button_h)
            money2_rect = pygame.Rect(mid_w-button_w/2,mid_h/1.028,button_w,button_h)
            money3_rect = pygame.Rect(mid_w-button_w/2,mid_h/0.84,button_w,button_h)
            money4_rect = pygame.Rect(mid_w-button_w/2,mid_h/0.72,button_w,button_h)
            #Display
            self.text("LET'S BET", mid_w, mid_h/3.6, 70, (255,255,255), 'comicsansms', 'center')
            self.text('Your money: '+str(self.money)+'$', money1_rect.x+money1_rect.w/2, money1_rect.y-100, 50, (255,255,255), 'comicsansms', 'center') 
            money1 = pygame.transform.scale(pygame.image.load('image/5000.png'), (button_w,button_h))
            money2 = pygame.transform.scale(pygame.image.load('image/10000.png'), (button_w,button_h))
            money3 = pygame.transform.scale(pygame.image.load('image/50000.png'), (button_w,button_h))
            money4 = pygame.transform.scale(pygame.image.load('image/100000.png'), (button_w,button_h))

            if money1_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(money1, [money1_rect.x, money1_rect.y])
                if pygame.mouse.get_pressed()[0]:
                    if self.money < 5000:
                        self.error = True
                    else:
                        self.money_bet = 5000
                        self.money -= 5000
                        self.money_choice = True
            elif money2_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(money2, [money2_rect.x, money2_rect.y])
                if pygame.mouse.get_pressed()[0]:
                    if self.money < 10000:
                        self.error = True
                    else:
                        self.money_bet = 10000
                        self.money -= 10000
                        self.money_choice = True
            elif money3_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(money3, [money3_rect.x, money3_rect.y])
                if pygame.mouse.get_pressed()[0]:
                    if self.money < 50000:
                        self.error = True
                    else:
                        self.money_bet = 50000
                        self.money -= 50000
                        self.money_choice = True
            elif money4_rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_effect(money4, [money4_rect.x, money4_rect.y])
                if pygame.mouse.get_pressed()[0]:
                    if self.money < 100000:
                        self.error = True
                    else:
                        self.money_bet = 100000
                        self.money -= 100000
                        self.money_choice = True

            self.screen.blit(money1, (money1_rect.x, money1_rect.y))
            self.screen.blit(money2, (money2_rect.x, money2_rect.y))
            self.screen.blit(money3, (money3_rect.x, money3_rect.y))
            self.screen.blit(money4, (money4_rect.x, money4_rect.y))
            if self.error:
                self.text('not enough money', money1_rect.x+money1_rect.w/2, money1_rect.y-30, 30, (255,255,255), 'comicsansms', 'center')
                pygame.display.update()
                pygame.time.delay(1000)
                self.error = False
                

        def picking(self):
            self.screen.blit(pygame.transform.scale(self.bg, 
            (self.screen.get_width(), self.screen.get_height())), (0,0))
            if not self.road_choice:
                self.pick_road()
                pygame.event.wait()
            else:
                if not self.skin_choice:
                    self.pick_skin()
                    pygame.event.wait()
                else:
                    if not self.car_choice:
                        self.pick_car()
                        pygame.event.wait()
                    else:
                        if not self.money_choice:
                            self.pick_money()
                        else:
                            return True

        def back(self):
            self.mainmenu = True

    class racing:
        def __init__(self, screen, skin, choice, mode, username):
            #Screen
            self.screen = screen 
            screen_w = self.screen.get_width()    
            screen_h = self.screen.get_height() 
            self.mode = mode
            self.mainmenu = False
            self.playagain = False
            self.username = username
            #Display car randomly
            self.skin = skin
            car_y = [screen_h/5.625, screen_h/3.33 ,screen_h/2.33 ,screen_h/1.77 ,screen_h/1.42]
            choice_y = random.choice(car_y)
            self.car1 = NewGame.car(screen, self.skin + 'car1.png', 0, choice_y)
            car_y.remove(choice_y)
            choice_y = random.choice(car_y)
            self.car2 = NewGame.car(screen, self.skin + 'car2.png', 0, choice_y)
            car_y.remove(choice_y)
            choice_y = random.choice(car_y)
            self.car3 = NewGame.car(screen, self.skin + 'car3.png', 0, choice_y)
            car_y.remove(choice_y)
            choice_y = random.choice(car_y)
            self.car4 = NewGame.car(screen, self.skin + 'car4.png', 0, choice_y)
            car_y.remove(choice_y)
            choice_y = random.choice(car_y)
            self.car5 = NewGame.car(screen, self.skin + 'car5.png', 0, choice_y)
            car_y.remove(choice_y)       
            #Back ground
            self.road = NewGame.road(screen, self.mode)
            #Car choosed
            self.choice = choice
            if self.choice == 1:
                self.your_car = self.car1
            elif self.choice == 2:
                self.your_car = self.car2
            elif self.choice == 3:
                self.your_car = self.car3
            elif self.choice == 4:
                self.your_car = self.car4
            elif self.choice == 5:
                self.your_car = self.car5
            #Ranking
            self.rank = 1
            self.top1 = object
            self.top2 = object
            self.top3 = object
            self.finished = False
            #sound
            self.countdown = pygame.mixer.Sound('sound/countdown.mp3')
            self.engine = pygame.mixer.Sound('sound/engine.mp3')
            self.finish_sound = pygame.mixer.Sound('sound/finished.mp3')

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

        def item1(self, lane, car):
            if lane == 'lane1':
                x_item = self.road.item1_lane1
            elif lane == 'lane2':
                x_item = self.road.item1_lane2
            elif lane == 'lane3':
                x_item = self.road.item1_lane3
            elif lane == 'lane4':
                x_item = self.road.item1_lane4
            elif lane == 'lane5':
                x_item = self.road.item1_lane5
            x_car = car.x
            def random_item():
                random_item = car.random_item
                original_speed = car.original_speed
                if 1 <= random_item <= 10:
                    car.teleport()
                    if car.teleport_time == 20:
                        car.speed = original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item1_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item1_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item1_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item1_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item1_lane5 = 5000
                elif 11 <= random_item <= 20:
                    car.start_again()
                    if car.teleback_time == 20:
                        car.speed = original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item1_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item1_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item1_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item1_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item1_lane5 = 5000
                elif 21 <= random_item <= 40:
                    car.boost()
                    car.boost_time += 1
                    if car.boost_time == 100:
                        car.boost_time = 0
                        car.speed = car.original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item1_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item1_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item1_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item1_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item1_lane5 = 5000
                elif 41 <= random_item <= 60:
                    car.slow()
                    car.slow_time += 1
                    if car.slow_time == 200:
                        car.slow_time = 0
                        car.speed = car.original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item1_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item1_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item1_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item1_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item1_lane5 = 5000 
                elif 61 <= random_item <= 80:
                    car.stun()
                    car.stun_time += 1
                    if car.stun_time == 100:
                        car.stun_time = 0
                        car.speed = car.original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item1_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item1_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item1_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item1_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item1_lane5 = 5000 
                elif 81 <= random_item <= 100:
                    car.run_back() 
                    car.go_back += 1
                    car.car = pygame.transform.flip(car.car, True, False) 
            if x_car > x_item:
                random_item()
            if car.go_back > 0:
                car.go_back += 1
                if car.go_back == 100:
                    car.go_back = 0
                    car.speed = car.original_speed
                    car.car = pygame.transform.flip(car.car, True, False)
                    if True:
                        if lane == 'lane1':
                            self.road.item1_lane1 = 5000 
                        elif lane == 'lane2':
                            self.road.item1_lane2 = 5000
                        elif lane == 'lane3':
                            self.road.item1_lane3 = 5000
                        elif lane == 'lane4':
                            self.road.item1_lane4 = 5000
                        elif lane == 'lane5':
                            self.road.item1_lane5 = 5000

        def item2(self, lane, car):
            if lane == 'lane1':
                x_item = self.road.item2_lane1
            elif lane == 'lane2':
                x_item = self.road.item2_lane2
            elif lane == 'lane3':
                x_item = self.road.item2_lane3
            elif lane == 'lane4':
                x_item = self.road.item2_lane4
            elif lane == 'lane5':
                x_item = self.road.item2_lane5
            x_car = car.x
            def random_item():
                random_item = car.random_item
                original_speed = car.original_speed
                if 1 <= random_item <= 10:
                    car.teleport()
                    if True:
                        if lane == 'lane1':
                            self.road.item2_lane1 = 5000 
                        elif lane == 'lane2':
                            self.road.item2_lane2 = 5000
                        elif lane == 'lane3':
                            self.road.item2_lane3 = 5000
                        elif lane == 'lane4':
                            self.road.item2_lane4 = 5000
                        elif lane == 'lane5':
                            self.road.item2_lane5 = 5000
                elif 11 <= random_item <= 20:
                    car.start_again()
                    if True:
                        if lane == 'lane1':
                            self.road.item2_lane1 = 5000 
                        elif lane == 'lane2':
                            self.road.item2_lane2 = 5000
                        elif lane == 'lane3':
                            self.road.item2_lane3 = 5000
                        elif lane == 'lane4':
                            self.road.item2_lane4 = 5000
                        elif lane == 'lane5':
                            self.road.item2_lane5 = 5000
                elif 21 <= random_item <= 40:
                    car.boost()
                    if x_car > x_item + 200:
                        car.speed = original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item2_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item2_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item2_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item2_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item2_lane5 = 5000 
                elif 41 <= random_item <= 60:
                    car.slow()
                    if x_car > x_item + 200:
                        car.speed = original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item2_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item2_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item2_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item2_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item2_lane5 = 5000 
                elif 61 <= random_item <= 80:
                    car.stun()
                    car.stun_time += 1
                    if car.stun_time == 100:
                        car.stun_time = 0
                        car.speed = car.original_speed
                        if True:
                            if lane == 'lane1':
                                self.road.item2_lane1 = 5000 
                            elif lane == 'lane2':
                                self.road.item2_lane2 = 5000
                            elif lane == 'lane3':
                                self.road.item2_lane3 = 5000
                            elif lane == 'lane4':
                                self.road.item2_lane4 = 5000
                            elif lane == 'lane5':
                                self.road.item2_lane5 = 5000 
                elif 81 <= random_item <= 100:
                    car.run_back() 
                    car.go_back += 1
                    car.car = pygame.transform.flip(car.car, True, False)
            if x_car > x_item:
                random_item()
            if car.go_back > 0:
                car.go_back += 1
                if car.go_back == 100:
                    car.go_back = 0
                    car.speed = car.original_speed
                    car.car = pygame.transform.flip(car.car, True, False)
                    if True:
                        if lane == 'lane1':
                            self.road.item2_lane1 = 5000 
                        elif lane == 'lane2':
                            self.road.item2_lane2 = 5000
                        elif lane == 'lane3':
                            self.road.item2_lane3 = 5000
                        elif lane == 'lane4':
                            self.road.item2_lane4 = 5000
                        elif lane == 'lane5':
                            self.road.item2_lane5 = 5000
                        
        def start_effect(self):
            self.road.display()
            self.car1.display()
            self.car2.display()
            self.car3.display()
            self.car4.display()
            self.car5.display()
            self.countdown.play()
            self.text('3',self.screen.get_width()/2, self.screen.get_height()/2, 300, (0,0,0), 'comicsansms', 'center')
            red_light = pygame.image.load('image/redlight.png')
            self.screen.blit(pygame.transform.scale(red_light, 
            (int(self.screen.get_width()/3.8), int(self.screen.get_height()/5.2))), (self.screen.get_width()/2.7, self.screen.get_height()/6.35))
            pygame.display.update()
            pygame.time.delay(1000)
            self.road.display()
            self.car1.display()
            self.car2.display()
            self.car3.display()
            self.car4.display()
            self.car5.display()
            self.text('2',self.screen.get_width()/2, self.screen.get_height()/2, 300, (0,0,0), 'comicsansms', 'center')
            yellow_light = pygame.image.load('image/yellowlight.png')
            self.screen.blit(pygame.transform.scale(yellow_light, (int(self.screen.get_width()/3.8), int(self.screen.get_height()/5.2))),
             (self.screen.get_width()/2.7, self.screen.get_height()/6.35))
            pygame.display.update()
            pygame.time.delay(1000)
            self.road.display()
            self.car1.display()
            self.car2.display()
            self.car3.display()
            self.car4.display()
            self.car5.display()
            self.text('1',self.screen.get_width()/2, self.screen.get_height()/2, 300, (0,0,0), 'comicsansms', 'center')
            green_light = pygame.image.load('image/greenlight.png')
            self.screen.blit(pygame.transform.scale(green_light, 
            (int(self.screen.get_width()/3.8), int(self.screen.get_height()/5.2))), (self.screen.get_width()/2.7, self.screen.get_height()/6.35))
            pygame.display.update()
            pygame.time.delay(1000)
                         
        def start(self): 
            self.countdown.stop()  
            self.engine.set_volume(0.3)
            self.engine.play()
            if self.mode == 'long':
                self.road.display()
                self.car1.run()
                self.car2.run()
                self.car3.run()
                self.car4.run()
                self.car5.run()
                if self.choice != 1:
                    self.text('bot 1', self.car1.x+20, self.car1.y-20, 25, (0,0,0))
                if self.choice != 2:
                    self.text('bot 2', self.car2.x+20, self.car2.y-20, 25, (0,0,0))
                if self.choice != 3:
                    self.text('bot 3', self.car3.x+20, self.car3.y-20, 25, (0,0,0))
                if self.choice != 4:
                    self.text('bot 4', self.car4.x+20, self.car4.y-20, 25, (0,0,0))
                if self.choice != 5:
                    self.text('bot 5', self.car5.x+20, self.car5.y-20, 25, (0,0,0))
                self.text(self.username, self.your_car.x+20, self.your_car.y-20, 25, (0,0,0))
                self.item1('lane1', self.car1)
                self.item1('lane2', self.car2)
                self.item1('lane3', self.car3)
                self.item1('lane4', self.car4)
                self.item1('lane5', self.car5)
            elif self.mode == 'short':
                self.road.display()
                self.car1.run()
                self.car2.run()
                self.car3.run()
                self.car4.run()
                self.car5.run()
                if self.choice != 1:
                    self.text('bot 1', self.car1.x+20, self.car1.y-20, 25, (0,0,0))
                if self.choice != 2:
                    self.text('bot 2', self.car2.x+20, self.car2.y-20, 25, (0,0,0))
                if self.choice != 3:
                    self.text('bot 3', self.car3.x+20, self.car3.y-20, 25, (0,0,0))
                if self.choice != 4:
                    self.text('bot 4', self.car4.x+20, self.car4.y-20, 25, (0,0,0))
                if self.choice != 5:
                    self.text('bot 5', self.car5.x+20, self.car5.y-20, 25, (0,0,0))
                self.text(self.username, self.your_car.x+20, self.your_car.y-20, 25, (0,0,0))
                self.item1('lane1', self.car1)
                self.item1('lane2', self.car2)
                self.item1('lane3', self.car3)
                self.item1('lane4', self.car4)
                self.item1('lane5', self.car5)
                         
            if self.car1.finished(self.rank):
                self.rank += 1
            elif self.car2.finished(self.rank):
                self.rank += 1
            elif self.car3.finished(self.rank):
                self.rank += 1
            elif self.car4.finished(self.rank):
                self.rank += 1
            elif self.car5.finished(self.rank):
                self.rank += 1
            if self.rank == 6:
                self.ranking()

        def ranking(self):  
            #Top 1
            if self.car1.rank == 1:
                self.top1 = self.car1
            elif self.car2.rank == 1:
                self.top1 = self.car2
            elif self.car3.rank == 1:
                self.top1 = self.car3
            elif self.car4.rank == 1:
                self.top1 = self.car4
            elif self.car5.rank == 1:
                self.top1 = self.car5
            #Top 2
            if self.car1.rank == 2:
                self.top2 = self.car1
            elif self.car2.rank == 2:
                self.top2 = self.car2
            elif self.car3.rank == 2:
                self.top2 = self.car3
            elif self.car4.rank == 2:
                self.top2 = self.car4
            elif self.car5.rank == 2:
                self.top2 = self.car5
            #Top 3
            if self.car1.rank == 3:
                self.top3 = self.car1
            elif self.car2.rank == 3:
                self.top3 = self.car2
            elif self.car3.rank == 3:
                self.top3 = self.car3
            elif self.car4.rank == 3:
                self.top3 = self.car4
            elif self.car5.rank == 3:
                self.top3 = self.car5
            #Finished
            self.finished = True

        def finished_effect(self):
            self.engine.stop()
            self.finish_sound.set_volume(0.1)
            self.finish_sound.play()
            screen_w = self.screen.get_width()
            screen_h = self.screen.get_height()
            
            self.top1.x = screen_w/2.4
            self.top1.y = screen_h/2
            self.top2.x = screen_w/4.085
            self.top2.y = screen_h/1.68
            self.top3.x = screen_w/1.7
            self.top3.y = screen_h/1.5
            btn_playagain = pygame.Rect(screen_w/2.37, screen_h/4.7, screen_w/6.4, screen_h/15.43)
            btn_mainmenu = pygame.Rect(screen_w/2.23, screen_h/3.36, screen_w/9.6, screen_h/21.6)
            firework = pygame.image.load('image/firework.png')
            ray = pygame.image.load('image/ray.png')
            for y in range(self.screen.get_height(),100,-10):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                self.screen.blit(pygame.transform.scale(self.road.road_finished, 
                (self.screen.get_width(), self.screen.get_height())), (0, 0))
                self.top1.display(6, 7.2)
                self.top2.display(6, 7.2)
                self.top3.display(6, 7.2)
                self.screen.blit(ray, (self.screen.get_width()/2, y))
                self.text(self.username+"'s rank: "+str(self.your_car.rank), screen_w/2, 100, 40, (255,255,255), 'comicsansms', 'center')
                self.button(btn_playagain, 40, self.play_again)
                self.text("Play again", btn_playagain.x+btn_playagain.w/2, btn_playagain.y+btn_playagain.h/2, 37, (255,255,255), 'comicsansms', 'center')
                self.button(btn_mainmenu, 40, self.back)
                self.text("Main menu", btn_mainmenu.x+btn_mainmenu.w/2, btn_mainmenu.y+btn_mainmenu.h/2, 25, (255,255,255), 'comicsansms', 'center')
                pygame.display.update()
                if self.playagain or self.mainmenu:
                    break
            for x in range(25):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                self.screen.blit(pygame.transform.scale(self.road.road_finished, 
                (self.screen.get_width(), self.screen.get_height())), (0, 0))
                self.top1.display(6, 7.2)
                self.top2.display(6, 7.2)
                self.top3.display(6, 7.2)
                self.screen.blit(pygame.transform.scale(firework, 
                (self.screen.get_width(), self.screen.get_height())), (0, 0))
                self.text(self.username+"'s rank: "+str(self.your_car.rank), screen_w/2, 100, 40, (255,255,255), 'comicsansms', 'center')
                self.button(btn_playagain, 40, self.play_again)
                self.text("Play again", btn_playagain.x+btn_playagain.w/2, btn_playagain.y+btn_playagain.h/2, 37, (255,255,255), 'comicsansms', 'center')
                self.button(btn_mainmenu, 40, self.back)
                self.text("Main menu", btn_mainmenu.x+btn_mainmenu.w/2, btn_mainmenu.y+btn_mainmenu.h/2, 25, (255,255,255), 'comicsansms', 'center')
                pygame.display.update()
                if self.playagain or self.mainmenu:
                    break

        def play_again(self):
            self.finish_sound.stop()
            self.playagain = True
        def back(self):
            self.finish_sound.stop()
            self.mainmenu = True
            
    class after_racing:
        def __init__(self, money, money_bet, rank):
            self.money = money
            self.money_bet = money_bet
            self.rank = rank
        def update_data(self):
            if self.rank == 1:
                self.money += 2*self.money_bet 
            elif self.rank == 2:
                self.money += int(self.money_bet/2)


    



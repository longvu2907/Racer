from minigame import XO
from data import userdata
import pygame
from datetime import datetime


class mini_game:
    def __init__(self, screen, username):
        self.screen = screen
        self.data = userdata()
        self.username = username
        self.userdata = self.data.get(username)
        self.money = self.userdata['money']
        self.now = datetime.now()

    def start(self):
        pygame.event.wait()
        game = XO.game(self.screen, self.money)
        game.main()
        self.data.update(self.userdata['name'], self.userdata['password'], game.money, self.userdata['items'])
        result = game.money - self.money
        if result > 0:
            sign = '+'
        else:
            sign = ''
        history_data = self.now.strftime("%d/%m/%Y(%H:%M:%S): ") + "Play mini game " + sign + str(result) + '$' + ' -> ' + str(game.money) + '$'
        self.data.update_history(self.username, history_data)
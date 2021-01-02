import pygame
from pygame.locals import *


# Create the constants (go ahead and experiment with different values)
BOARDWIDTH = 3  # number of columns in the board
BOARDHEIGHT = 3 # number of rows in the board
TILESIZE = 100


FPS = 30
BLANK = None

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

BLANK = 10
PLAYER_O = 11
PLAYER_X = 21


PLAYER_O_WIN = PLAYER_O * 3
PLAYER_X_WIN = PLAYER_X * 3

CONT_GAME         = 10
DRAW_GAME         = 20
QUIT_GAME         = 30



choice = 0

class game:
    def __init__(self, screen, money):
        self.money = money
        self.screen = screen
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        self.XMARGIN = int((self.w - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
        self.YMARGIN = int((self.h - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

    def check_win_game(self, board):
        def check_draw_game():
            return sum(board)%10 == 9

        def check_horizontal(player):
            for i in [0, 3, 6]:
                if sum(board[i:i+3]) == 3 * player:
                    return player

        def check_vertical(player):
            for i in range(3):
                if sum(board[i::3]) == 3 * player:
                    return player

        def check_diagonals(player):
            if (sum(board[0::4]) == 3 * player) or (sum(board[2:7:2]) == 3 * player):
                return player

        for player in [PLAYER_X, PLAYER_O]:
            if any([check_horizontal(player), check_vertical(player), check_diagonals(player)]):
                return player

        return DRAW_GAME if check_draw_game() else CONT_GAME


    def unit_score(self, winner, depth):
        if winner == DRAW_GAME:
            return 0
        else:
            return 10 - depth if winner == PLAYER_X else depth - 10


    def get_available_step(self, board):
        return [i for i in range(9) if board[i] == BLANK]


    def minmax(self, board, depth):
        global choice
        result = self.check_win_game(board)
        if result != CONT_GAME:
            return self.unit_score(result, depth)

        depth += 1
        scores = []
        steps = []

        for step in self.get_available_step(board):
            score = self.minmax(self.update_state(board, step, depth), depth)
            scores.append(score)
            steps.append(step)

        if depth % 2 == 1:
            max_value_index = scores.index(max(scores))
            choice = steps[max_value_index]
            return max(scores)
        else:
            min_value_index = scores.index(min(scores))
            choice = steps[min_value_index]
            return min(scores)


    def update_state(self, board, step, depth):
        board = list(board)
        board[step] = PLAYER_X if depth % 2 else PLAYER_O
        return board


    def update_board(self, board, step, player):
        board[step] = player


    def change_to_player(self, player):
        if player == PLAYER_O:
            return 'O'
        elif player == PLAYER_X:
            return 'X'
        elif player == BLANK:
            return '-'


    def drawBoard(self, board, message, money):
        self.screen.fill(BGCOLOR)
        if message:
            textSurf, textRect = self.makeText(message, MESSAGECOLOR, BGCOLOR, self.w/2-30, 5)
            textSurf1, textRect1 = self.makeText(money, MESSAGECOLOR, BGCOLOR, self.w-300, 5)
            self.screen.blit(textSurf, textRect)
            self.screen.blit(textSurf1, textRect1)

        for tilex in range(3):
            for tiley in range(3):
                if board[tilex*3+tiley] != BLANK:
                    self.drawTile(tilex, tiley, board[tilex*3+tiley])

        left, top = self.getLeftTopOfTile(0, 0)
        width = BOARDWIDTH * TILESIZE
        height = BOARDHEIGHT * TILESIZE
        pygame.draw.rect(self.screen, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

        self.screen.blit(NEW_SURF, NEW_RECT)
        self.screen.blit(NEW_SURF2, NEW_RECT2)


    def getLeftTopOfTile(self, tileX, tileY):
        left = self.XMARGIN + (tileX * TILESIZE) + (tileX - 1)
        top = self.YMARGIN + (tileY * TILESIZE) + (tileY - 1)
        return (left, top)


    def makeText(self, text, color, bgcolor, top, left):
        '''Create the Surface and Rect objects for some text.'''
        textSurf = BASICFONT.render(text, True, color, bgcolor)
        textRect = textSurf.get_rect()
        textRect.topleft = (top, left)
        return (textSurf, textRect)


    def drawTile(self, tilex, tiley, symbol, adjx=0, adjy=0):
        '''
        Draw a tile at board coordinates tilex and tiley, optionally a few
        pixels over (determined by adjx and adjy).
        '''
        left, top = self.getLeftTopOfTile(tilex, tiley)
        pygame.draw.rect(self.screen, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))
        textSurf = BASICFONT.render(self.symbol_to_str(symbol), True, TEXTCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
        self.screen.blit(textSurf, textRect)

    def symbol_to_str(self, symbol):
        if symbol == PLAYER_O:
            return 'O'
        elif symbol == PLAYER_X:
            return 'X'


    def getSpotClicked(self, x, y):
        '''From the x & y pixel coordinates, get the x & y board coordinates.'''
        for tileX in range(3):
            for tileY in range(3):
                left, top = self.getLeftTopOfTile(tileX, tileY)
                tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
                if tileRect.collidepoint(x, y):
                    return (tileX, tileY)
        return None


    def board_to_step(self, spotx, spoty):
        return spotx * 3 + spoty


    def check_move_legal(self, coords, board):
        step = self.board_to_step(*coords)
        return board[step] == BLANK

    def main(self):
        global FPSCLOCK, BASICFONT, NEW_SURF, NEW_RECT, NEW_SURF2, NEW_RECT2
        two_player = False #by default false
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
        NEW_SURF, NEW_RECT = self.makeText('QUIT', TEXTCOLOR, TILECOLOR, self.w/2 + 100, 550)
        NEW_SURF2, NEW_RECT2 = self.makeText('PLAY AGAIN', TEXTCOLOR, TILECOLOR, self.w/2-75, 550)
        board = [BLANK] * 9
        game_over = False
        x_turn = True
        msg = "CARO"
        your_money = self.money
        money = "Your money: " + str(your_money) + " $"
        self.drawBoard(board, msg, money)
        pygame.display.update()
        running = True
        while running:
            your_money = self.money
            money = "Your money: " + str(your_money) + " $"
            coords = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == MOUSEBUTTONUP:
                    coords = self.getSpotClicked(event.pos[0], event.pos[1])
                    if not coords and NEW_RECT.collidepoint(event.pos):
                        running = False
                    if not coords and NEW_RECT2.collidepoint(event.pos):
                        board = [BLANK] * 9
                        game_over = False
                        msg = "CARO"
                        self.drawBoard(board, msg, money)
                        pygame.display.update()
            if coords and self.check_move_legal(coords, board) and not game_over:

                next_step = self.board_to_step(*coords)
                self.update_board(board, next_step, PLAYER_X)
                self.drawBoard(board, msg, money)
                pygame.display.update()
                self.minmax(board, 0)
                self.update_board(board, choice, PLAYER_O)

                result = self.check_win_game(board)
                game_over = (result != CONT_GAME)

                if result == PLAYER_X:
                    msg = "YOU WIN!"
                    self.money += 20000
                elif result == PLAYER_O:
                    msg = "YOU LOSE!"

                elif result == DRAW_GAME:
                    msg = "Draw game"
                    self.money += 1000
                self.drawBoard(board, msg, money)
                pygame.display.update()




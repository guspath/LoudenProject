import pygame

# C
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 215, 0)
C_L_BLUE = (0, 255, 255)
C_L_GRAY = (230, 230, 230)
C_BLUEE = (0, 180, 255)
C_L_RED = (220, 50, 0)
C_ORANGEE = (255, 165, 0)
C_ORANGE = (242, 128, 13)
C_LEMON = (0, 240, 0)
# E
E_ENEMY = pygame.USEREVENT + 1


E_SPEED = {
    'Level1bg0': 0,
    'Level1bg1': 1,
    'Level1bg2': 2,
    'Level1bg3': 3,
    'Level1bg4': 4,
    'Level1bg5': 5,
    'Level1bg6': 6,
    'Level2bg0': 0,
    'Level2bg1': 1,
    'Level2bg2': 2,
    'Level2bg3': 3,
    'Level2bg4': 4,
    'Level2bg5': 5,
    'Player1'  : 3,
    'Player2'  : 3,
    'Enemy1'   : 2,
    'Enemy2'   : 2,
    'Player1Shot': 1,
    'Player2Shot': 3,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3,
}

E_HEALTH = {
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Level1bg3': 999,
    'Level1bg4': 999,
    'Level1bg5': 999,
    'Level1bg6': 999,
    'Level2bg0': 999,
    'Level2bg1': 999,
    'Level2bg2': 999,
    'Level2bg3': 999,
    'Level2bg4': 999,
    'Level2bg5': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

E_S_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 45,
    'Enemy2': 60,
}

E_DMG = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level1bg5': 0,
    'Level1bg6': 0,
    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Level2bg4': 0,
    'Level2bg5': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

E_SCORE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level1bg5': 0,
    'Level1bg6': 0,
    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Level2bg4': 0,
    'Level2bg5': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

# O
OPTIONS_MENU = ('1P - SOLO GAME',
                '2P - PLAYER VS PLAYER',
                'SCORE',
                'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
S_TIME = 3500

#T
TO_E = pygame.USEREVENT + 2
TO_D = 100
TO_L = 15000

# W
W_WIDTH = 600
W_HEIGHT = 480

#P
POS_S = {'Title': (W_WIDTH / 2, 50),
             'EnterName': (W_WIDTH / 2, 80),
             'Label': (W_WIDTH / 2, 90),
             'Name': (W_WIDTH / 2, 110),
             0: (W_WIDTH / 2, 110),
             1: (W_WIDTH / 2, 130),
             2: (W_WIDTH / 2, 150),
             3: (W_WIDTH / 2, 170),
             4: (W_WIDTH / 2, 190),
             5: (W_WIDTH / 2, 210),
             6: (W_WIDTH / 2, 230),
             7: (W_WIDTH / 2, 250),
             8: (W_WIDTH / 2, 270),
             9: (W_WIDTH / 2, 290),
             }
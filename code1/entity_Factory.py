import random

from code1.background import Background
from code1.const import W_WIDTH, W_HEIGHT
from code1.enemy import Enemy
from code1.player import Player


class EntityFactory:


    @staticmethod
    def g_entity(entity_n: str):
        match entity_n:
            case 'Level1bg':
                bg_l = []
                for i in range (7):
                    bg_l.append(Background(f'Level1bg{i}', (0,0)))
                    bg_l.append(Background(f'Level1bg{i}', (W_WIDTH, 0)))
                return bg_l
            case 'Player1':
                return Player('Player1', (-10, W_HEIGHT - 92))
            case 'Player2':
                return Player('Player2', (3, W_HEIGHT - 165))
            case 'Enemy1':
                return Enemy('Enemy1', (W_WIDTH + 10, random.randint(W_HEIGHT - 150, W_HEIGHT - 70)))
            case 'Enemy2':
                return Enemy('Enemy2', (W_WIDTH + 10, random.randint(W_HEIGHT - 150, W_HEIGHT - 70)))

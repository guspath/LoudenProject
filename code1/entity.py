from abc import ABC, abstractmethod

import pygame.image

from code1.const import E_HEALTH, E_DMG, E_SCORE


class Entity1(ABC):

    def __init__(self, name:str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.e_speed = 0
        self.health = E_HEALTH[self.name]
        self.dmg = E_DMG[self.name]
        self.score = E_SCORE[self.name]
        self.l_dmg = 'None'
    @abstractmethod
    def move(self):
        pass


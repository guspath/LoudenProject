from abc import ABC, abstractmethod

import pygame.image

from code1.const import E_HEALTH


class Entity1(ABC):

    def __init__(self, name:str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.e_speed = 0
        self.health = E_HEALTH[self.name]
    @abstractmethod
    def move(self):
        pass
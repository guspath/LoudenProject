from abc import ABC, abstractmethod

import pygame.image


class Entity1(ABC):

    def __init__(self, name:str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.e_speed = 0
    @abstractmethod
    def move(self):
        pass
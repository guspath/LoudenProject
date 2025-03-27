import pygame.key

from code1.const import E_SPEED, W_WIDTH, W_HEIGHT, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP, \
    PLAYER_KEY_SHOT, E_S_DELAY
from code1.entity import Entity1
from code1.playerShot import PlayerShot


class Player(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.s_delay = E_S_DELAY[self.name]

    def update(self):
        pass

    def move(self):
        key_p = pygame.key.get_pressed()
        if key_p[PLAYER_KEY_UP[self.name]] and self.rect.top > 330:
            self.rect.centery -= E_SPEED[self.name]
        if key_p[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < W_HEIGHT - 10:
            self.rect.centery += E_SPEED[self.name]
        if key_p[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= E_SPEED[self.name]
        if key_p[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < W_WIDTH:
            self.rect.centerx += E_SPEED[self.name]

        pass

    def shot(self):
        self.s_delay -= 1
        if self.s_delay == 0:
            self.s_delay = E_S_DELAY[self.name]
            p_key = pygame.key.get_pressed()
            if p_key[PLAYER_KEY_SHOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

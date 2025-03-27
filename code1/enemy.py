from code1.const import W_WIDTH, E_SPEED, E_S_DELAY
from code1.enemyShot import EnemyShot
from code1.entity import Entity1


class Enemy(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.s_delay = E_S_DELAY[self.name]

    def move(self):
        self.rect.centerx -= E_SPEED[self.name]

    def shot(self):
        self.s_delay -= 1
        if self.s_delay == 0:
            self.s_delay = E_S_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

from code1.const import W_WIDTH, E_SPEED
from code1.entity import Entity1


class Enemy(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= E_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = W_WIDTH

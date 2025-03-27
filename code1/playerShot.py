from code1.const import E_SPEED
from code1.entity import Entity1


class PlayerShot(Entity1):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += E_SPEED[self.name]


from code1.entity import Entity1

class Player(Entity1):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)

    def update(self):
        pass

    def move(self):
        pass
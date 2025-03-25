from code1.entity import Entity1
from code1.entity_Factory import EntityFactory


class Level:
    def __init__(self, window, name, g_mode):
        self.window = window
        self.name = name
        self.g_mode = g_mode
        self.e_list: list[Entity1] = []
        self.e_list.extend(EntityFactory.g_entity('Level1bg'))


    def run(self):
        while True:
            for e in self.e_list:
                self.window.blit()
        pass
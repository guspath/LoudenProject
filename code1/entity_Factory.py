from code1.background import Background
from code1.const import W_WIDTH


class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def g_entity(entity_n: str):
        match entity_n:
            case 'Level1bg':
                bg_l = []
                for i in range (7):
                    bg_l.append(Background(f'Level1bg{i}', (0,0)))
                    bg_l.append(Background(f'Level1bg{i}', (W_WIDTH, 0)))
                return bg_l
from code1.background import Background


class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def g_entity(entity_n: str):
        match entity_n:
            case 'Level1bg':
                bg_l = []
                for i in range (8):
                    bg_l.append(Background(f'Level1bg{i}', (0,0)))
                return bg_l
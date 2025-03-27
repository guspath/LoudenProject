from code1.enemy import Enemy
from code1.entity import Entity1


class EntityMediator:

    @staticmethod
    def __v_c_window(e: Entity1):
        if isinstance(e, Enemy):
            if e.rect.right < 0:
                e.health = 0



    @staticmethod
    def v_collisions(e_list: list[Entity1]):
        for i in range(len(e_list)):
            t_entity = e_list[i]
            EntityMediator.__v_c_window(t_entity)

    @staticmethod
    def v_health(e_list: list[Entity1]):
        for e in e_list:
            if e.health <= 0:
                e_list.remove(e)
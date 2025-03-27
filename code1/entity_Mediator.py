from code1.const import W_WIDTH
from code1.enemy import Enemy
from code1.enemyShot import EnemyShot
from code1.entity import Entity1
from code1.player import Player
from code1.playerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __v_c_window(e: Entity1):
        if isinstance(e, Enemy):
            if e.rect.right <= 0:
                e.health = 0
        if isinstance(e, PlayerShot):
            if e.rect.left >= W_WIDTH:
                e.health = 0
        if isinstance(e, EnemyShot):
            if e.rect.right <= 0:
                e.health = 0



    @staticmethod
    def v_c_ent(e1, e2):
        v_int = False
        if isinstance(e1, Enemy) and isinstance(e2, PlayerShot):
            v_int = True
        elif isinstance(e1, PlayerShot) and isinstance(e2, Enemy):
            v_int = True
        elif isinstance(e1, Player) and isinstance(e2, EnemyShot):
            v_int = True
        elif isinstance(e1, EnemyShot) and isinstance(e2, Player):
            v_int = True

        if v_int:
            if (e1.rect.right >= e2.rect.left and
                    e1.rect.left <= e2.rect.right and
                    e1.rect.bottom >= e2.rect.top and
                    e1.rect.top <= e2.rect.bottom):
                e1.health -= e2.dmg
                e2.health -= e1.dmg
                e1.l_dmg = e2.name
                e2.l_dmg = e1.name

    @staticmethod
    def __score(enemy: Enemy, e_list: list[Entity1]):
        if enemy.l_dmg == 'Player1Shot':
            for e in e_list:
                if e.name == 'Player1':
                    e.score += enemy.score
        elif enemy.l_dmg == 'Player2Shot':
            for e in e_list:
                if e.name == 'Player2':
                    e.score += enemy.score



    @staticmethod
    def v_collisions(e_list: list[Entity1]):
        for i in range(len(e_list)):
            t_entity1 = e_list[i]
            EntityMediator.__v_c_window(t_entity1)
            for o in range(i+1, len(e_list)):
                t_entity2 = e_list[o]
                EntityMediator.v_c_ent(t_entity1, t_entity2)

    @staticmethod
    def v_health(e_list: list[Entity1]):
        for e in e_list:
            if e.health <= 0:
                if isinstance(e, Enemy):
                    EntityMediator.__score(e, e_list)
                e_list.remove(e)
import random
import sys

import pygame
from pygame import Surface

from pygame.font import Font

from code1.const import C_WHITE, W_HEIGHT, W_WIDTH, OPTIONS_MENU, E_ENEMY, S_TIME, C_BLUEE, C_LEMON, C_L_RED, \
    TO_E, TO_D, TO_L
from code1.enemy import Enemy
from code1.entity import Entity1
from code1.entity_Factory import EntityFactory
from code1.entity_Mediator import EntityMediator
from code1.player import Player


class Level:
    def __init__(self, window, name, g_mode):
        self.timeout = TO_L
        self.window = window
        self.name = name
        self.g_mode = g_mode
        self.e_list: list[Entity1] = []
        self.e_list.extend(EntityFactory.g_entity(self.name + 'bg'))
        self.e_list.append(EntityFactory.g_entity('Player1'))
        if g_mode in [OPTIONS_MENU[1]]:
            self.e_list.append(EntityFactory.g_entity('Player2'))
        pygame.time.set_timer(E_ENEMY, S_TIME)
        pygame.time.set_timer(TO_E, TO_D)



    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        frames = pygame.time.Clock()
        while True:
            frames.tick(60)
            for e in self.e_list:
                self.window.blit(source=e.surf, dest=e.rect)
                e.move()
                if isinstance(e, (Player, Enemy)):
                    shot = e.shot()
                    if shot is not None:
                        self.e_list.append(shot)
                if e.name == 'Player1':
                    self.text_lvl(20, f'Player1 - HP: {e.health} | Score: {e.score}', C_BLUEE, (87, 25))
                if e.name == 'Player2':
                    self.text_lvl(20, f'Player2 - HP: {e.health} | Score: {e.score}', C_L_RED, (83, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == E_ENEMY:
                    r_enemy = random.choice(('Enemy1', 'Enemy2'))
                    self.e_list.append(EntityFactory.g_entity(r_enemy))
                if event.type == TO_E:
                    self.timeout -= TO_D
                    if self.timeout == 0:
                        return True

            # screen texts
            self.text_lvl(17, f'{self.name} - Remaining Time: {self.timeout / 1000:.1f}s', C_WHITE, (W_WIDTH - 90, W_HEIGHT - 8))
            self.text_lvl(17, f'FPS: {frames.get_fps():.0f}', C_WHITE, (21, W_HEIGHT - 8))
            self.text_lvl(17, f'Entitys: {len(self.e_list)}', C_WHITE, (80, W_HEIGHT - 8))
            pygame.display.flip()

            # checking collisions/health
            EntityMediator.v_collisions(e_list=self.e_list)
            EntityMediator.v_health(e_list=self.e_list)





    def text_lvl(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Open Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
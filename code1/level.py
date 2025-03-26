import random
import sys

import pygame
from pygame import Surface

from pygame.font import Font

from code1.const import C_WHITE, W_HEIGHT, W_WIDTH, OPTIONS_MENU, E_ENEMY, S_TIME
from code1.entity import Entity1
from code1.entity_Factory import EntityFactory


class Level:
    def __init__(self, window, name, g_mode):
        self.timeout = 15000 #15 seconds
        self.window = window
        self.name = name
        self.g_mode = g_mode
        self.e_list: list[Entity1] = []
        self.e_list.extend(EntityFactory.g_entity('Level1bg'))
        self.e_list.append(EntityFactory.g_entity('Player1'))
        if g_mode in [OPTIONS_MENU[1]]:
            self.e_list.append(EntityFactory.g_entity('Player2'))
        pygame.time.set_timer(E_ENEMY, S_TIME)



    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        frames = pygame.time.Clock()
        while True:
            frames.tick(60)
            for e in self.e_list:
                self.window.blit(source=e.surf, dest=e.rect)
                e.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == E_ENEMY:
                    r_enemy = random.choice(('Enemy1', 'Enemy2'))
                    self.e_list.append(EntityFactory.g_entity(r_enemy))


            # screen texts
            self.text_lvl(17, f'{self.name} - Remaining Time: {self.timeout / 1000:.1f}s', C_WHITE, (W_WIDTH - 90, W_HEIGHT - 8))
            self.text_lvl(17, f'FPS: {frames.get_fps():.0f}', C_WHITE, (21, W_HEIGHT - 8))
            self.text_lvl(17, f'Entitys: {len(self.e_list)}', C_WHITE, (80, W_HEIGHT - 8))
            pygame.display.flip()
        pass




    def text_lvl(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Open Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
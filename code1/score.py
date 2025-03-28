import sys
from datetime import datetime
from idlelib.debugger_r import IdbProxy

import pygame
from pygame import Surface, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code1 import dbProxy
from code1.const import C_LEMON, POS_S, OPTIONS_MENU, C_WHITE, C_YELLOW
from code1.dbProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/scorebg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_s(self, g_mode: str, s: list[int]):
        pygame.mixer_music.load('./asset/score.mp3')
        pygame.mixer_music.play(-1)
        db_p = DBProxy('DB_S')
        n = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_t(60, 'YOU WON!', C_YELLOW, POS_S['Title'])
            if g_mode == OPTIONS_MENU[0]:
                p_s = s[0]
                t = 'Player, please enter your name(6 characters):'
            if g_mode == OPTIONS_MENU[1]:
                if s[0] >= s[1]:
                    p_s = s[0]
                    t = 'Player1, please enter your name(6 characters):'
                else:
                    p_s = s[1]
                    t = 'Player 2, please enter your name(6 characters):'
            self.score_t(30, t, C_WHITE, POS_S['EnterName'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(n) == 6:
                        db_p.save_db({'name': n, 'score': p_s, 'date': get_formatted_date()})
                        self.show_s()
                        return
                    elif event.key == K_BACKSPACE:
                        n = n[:-1]
                    else:
                        if len(n) < 6:
                            n += event.unicode
            self.score_t(30, n, C_YELLOW, POS_S['Name'])
            pygame.display.flip()
            pass

    def show_s(self):
        pygame.mixer_music.load('./asset/score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_t(48, 'TOP 10 SCORE', C_YELLOW, POS_S['Title'])
        self.score_t(20, 'NAME       SCORE            DATE         ', C_YELLOW, POS_S['Label'])
        db_p = DBProxy('DB_S')
        score_l = db_p.db_top10()
        db_p.close()

        for s in score_l:
            id_, name, score, date = s
            self.score_t(30, f'{name}      {score:05d}       {date}', C_YELLOW,
                            POS_S[score_l.index(s)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()


    def score_t(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Open Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M:%S")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f"{current_time} - {current_date}"
import pygame

from code1.const import W_WIDTH, W_HEIGHT, OPTIONS_MENU
from code1.level import Level
from code1.menu import Menu
from code1.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

    def run(self):

        while True:
            s = Score(self.window)
            menu = Menu(self.window)
            r_menu = menu.run()

            if r_menu in [OPTIONS_MENU[0], OPTIONS_MENU[1]]:
                score_p = [0, 0] #P1, P2
                level = Level(self.window, 'Level1', r_menu, score_p)
                r_level = level.run(score_p)
                if r_level:
                    level = Level(self.window, 'Level2', r_menu, score_p)
                    r_level = level.run(score_p)
                    if r_level:
                        s.save_s(r_menu, score_p)


            elif r_menu == OPTIONS_MENU[2]:
                s.show_s()
            elif r_menu == OPTIONS_MENU[3]:
                pygame.quit()
                quit()
            else:
                pass




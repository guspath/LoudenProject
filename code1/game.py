import pygame

from code1.const import W_WIDTH, W_HEIGHT, OPTIONS_MENU
from code1.level import Level
from code1.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            r_menu = menu.run()

            if r_menu in [OPTIONS_MENU[0], OPTIONS_MENU[1]]:
                level = Level(self.window, 'Level1', r_menu)
                r_level = level.run()
                if r_level:
                    level = Level(self.window, 'Level2', r_menu)
                    r_level = level.run()


            elif r_menu == OPTIONS_MENU[3]:
                pygame.quit()
                quit()
            else:
                pass




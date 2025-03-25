import pygame
import pygame.image
from pygame import Surface
from pygame.font import Font

from code1.const import W_WIDTH, C_YELLOW, OPTIONS_MENU, C_LEMON, C_ORANGE, C_BLUEE, C_ORANGEE, C_WHITE, C_L_BLUE, \
    C_L_GRAY, C_L_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menubg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        opt_menu = 0
        pygame.mixer_music.load('./asset/menumusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.text_menu(70, "Louden", C_WHITE, ((W_WIDTH / 2), 60))

            for i in range(len(OPTIONS_MENU)):
                if i == opt_menu:
                    self.text_menu(50, OPTIONS_MENU[i], C_ORANGE, ((W_WIDTH / 2), 170 + 60 * i))
                else:
                    self.text_menu(50, OPTIONS_MENU[i], C_YELLOW, ((W_WIDTH / 2), 170 + 60 * i))

            pygame.display.flip()

            # checking all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if opt_menu < len(OPTIONS_MENU) - 1:
                            opt_menu += 1
                        else:
                            opt_menu = 0
                    if event.key == pygame.K_UP:
                        if opt_menu > 0:
                            opt_menu -= 1
                        else:
                            opt_menu = len(OPTIONS_MENU) - 1

                    if event.key == pygame.K_RETURN: # ENTER KEY
                        return OPTIONS_MENU[opt_menu]



    def text_menu(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Open Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
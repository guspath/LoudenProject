import pygame
import pygame.image
from pygame import Surface
from pygame.font import Font

from code1.const import W_WIDTH, C_YELLOW, OPTIONS_MENU, C_LEMON, C_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menubg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/menumusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.text_menu(65, "Louden", C_LEMON, ((W_WIDTH / 2), 60))

            for i in range(len(OPTIONS_MENU)):
                self.text_menu(50, OPTIONS_MENU[i], C_ORANGE, ((W_WIDTH / 2), 170 + 60 * i))

            pygame.display.flip()

            # checking all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def text_menu(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Open Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
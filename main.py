import pygame
import sys

import consts
import character
import helpers


class Framework:
    def __init__(self, xa, ya, player_sprite_sheet, npc_sprite_sheet_list: list):
        pygame.init()
        self.screen = pygame.display.set_mode((consts.WIDTH, consts.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.player = character.Player(xa, ya, consts.CHARACTER_WIDTH, consts.CHARACTER_HEIGHT,
                                       consts.CHARACTER_DEFAULT_SPEED, player_sprite_sheet)
        self.npc_list = []

    def draw(self, screen):
        pass

    def run(self):
        self.running = True
        while self.running:
            self.draw(self.screen)
            self.clock.tick(consts.FPS)
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def keyup(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False


if __name__ == "__main__":
    pass

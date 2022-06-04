import pygame
import sys

import consts
import character
import helpers


class Framework:
    def __init__(self, xa, ya, player_sprite_sheet, npc_list):
        pygame.init()
        self.screen = pygame.display.set_mode((consts.WIDTH, consts.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.player = character.Player(xa, ya, consts.CHARACTER_WIDTH, consts.CHARACTER_HEIGHT,
                                       consts.CHARACTER_DEFAULT_SPEED, player_sprite_sheet, [5, 5, 7, 7])
        self.npc_list = npc_list

    def draw(self):
        # TODO: blit background
        # self.screen.blit(helpers.level, (player.xapx - consts.XRPX, player.yapx - consts.YRPX))
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)

    def load_level(self, levelname):
        # TODO: add collision rects
        helpers.level = pygame.image.load(levelname).convert_alpha()

    def run(self):
        self.running = True
        while self.running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.keydown(event.key)
                elif event.type == pygame.KEYUP:
                    self.keyup(event.key)
            self.clock.tick(consts.FPS)
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def keydown(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False
        self.player.keydown(key)

    def keyup(self, key):
        self.player.keyup(key)


if __name__ == "__main__":
    f = Framework(0, 0, "res/player_sprite_sheet.png", [])
    f.run()

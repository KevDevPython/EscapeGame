import random

import pygame

import consts
import helpers


class BaseCharacter:
    def __init__(self, xa, ya, w, h, speed, sprite_sheet, frame_cnt, facing=consts.SOUTH):
        self.xapx, self.yapx = helpers.a_to_apx(xa, ya)
        self.w, self.h = w, h
        self.frame_cnt = frame_cnt
        self.frame_list = list(map(helpers.gen_frame_list, frame_cnt))
        self.cur_frame = 0
        self.tick = 0
        self.speed = speed
        self.is_walking = False
        self.facing = facing
        self.cbox = pygame.Rect(self.xapx, self.yapx, w, h)
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.sprite_sheet.set_colorkey((0, 255, 0))

    def collide(self, level):
        return False

    def draw(self, screen):
        frame = 0
        if self.is_walking:
            frame = self.frame_list[self.facing][self.cur_frame % self.frame_cnt[self.facing]]
        # TODO: translate coords
        screen.blit(self.sprite_sheet, (self.xapx, self.yapx),
                    (frame * self.w, self.facing * self.h, self.w, self.h))
        self.tick = (self.tick + 1) % consts.FPS
        if self.tick in range(0, 100, self.speed * 2):
            self.cur_frame = (self.cur_frame + 1) % self.frame_cnt[self.facing]

    def move(self, facing):
        if self.is_walking and (not self.collide(helpers.level)):
            self.xapx += self.speed * consts.dx[facing]
            self.yapx += self.speed * consts.dy[facing]


class Player(BaseCharacter):
    def __init__(self, xa, ya, w, h, speed, sprite_sheet, frame_cnt, facing=consts.SOUTH):
        super(Player, self).__init__(xa, ya, w, h, speed, sprite_sheet, frame_cnt, facing)
        self.xrpx, self.yrpx = consts.PLAYER_XRPX, consts.PLAYER_YRPX
        self.inventory = [None] * 5

    def draw(self, screen):
        frame = 0
        if self.is_walking:
            frame = self.frame_list[self.facing][self.cur_frame % self.frame_cnt[self.facing]]
        screen.blit(self.sprite_sheet, (self.xrpx, self.yrpx),
                    (frame * self.w, self.facing * self.h, self.w, self.h))
        self.tick = (self.tick + 1) % consts.FPS
        if self.tick in range(0, 100, self.speed * 2):
            self.cur_frame = (self.cur_frame + 1) % self.frame_cnt[self.facing]

    def pick_up(self, item):
        # TODO: pick up item
        pass

    def get_looking_at(self):
        # TODO: get first interactable object in facing direction and radius
        pass

    def keyup(self, key):
        if key == pygame.K_w or key == pygame.K_s or key == pygame.K_a or key == pygame.K_d:
            self.is_walking = False

    def keydown(self, key):
        if key == pygame.K_w:
            self.is_walking = True
            self.facing = consts.NORTH
        elif key == pygame.K_s:
            self.is_walking = True
            self.facing = consts.SOUTH
        elif key == pygame.K_a:
            self.is_walking = True
            self.facing = consts.WEST
        elif key == pygame.K_d:
            self.is_walking = True
            self.facing = consts.EAST

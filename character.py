import random

import pygame

import consts
import helpers


class BaseCharacter:
    def __init__(self, xa, ya, w, h, speed, sprite_sheet, facing=consts.SOUTH):
        self.xapx, self.yapx = helpers.a_to_apx(xa, ya)
        self.w, self.h = w, h
        self.speed = speed
        self.is_walking = False
        self.facing = facing
        self.cbox = pygame.Rect(self.xapx, self.yapx, w, h)
        self.sprite_sheet = pygame.image.load(sprite_sheet)
        self.sprite_sheet.set_colorkey((0, 255, 0))

    def draw(self, screen):
        pass

    def move(self, facing):
        if self.is_walking:
            self.xapx += self.speed * consts.dx[facing]
            self.yapx += self.speed * consts.dy[facing]


class Worker(BaseCharacter):
    def __init__(self, xa, ya, w, h, speed, sprite_sheet, facing):
        self.status = consts.NPC_IDLE
        super(Worker, self).__init__(xa, ya, w, h, speed, sprite_sheet, facing)

    def draw(self, screen):
        pass

    def move(self, facing):
        if random.randint(0, 100) > 60:
            self.is_walking = 1 - self.is_walking
        super(Worker, self).move(self.facing)


class Enemy(BaseCharacter):
    def __init__(self, xa, ya, w, h, speed, sprite_sheet, facing):
        super(Enemy, self).__init__(xa, ya, w, h, speed, sprite_sheet, facing)

    def draw(self, screen):
        pass

    def move(self, facing):
        if random.randint(0, 100) > 60:
            self.is_walking = 1 - self.is_walking
        super(Enemy, self).move(self.facing)


class Player(BaseCharacter):
    def __init__(self, xa, ya, w, h, speed, sprite_sheet, facing):
        super(Player, self).__init__(xa, ya, w, h, speed, sprite_sheet, facing)
        self.xrpx, self.yrpx = consts.PLAYER_XRPX, consts.PLAYER_YRPX
        self.inventory = [None] * 5

    def pick_up(self, item):
        # TODO: pick up item
        pass

    def get_looking_at(self):
        # TODO: get first interactable object in facing direction and radius
        pass

    def key_up(self, key):
        if key == pygame.K_w or key == pygame.K_s or key == pygame.K_a or key == pygame.K_d:
            self.is_walking = False

    def key_down(self, key):
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


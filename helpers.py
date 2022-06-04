import pygame

import consts


def a_to_rpx(xa, ya):
    return xa, ya


def a_to_apx(xa, ya):
    return xa, ya


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def gen_frame_list(frame_cnt):
    frame_list = []
    mid = frame_cnt // 2 + 1
    frame_list += range(mid, 0, -1)
    frame_list += range(mid, frame_cnt + 1)
    return frame_list


level = None

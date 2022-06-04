import pygame

f = open('res/map.txt', 'r')
mapList = f.readlines()
SCREEN_H, SCREEN_W = len(mapList) * 16, len(mapList[0]) * 16
scr = pygame.display.set_mode((SCREEN_W, SCREEN_H))
while True:
    for i in range(len(mapList)):
        for j in range(len(mapList[i])):
            if mapList[i][j] == 'w':
                image = pygame.image.load('res/wall.png').convert_alpha()
                scr.blit(image, (j * 16, i * 16))
                clock = pygame.time.Clock()
                pygame.display.update()
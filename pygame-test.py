from pygame.locals import *
import pygame

green = (40,255,30)
brown = (40,60,90)

grass = 0
dirt = 1

colours = {
    grass: green,
    dirt: brown,
    }

tilemap = [
        [grass,dirt,dirt,dirt, grass],
        [dirt,grass,dirt,dirt, dirt],
        [grass, grass,dirt,dirt, grass],
        [grass, grass,dirt,dirt, grass],
        [dirt,dirt,dirt,dirt,grass]

        ]

TILESIZE = 50
MAPWIDTH =  5
MAPHEIGHT = 5

pygame.init()
DISPLAYMAP = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        DISPLAYMAP.fill((0, 0, 0))
        for row in range(MAPWIDTH):
            print
            for column in range(MAPHEIGHT):
                color = colours[tilemap[row][column]]
                pygame.draw.rect(DISPLAYMAP, color, (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))

    pygame.display.update()
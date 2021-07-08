# This is a work in progress
# It also requires you to have pygame installed
# Easiest way to do that is to run "pip install pygame"
# in your cmd prompt

import pygame, sys
from pygame.locals import *
from time import sleep

def main():
    pygame.init()

    CUBE_SIZE = 200
    CUBE_OFFSET = CUBE_SIZE/10
    CUBE_OFFSET = int(CUBE_OFFSET)

    DISPLAY_OFFSET = 50

    DISPLAY = pygame.display.set_mode(((4 * CUBE_SIZE) + (5 * CUBE_OFFSET) + (2 * DISPLAY_OFFSET),
                                       (4 * CUBE_SIZE) + (5 * CUBE_OFFSET) + (2 * DISPLAY_OFFSET)), 0, 32)

    WHITE = (255, 255, 255)
    DARK_BROWNISH = (187, 173, 160)
    LIGHT_BROWNISH = (205, 193, 180)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY, DARK_BROWNISH, (DISPLAY_OFFSET, DISPLAY_OFFSET,
                                              (4 * CUBE_SIZE) + (5 * CUBE_OFFSET),
                                              (4 * CUBE_SIZE) + (5 * CUBE_OFFSET)))
    for r in range(4):
        for c in range(4):
            pygame.draw.rect(DISPLAY, LIGHT_BROWNISH,
                             (DISPLAY_OFFSET + CUBE_OFFSET + (CUBE_OFFSET * c) + (CUBE_SIZE * c),
                              DISPLAY_OFFSET + CUBE_OFFSET + (CUBE_OFFSET * r) + (CUBE_SIZE * r),
                              CUBE_SIZE, CUBE_SIZE))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()

import pygame, sys
from pygame.locals import *
from time import sleep

CUBE_SIZE = 100
CUBE_OFFSET = CUBE_SIZE / 10
CUBE_OFFSET = int(CUBE_OFFSET)

DISPLAY_OFFSET = 50

pygame.font.init()
font = pygame.font.SysFont('Clear Sans', CUBE_SIZE//100 * 50)
text_surface = font.render('hello', False, (255, 0, 0))

DISPLAY = pygame.display.set_mode(((4 * CUBE_SIZE) + (5 * CUBE_OFFSET) + (2 * DISPLAY_OFFSET),
                                   (4 * CUBE_SIZE) + (5 * CUBE_OFFSET) + (2 * DISPLAY_OFFSET)), 0, 32)

WHITE = (255, 255, 255)
DARK_BROWNISH = (187, 173, 160)
LIGHT_BROWNISH = (205, 193, 180)
BLACK = (0, 0, 0)
game_colors = {0: LIGHT_BROWNISH,
               2: (238, 228, 218),
               4: (237, 224, 200),
               8: (242, 177, 121),
               16: (245, 149, 99),
               32: (246, 124, 96),
               64: (246, 94, 59),
               128: (237, 207, 115),
               256: (237, 204, 98),
               512: (237, 200, 80),
               1024: (237, 197, 63),
               2048: (237, 194, 45)}

game_board = [[0, 2, 4, 8],
              [16, 32, 64, 128],
              [256, 512, 1024, 2048],
              [0, 0, 0, 0]]

def cell_center(row, col):
    x_res = DISPLAY_OFFSET + CUBE_OFFSET + (CUBE_OFFSET * col) + (CUBE_SIZE * col) + int(CUBE_SIZE / 2)
    y_res = DISPLAY_OFFSET + CUBE_OFFSET + (CUBE_OFFSET * row) + (CUBE_SIZE * row) + int(CUBE_SIZE / 2)
    return x_res, y_res

def text_center(row, col, size):   # size[0] is the width, size[1] is the height
    # this function will return the x, y position to center the text on cell row, col
    # pass
    x_res, y_res = cell_center(row, col)
    x_res -= size[0]//2
    y_res -= size[1]//2
    return x_res, y_res

def print_board(board_2d):
    pygame.draw.rect(DISPLAY, DARK_BROWNISH, (DISPLAY_OFFSET, DISPLAY_OFFSET,
                                              (4 * CUBE_SIZE) + (5 * CUBE_OFFSET),
                                              (4 * CUBE_SIZE) + (5 * CUBE_OFFSET)))
    for r in range(4):
        for c in range(4):
            pygame.draw.rect(DISPLAY, game_colors[board_2d[r][c]],
                             (DISPLAY_OFFSET + CUBE_OFFSET + (CUBE_OFFSET * c) + (CUBE_SIZE * c),
                              DISPLAY_OFFSET + CUBE_OFFSET + (CUBE_OFFSET * r) + (CUBE_SIZE * r),
                              CUBE_SIZE, CUBE_SIZE))

    for row in range(4):
        for col in range(4):
            if board_2d[row][col] == 2 or board_2d[row][col] == 4:
                text_surface = font.render(str(board_2d[row][col]), False, BLACK)
                DISPLAY.blit(text_surface, text_center(row, col, text_surface.get_size()))

            elif board_2d[row][col] != 0:
                text_surface = font.render(str(board_2d[row][col]), False, WHITE)
                DISPLAY.blit(text_surface, text_center(row, col, text_surface.get_size()))

def main():
    pygame.init()

    DISPLAY.fill(WHITE)
    print_board(game_board)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()

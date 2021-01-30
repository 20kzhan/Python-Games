import msvcrt
import os, sys
import random
from random import randint
import time
from colorama import Fore, Back, Style, init
import numpy as np


BOARD_WIDTH = 16
BOARD_HEIGHT = 8
board = []

NO_BLOCKS = 1

block_count = 0

smiley_y = randint(0, BOARD_HEIGHT - 1)
smiley_x = randint(0, BOARD_WIDTH - 1)

border_off_row = BOARD_WIDTH - 1
border_off_col = BOARD_HEIGHT + 1

offset_row = border_off_row + 1
offset_col = border_off_col + 1

now = time.time()
future = now + 15

no_of_blocks = 0
no_of_goals = 0

def print_wall(height, width, offset_row, offset_col):
    width += 2
    height += 1
    for i in range(width):
        print(Fore.WHITE + '\033[{};{}H'.format(offset_row, offset_col + i) + '▓')
    for i in range(1, height + 1):
        print(Fore.WHITE + '\033[{};{}H'.format(offset_row + i, offset_col) + '▓', ' ' * (width - 4), '▓')
    for i in range(width):
        print(Fore.WHITE + '\033[{};{}H'.format(offset_row + height, offset_col + i) + '▓')


def get_object(board_2d, row, col):
    if BOARD_HEIGHT > row >= 0 and BOARD_WIDTH > col >= 0:
        # if int(board_2d[row][col]) == 1:
        #     return 1
        # elif int(board_2d[row][col]) == 0:
        #     return 0
        # elif int(board_2d[row][col]) == 3:
        #     return 3
        # elif int(board_2d[row][col]) == 2:
        #     return 2
        # elif int(board_2d[row][col]) == 4:
            return int(board_2d[row][col])
    return 5


def print_board(board_2d):
    for n, each_row in enumerate(board_2d):
        for i in range(len(board_2d[-1])):
            if each_row[i] == 1:
                print(Fore.WHITE + '\033[{};{}H'.format(n + offset_row, i + offset_col) + ' ')
            elif each_row[i] == 0:
                print(Fore.WHITE + '\033[{};{}H'.format(n + offset_row, i + offset_col) + 'Ö')
            elif each_row[i] == 2:
                print(Fore.WHITE + '\033[{};{}H'.format(n + offset_row, i + offset_col) + '▓')
            elif each_row[i] == 3:
                print(Fore.WHITE + '\033[{};{}H'.format(n + offset_row, i + offset_col) + '░')
            elif each_row[i] == 4:
                print(Fore.WHITE + '\033[{};{}H'.format(n + offset_row, i + offset_col) + '▒')
            else:
                print(Fore.RED + '\033[{};{}H'.format(n + offset_row, i + offset_col) + 'INVALID BOARD')
                break
        print()

def random_place(board_2d, num_blocks):
    global smiley_y, smiley_x

    smiley_y = randint(0, BOARD_HEIGHT - 1)
    smiley_x = randint(0, BOARD_WIDTH - 1)

    if board_2d[smiley_y][smiley_x] == 1:
        board_2d[smiley_y][smiley_x] = 0

    for i in range(num_blocks):
        while True:
            y = randint(1, BOARD_HEIGHT - 2)
            x = randint(1, BOARD_WIDTH - 2)
            if board_2d[y][x] == 1:
                board_2d[y][x] = 2
                break

    for i in range(num_blocks):
        while True:
            y = randint(1, BOARD_HEIGHT - 2)
            x = randint(1, BOARD_WIDTH - 2)
            if board_2d[y][x] == 1:
                board_2d[y][x] = 3
                break

def reset_board(board_2d):
    global NO_BLOCKS, block_count, future, now
    for i in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            board[i][x] = 1
    NO_BLOCKS += 1
    block_count = 0
    random_place(board, num_blocks=NO_BLOCKS)
    print_board(board)
    now = time.time()
    future = now + 10 + (NO_BLOCKS*5)


def move_object(board, y, x, direction, object):
    global NO_BLOCKS, block_count
    if object == 0:
        if direction == 'right':
            if get_object(board, y, x+1) == 1:
                board[y][x] = 1
                board[y][x+1] = 0
                return True
            elif get_object(board, y, x+1) == 2 and get_object(board, y, x+2) == 1:
                board[y][x] = 1
                board[y][x+1] = 0
                board[y][x+2] = 2
                return True
            elif get_object(board, y, x+1) == 2 and get_object(board, y, x+2) == 3:
                board[y][x+2] = 4
                board[y][x+1] = 0
                board[y][x] = 1
                block_count += 1
                if block_count == NO_BLOCKS:
                    reset_board(board)
                    print(':/', NO_BLOCKS, block_count)
                    return False
                return True
        elif direction == 'left':
            if get_object(board, y, x-1) == 1:
                board[y][x] = 1
                board[y][x-1] = 0
                return True
            elif get_object(board, y, x-1) == 2 and get_object(board, y, x-2) == 1:
                board[y][x] = 1
                board[y][x-1] = 0
                board[y][x-2] = 2
                return True
            elif get_object(board, y, x-1) == 2 and get_object(board, y, x-2) == 3:
                board[y][x-2] = 4
                board[y][x-1] = 0
                board[y][x] = 1
                block_count += 1
                if block_count == NO_BLOCKS:
                    reset_board(board)
                    print(':/', NO_BLOCKS, block_count)
                    return False
                return True
        elif direction == 'up':
            if get_object(board, y-1, x) == 1:
                board[y][x] = 1
                board[y-1][x] = 0
                return True
            elif get_object(board, y-1, x) == 2 and get_object(board, y-2, x) == 1:
                board[y][x] = 1
                board[y-1][x] = 0
                board[y-2][x] = 2
                return True
            elif get_object(board, y-1, x) == 2 and get_object(board, y-2, x) == 3:
                board[y-2][x] = 4
                board[y-1][x] = 0
                board[y][x] = 1
                block_count += 1
                if block_count == NO_BLOCKS:
                    reset_board(board)
                    print(':/', NO_BLOCKS, block_count)
                    return False
                return True
        elif direction == 'down':
            if get_object(board, y+1, x) == 1:
                board[y][x] = 1
                board[y+1][x] = 0
                return True
            elif get_object(board, y+1, x) == 2 and get_object(board, y+2, x) == 1:
                board[y][x] = 1
                board[y+1][x] = 0
                board[y+2][x] = 2
                return True
            elif get_object(board, y+1, x) == 2 and get_object(board, y+2, x) == 3:
                board[y+2][x] = 4
                board[y+1][x] = 0
                board[y][x] = 1
                block_count += 1
                if block_count == NO_BLOCKS:
                    reset_board(board)
                    print(':/', NO_BLOCKS, block_count)
                    return False
                return True
    # elif object == 2:
    #     if direction == 'right':
    #         board[y][x + 1] = 1
    #         board[y][x + 2] = 2
    #         return True
    #     elif direction == 'left':
    #         board[y][x - 1] = 1
    #         board[y][x - 2] = 2
    #         return True
    #     elif direction == 'up':
    #         board[y - 1][x] = 1
    #         board[y - 2][x] = 2
    #         return True
    #     elif direction == 'down':
    #         if get_object(board, y + 1, x) == 2 and get_object(board, y + 2, x) == 1:
    #             board[y + 1][x] = 1
    #             board[y + 2][x] = 2
    #             return True
    else:
        return False



if os.name == "nt":
    os.system("cls")

    import ctypes


    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    a_row = []

    for i in range(BOARD_HEIGHT):
        board.append([1] * BOARD_WIDTH)


    print_wall(BOARD_HEIGHT, BOARD_WIDTH, border_off_row, border_off_col)
    random_place(board, num_blocks=NO_BLOCKS)
    print_board(board)

    while time.time() < future:
        if msvcrt.kbhit():
            c = msvcrt.getch()
            if c == b'\xe0':
                c = msvcrt.getch()
                if str(c) == "b'M'":
                    if smiley_x < BOARD_WIDTH-1:
                        if move_object(board, smiley_y, smiley_x, 'right', 0):
                            smiley_x += 1
                            print_board(board)
                            print(Fore.GREEN + '\033[1;1H' + 'right pressed')
                elif str(c) == "b'K'":
                    if smiley_x > 0:
                        if move_object(board, smiley_y, smiley_x, 'left', 0):
                            smiley_x -= 1
                            print_board(board)
                            print(Fore.GREEN + '\033[1;1H' + 'left pressed    ')
                elif str(c) == "b'H'":
                    if smiley_y > 0:
                        if move_object(board, smiley_y, smiley_x, 'up', 0):
                            smiley_y -= 1
                            print_board(board)
                            print(Fore.GREEN + '\033[1;1H' + 'up pressed    ')
                elif str(c) == "b'P'":
                    if smiley_y < BOARD_HEIGHT-1:
                        if move_object(board, smiley_y, smiley_x, 'down', 0):
                            smiley_y += 1
                            print_board(board)
                            print(Fore.GREEN + '\033[1;1H' + 'down pressed ')
        print(Fore.GREEN + '\033[5;5H' + str(round(time.time()-now)))


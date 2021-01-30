import msvcrt
import os, sys
import random
from random import randint
from time import sleep
from colorama import Fore, Back, Style, init
import numpy as np


BOARD_WIDTH = 16
BOARD_HEIGHT = 8
board = []

border_off_row = BOARD_WIDTH - 1
border_off_col = BOARD_HEIGHT + 1

offset_row = border_off_row + 1
offset_col = border_off_col + 1


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

def move_object(board, y, x, direction, object):
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

def random_place(board_2d, num_blocks):
    if board_2d[randint(0, BOARD_HEIGHT - 1)][randint(0, BOARD_WIDTH - 1)] == 1:
        board_2d[randint(0, BOARD_HEIGHT - 1)][randint(0, BOARD_WIDTH - 1)] = 0

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
    print_board(board)

    no_of_blocks = 0
    no_of_goals = 0

    while True:
        print_wall(BOARD_HEIGHT, BOARD_WIDTH, border_off_row, border_off_col)
        random_place(board, num_blocks=2)
        print_board(board)
        smiley_y = randint(0, BOARD_HEIGHT - 1)
        smiley_x = randint(0, BOARD_WIDTH - 1)
        for each_row in board:
            for each_char in each_row:
                if each_char == 2:
                    no_of_blocks += 1
                elif each_char == 3:
                    no_of_goals += 1
        if no_of_blocks != 2:
            break
        elif no_of_goals != 2:
            break
        no_of_blocks = 0
        no_of_goals = 0
        for i in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                board[i][x] = 1
        # sleep(1)


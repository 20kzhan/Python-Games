from colorama import Fore
import msvcrt
import os, sys
import random
from random import randint
import time

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

game_board = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

def print_board(board_2d):
    offset = 0
    row_offset = 0
    for n, each_row in enumerate(board_2d):
        for i in range(len(board_2d[0])):
            print(Fore.WHITE + '\033[{};{}H'.format(5+n+row_offset, 15+i+offset) + ' ' + str(each_row[i]) + ' ')
            offset += 3
        offset = 0
        row_offset += 1

def place_new_value(board_2d):
    value = 0
    if randint(0, 9) != 9:
        value = 2
    else:
        value = 4
    while True:
        x = randint(0, len(board_2d[0])-1)
        y = randint(0, len(board_2d)-1)
        if board_2d[y][x] == 0:
            board_2d[y][x] = value
            break

def rotate_board(board2d):
    board2d = list(reversed(list(zip(*board2d))))
    return board2d

def game_over(board_2d):
    for each_row in board_2d:
        for i in range(len(board_2d[0])):
            if each_row[i] == 0:
                return False
    return True

def shift(sequence, right=False):
    if right:
        sequence = sequence[::-1]
    values = []
    empty = 0
    for n in sequence:
        if values and n == values[-1]:
            values[-1] = 2*n
            empty += 1
        elif n:
            values.append(n)
        else:
            empty += 1
    values += [0]*empty
    if right:
        values = values[::-1]
    return values

def shift_board_left(board_2d):
    # temporary_list = []
    # final_list = []
    #
    # for element in original_list:
    #     if element != 0:
    #         temporary_list.append(element)
    #
    # while len(temporary_list) < len(original_list):
    #     temporary_list.append(0)
    #
    # count_var = 0
    # flag_var = 0
    # if len(temporary_list) % 2 == 0:
    #     temporary_list.append(0)
    #
    # while count_var < len(temporary_list) - 1:
    #     if temporary_list[count_var] == temporary_list[count_var + 1] and temporary_list[count_var] != 0:
    #         add = 2 * temporary_list[count_var]
    #         final_list.append(add)
    #         count_var = count_var + 2
    #     else:
    #         flag_var = flag_var + 1
    #         final_list.append(temporary_list[count_var])
    #         count_var = count_var + 1
    # if count_var < len(temporary_list):
    #     final_list.append(temporary_list[count_var])
    #
    # final_count = len(final_list)
    # original_count = len(original_list)
    #
    # while final_count < original_count:
    #     final_list.append(0)
    #     final_count = final_count + 1
    #
    # if flag_var == len(original_list):
    #     temporary_list.pop()
    #     print(temporary_list)
    # else:
    #     print(final_list)
    for i in range(len(board_2d)):
        shift(board_2d[i], right=False)
    return board_2d

def shift_board_right(board2d):
    for i in range(4):
        shift(board2d[i], right=True)

def shift_board_down(board2d):
    board2d = rotate_board(board2d)
    for i in range(4):
        board2d[i] = shift(board2d[i], right=True)
    for i in range(3):
        board2d = rotate_board(board2d)
    return board2d

def shift_board_up(board2d):
    board2d = rotate_board(board2d)
    for i in range(4):
        board2d[i] = shift(board2d[i], right=False)
    for i in range(3):
        board2d = rotate_board(board2d)
    return board2d

# # directions are: 0: up, 1: right, 2: down, 3: left
# def play(gb, direction):
#     print("Direction: ", direction)



from colorama import Fore
import msvcrt
import os, sys
import random
from random import randint
import time
import numpy as np
import keyboard

X_O_STR = ['   ', ' O ', ' X ']
DIVIDER_STR = ['-'*11 + ' '*8 + '-'*11, '-'*11 + ' '*8 + '-'*11, '']
HORIZONTAL_DIVIDER = ['|', '|', ' '*8]

BOARD_ROW = 5
BOARD_COL = 5

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

def print_board(board_2d):
    for n, each_row in enumerate(board_2d):
        print(Fore.WHITE + '\033[{};{}H'.format(n*2+BOARD_ROW, BOARD_COL), end='')
        for i in range(len(each_row)):
            print(X_O_STR[each_row[i]], end='')
            print(HORIZONTAL_DIVIDER[i], end='')

        for i in range(len(each_row)):
            # print(' ' + str(i+n*3+1) + ' ', end='') if each_row[i] == 0 else print('   ', end='')
            print(' ' + str(i+n*3+1) + ' ' if each_row[i] == 0 else ' . ', end='')
            print(HORIZONTAL_DIVIDER[i], end='')

        print(Fore.WHITE + '\033[{};{}H'.format(BOARD_ROW+(n*2+1), BOARD_COL) + DIVIDER_STR[n])


def check_game_over(board_2d):
    temp_list = []
    for i in range(len(board_2d[0])):
        for each_row in board_2d:
            temp_list.append(each_row[i])
        if len(list(set(temp_list))) == 1 and temp_list[0] == 1:
            return True, 'O'
        elif len(list(set(temp_list))) == 1 and temp_list[0] == 2:
            return True, 'X'
        temp_list = []
    for i in range(len(board_2d[0])):
        for each_row in board_2d:
            if len(list(set(each_row))) == 1 and each_row[0] == 1:
                return True, 'O'
            elif len(list(set(each_row))) == 1 and each_row[0] == 2:
                return True, 'X'
    cross1sum = []
    cross0sum = []
    for i in range(len(board_2d)):
        cross1sum.append(board_2d[(len(board_2d[0]) - 1) - i][i])
        cross0sum.append(board_2d[i][i])
    if len(list(set(cross1sum))) == 1 and cross1sum[0] == 1:
        return True, 'O'
    elif len(list(set(cross1sum))) == 1 and cross1sum[0] == 2:
        return True, 'X'
    if len(list(set(cross0sum))) == 1 and cross0sum[0] == 1:
        return True, 'O'
    elif len(list(set(cross0sum))) == 1 and cross0sum[0] == 2:
        return True, 'X'
    return False, 0

def update_board(board_2d, row, col, change_to):
    if board_2d[row][col] == 0:
        if change_to == -1:
            board_2d[row][col] = 2
        elif change_to == 1:
            board_2d[row][col] = 1

def check_pos_clear(board_2d, row, col):
    if board_2d[row][col] == 0:
        return True
    else:
        return False

game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

print_board(game_board)
# print(check_game_over(game_board))

last_turn_taken = 1

while True:
    # if last_turn_taken == 'X':
    #     for i in range(len(game_board[0])):
    #         if keyboard.is_pressed(str(i+1)) and game_board[0][i] == 0:
    #             update_board(game_board, 0, i, 2)
    #             last_turn_taken = 'O'
    #             break
    #     for i in range(len(game_board[0])):
    #         if keyboard.is_pressed(str(i+1)) and game_board[1][i] == 0:
    #             update_board(game_board, 1, i, 2)
    #             last_turn_taken = 'O'
    #             break
    #     for i in range(len(game_board[0])):
    #         if keyboard.is_pressed(str(i+1)) and game_board[2][i] == 0:
    #             update_board(game_board, 2, i, 2)
    #             last_turn_taken = 'O'
    #             break
    if msvcrt.kbhit():
        c = msvcrt.getch()
        if c == b'1' and check_pos_clear(game_board, 0, 0):
            update_board(game_board, 0, 0, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'2' and check_pos_clear(game_board, 0, 1):
            update_board(game_board, 0, 1, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'3' and check_pos_clear(game_board, 0, 2):
            update_board(game_board, 0, 2, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'4' and check_pos_clear(game_board, 1, 0):
            update_board(game_board, 1, 0, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'5' and check_pos_clear(game_board, 1, 1):
            update_board(game_board, 1, 1, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'6' and check_pos_clear(game_board, 1, 2):
            update_board(game_board, 1, 2, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'7' and check_pos_clear(game_board, 2, 0):
            update_board(game_board, 2, 0, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'8' and check_pos_clear(game_board, 2, 1):
            update_board(game_board, 2, 1, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        elif c == b'9' and check_pos_clear(game_board, 2, 2):
            update_board(game_board, 2, 2, last_turn_taken)
            print_board(game_board)
            last_turn_taken *= -1
        else:
            print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 8) + "Error: invalid move or spot is already taken!")
        if check_game_over(game_board)[0]:
            print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "                                ")
            print(Fore.WHITE + '\033[{};17H'.format(BOARD_ROW + 6) + check_game_over(game_board)[1] + ' Wins!')
            os.system(exit())

    # 1 is O

    if last_turn_taken == -1:
        print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "X's turn, please make your move:")
    else:
        print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "O's turn, please make your move:")



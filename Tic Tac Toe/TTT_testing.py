from colorama import Fore
import msvcrt
import os, sys
import random
from random import randint
import time
import numpy as np

X_O_STR = ['   ', ' O ', ' X ']
DIVIDER_STR = ['-'*11 + ' '*8 + '-'*11, '-'*12, '']
HORIZONTAL_DIVIDER = ['|', '|', '']

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
    a_row = []

    def print_board(board_2d):
        for n, each_row in enumerate(board_2d):
            print(Fore.WHITE + '\033[{};{}H'.format(n*2+BOARD_ROW, BOARD_COL), end='')
            for i in range(len(each_row)):
                print(X_O_STR[each_row[i]], end='')
                print(HORIZONTAL_DIVIDER[i], end='')

            print(' '*8, end='')

            for i in range(len(each_row)):
                if each_row[i] == 0:
                    print(' ' + str(i+n*3) + ' ', end='')
                else:
                    print(' . ', end='')
                print(HORIZONTAL_DIVIDER[i], end='')

            if n < 2:
                print(Fore.WHITE + '\033[{};{}H'.format(BOARD_ROW+(n*2+1), BOARD_COL + 19) + '-' * 11, end='')
                print(Fore.WHITE + '\033[{};{}H'.format(BOARD_ROW+(n*2+1), BOARD_COL) + '-' * 11, end='')
            elif n == 2:
                print()

    def check_game_over(board_2d):
        temp_list = []
        for i in range(len(board_2d[0])):
            for each_row in board_2d:
                temp_list.append(each_row[i])
            if len(list(set(temp_list))) == 1 and temp_list[0] == 1:
                return True, 2
            elif len(list(set(temp_list))) == 1 and temp_list[0] == 2:
                return True, 1
            temp_list = []
        for i in range(len(board_2d[0])):
            for each_row in board_2d:
                if len(list(set(each_row))) == 1 and each_row[0] == 1:
                    return True, 2
                elif len(list(set(each_row))) == 1 and each_row[0] == 2:
                    return True, 1
        cross1sum = []
        cross0sum = []
        for i in range(len(board_2d)):
            cross1sum.append(board_2d[(len(board_2d[0]) - 1) - i][i])
            cross0sum.append(board_2d[i][i])
        if len(list(set(cross1sum))) == 1 and cross1sum[0] == 1:
            return True, 2
        elif len(list(set(cross1sum))) == 1 and cross1sum[0] == 2:
            return True, 1
        if len(list(set(cross0sum))) == 1 and cross0sum[0] == 1:
            return True, 2
        elif len(list(set(cross0sum))) == 1 and cross0sum[0] == 2:
            return True, 1
        for i in range(len(board_2d)):
            if board_2d[i].count(0) > 0:
                return False, 0
        return True, 0


    # test row wins

    for winner in [1, 2]:
        
        game_board = [[winner] * 3] + [[0] * 3 for i in range(2)]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)
        game_board = [[0] * 3, [winner] * 3, [0] * 3]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)
        game_board = [[0] * 3 for i in range(2)] + [[winner] * 3]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)

        # test col wins

        
        game_board = [[winner, 0, 0] for i in range(3)]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)
        game_board = [[0, winner, 0] for i in range(3)]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)
        game_board = [[0, 0, winner] for i in range(3)]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)

        # test cross wins

        
        game_board = [[winner, 0, 0], [0, winner, 0], [0, 0, winner]]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)
        game_board = [[0, 0, winner], [0, winner, 0], [winner, 0, 0]]
        print(check_game_over(game_board))
        print_board(game_board)
        time.sleep(0.5)

    # test ties

    
    game_board = [[0] * 3 for i in range(3)]
    for r in range(2):
        for c in range(3):
            game_board[r][c] = (r * 3 + c) % 2 + 1
            print(check_game_over(game_board))
            print_board(game_board)
            time.sleep(0.5)
    game_board[2] = [2, 0, 0]
    print(check_game_over(game_board))
    print_board(game_board)
    time.sleep(0.5)
    game_board[2] = [2, 1, 0]
    print(check_game_over(game_board))
    print_board(game_board)
    time.sleep(0.5)
    game_board[2] = [2, 1, 2]
    print(check_game_over(game_board))
    print_board(game_board)
    time.sleep(0.5)

    quit()
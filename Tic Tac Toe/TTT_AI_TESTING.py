# *ominous music starts playing*

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


def get_stats(board2d):
    ncorners = 0
    nsides = 0
    ncenter = 0
    if board2d[0][0] == 1:
        ncorners += 1
    if board2d[0][1] == 1:
        nsides += 1
    if board2d[0][2] == 1:
        ncorners += 1
    if board2d[1][0] == 1:
        nsides += 1
    if board2d[1][2] == 1:
        nsides += 1
    if board2d[1][1] == 1:
        ncenter += 1
    if board2d[2][0] == 1:
        ncorners += 1
    if board2d[2][1] == 1:
        nsides += 1
    if board2d[2][2] == 1:
        ncorners += 1
    return (ncorners, nsides, ncenter)

def block(board_2d):
    for each_row in board_2d:
        for i in range(len(each_row)):
            if each_row[i] == 0:
                each_row[i] = 1
                if check_game_over(board_2d)[0]:
                    each_row[i] = 2
                    return True
                else:
                    each_row[i] = 0
    return False

def finish_board(board_2d):
    for each_row in board_2d:
        for i in range(len(each_row)):
            if each_row[i] == 0:
                each_row[i] = 2
                if check_game_over(board_2d)[0]:
                    return True
                else:
                    each_row[i] = 0
    return False

def ai_next_move(board_2d):
    # input('ai used next move')
    turns_taken = 0
    for each_row in board_2d:
        for i in range(len(each_row)):
            if each_row[i] != 0:
                turns_taken += 1
    # input(turns_taken)
    if finish_board(board_2d):
        # input('ai used finish board')
        return
    elif block(board_2d):
        # input('ai used block')
        return
    elif turns_taken == 1:
        if get_stats(board_2d)[2] == 0:
            board_2d[1][1] = 2
            # input('ai ended turn0  ')
        else:
            board_2d[0][0] = 2
        return
    elif turns_taken == 3:
        # handling all the special cases
        if get_stats(board_2d)[0] == 1 and get_stats(board_2d)[1] == 1:
            if board_2d[2][1] == 1 or board_2d[1][2] == 1:
                board_2d[2][2] = 2
                return
            else:
                board_2d[0][0] = 2
                return
        elif get_stats(board_2d)[0] == 2:
            board_2d[0][1] = 2
            return
        elif get_stats(board_2d)[1] == 2:
            if board_2d[2][1] == board_2d[1][2] == 1:
                board_2d[2][2] = 2
            else:
                board_2d[0][0] = 2
            return
        elif get_stats(board_2d)[0] == 1 and get_stats(board_2d)[2] == 1:
            board_2d[0][2] = 2
            return
    else:
        # find any random empty spot!
        while True:
            row = randint(0,2)
            col = randint(0,2)
            if board_2d[row][col] == 0:
                board_2d[row][col] = 2
                return

def dumb_ai(board2d):
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if game_board[row][col] == 0:
            game_board[row][col] = 1
            return


'''
    temp_list = []
    for i in range(len(board_2d[0])):
        for each_row in board_2d:
            temp_list.append(each_row[i])
        if temp_list.count(0) == 1:
            for x in range(3):
                if temp_list[x] == 0:
                    return x, i
        temp_list = []
    for i in range(len(board_2d[0])):
        for each_row in board_2d:
            if each_row.count(0) == 1:
                for x in range(3):
                    if each_row[x] == 0:
                        return i, x
    cross1sum = []
    cross0sum = []
    for i in range(len(board_2d)):
        cross1sum.append(board_2d[(len(board_2d[0]) - 1) - i][i])
        cross0sum.append(board_2d[i][i])
    if cross1sum.count(0) == 1:
        for x in range(3):
            if cross1sum[x] == 0 and x == 0:
                return 2, x
            if cross1sum[x] == 0 and x == 1:
                return 1, x
            if cross1sum[x] == 0 and x == 2:
                return 0, x
    if cross0sum.count(0) == 1:

        for x in range(3):
            if cross0sum[x] == 0:
                return x, x
'''
# def finish_game(board_2d):
#     board_template = board_2d
#     for each_row in board_template:
#         for i in range(len(each_row)):
#             if each_row[i] == 1:
#                 each_row[i] = 0
#     temp_list = []
#     temp_list2 = []
#     for i in range(len(board_template[0])):
#         for each_row in board_template:
#             temp_list.append(each_row[i])
#         if temp_list.count(0) == 1:
#             for x in range(3):
#                 if temp_list[x] == 0:
#                     return x, i
#         temp_list = []
#     for i in range(len(board_template[0])):
#         for each_row in board_template:
#             if each_row.count(0) == 1:
#                 for x in range(3):
#                     if each_row[x] == 0:
#                         return i, x
#     cross1sum = []
#     cross0sum = []
#     for i in range(len(board_template)):
#         cross1sum.append(board_template[(len(board_template[0]) - 1) - i][i])
#         cross0sum.append(board_template[i][i])
#     if cross1sum.count(0) == 1:
#         for x in range(3):
#             if cross1sum[x] == 0 and x == 0:
#                 return 2, x
#             if cross1sum[x] == 0 and x == 1:
#                 return 1, x
#             if cross1sum[x] == 0 and x == 2:
#                 return 0, x
#     if cross0sum.count(0) == 1:
#
#         for x in range(3):
#             if cross0sum[x] == 0:
#                 return x, x

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
    for each_row in board_2d:
        if each_row.count(0) != 0:
            return False, 0
    return True, 0

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

while True:
    game_board = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    print_board(game_board)
    # print(check_game_over(game_board))

    last_turn_taken = 1

    while True:
        if last_turn_taken == 1:
            dumb_ai(game_board)
            print_board(game_board)
            last_turn_taken *= -1

        if last_turn_taken == -1:
            ai_next_move(game_board)
            print_board(game_board)
            if check_game_over(game_board)[0] == True and check_game_over(game_board)[1] != 0:
                print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "                                ")
                print(Fore.WHITE + '\033[{};17H'.format(BOARD_ROW + 6) + str(check_game_over(game_board)[1]) + ' Wins!')
                break
            elif check_game_over(game_board)[0]:
                print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "                                ")
                print(Fore.WHITE + '\033[{};15H'.format(BOARD_ROW + 6) + "It's a tie!")
                break
            # elif check_game_over(game_board)[0] == True and check_game_over(game_board)[1] == 'X':
            #     print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "                                ")
            #     print(Fore.WHITE + '\033[{};17H'.format(BOARD_ROW + 6) + str(check_game_over(game_board)[1]) + ' Wins!')
            #     break
            last_turn_taken *= -1
        if msvcrt.kbhit():
            c = msvcrt.getch()
            if c == b'c':
                break
        if check_game_over(game_board)[0] and check_game_over(game_board)[1] == 2:
            print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "                                ")
            print(Fore.WHITE + '\033[{};17H'.format(BOARD_ROW + 6) + 'X Wins!')
            game_board = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]

            break

        elif check_game_over(game_board)[0] and check_game_over(game_board)[1] == 0:
            print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "                                ")
            print(Fore.WHITE + '\033[{};15H'.format(BOARD_ROW + 6) + "It's a tie!")
            game_board = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]

            break
        elif check_game_over(game_board)[0] and check_game_over(game_board)[1] == 'O':
            os.system(exit())


        # 1 is O

        if last_turn_taken == -1:
            print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "X's turn, please make your move:")
        else:
            print(Fore.WHITE + '\033[{};5H'.format(BOARD_ROW + 7) + "O's turn, please make your move:")

        time.sleep(0.05)

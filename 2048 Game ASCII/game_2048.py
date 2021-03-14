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

horizontal_divider = ['------' * 4] * 3 + ['']

vertical_divider = ['|'] * 3 + ['']


def print_board(board_2d):
    offset = 0
    row_offset = 0
    for n, each_row in enumerate(board_2d):
        for i in range(len(board_2d[0])):
            if each_row[i] != 0:
                print(Fore.WHITE +
                      '\033[{};{}H'.format(5+n+row_offset, 15+i+offset) +
                      str(each_row[i]).center(5) + vertical_divider[i])
            else:
                print(Fore.WHITE +
                      '\033[{};{}H'.format(5 + n + row_offset, 15 + i + offset) + "     " + vertical_divider[i])
            offset += 6
        offset = 0
        print(Fore.WHITE +
              '\033[{};{}H'.format(6 + n + row_offset, 15 + offset) + horizontal_divider[n])
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
    board_col = len(board2d[0])
    new = []
    for i in range(board_col):
        new.append([0]*board_col)
    for col in range(len(board2d[0])):
        for row in range(len(board2d)):
            new[row][col] = board2d[col][row]
    return new

def game_over(board_2d):
    board_copy = board_2d.copy()
    shift_board_up(board_copy)
    for each_row in board_2d:
        for i in range(len(board_2d[0])):
            if each_row[i] == 0:
                return False
    board_copy = board_2d.copy()
    shift_board_down(board_copy)
    for each_row in board_2d:
        for i in range(len(board_2d[0])):
            if each_row[i] == 0:
                return False
    board_copy = board_2d.copy()
    shift_board_left(board_copy)
    for each_row in board_2d:
        for i in range(len(board_2d[0])):
            if each_row[i] == 0:
                return False
    board_copy = board_2d.copy()
    shift_board_right(board_copy)
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
    for i in range(len(board_2d)):
        board_2d[i] = shift(board_2d[i], right=False)
    return board_2d

def shift_board_right(board_2d):
    for i in range(4):
        board_2d[i] = shift(board_2d[i], right=True)
    return board_2d

def shift_board_down(board2d):
    board2d = rotate_board(board2d)
    for i in range(4):
        board2d[i] = shift(board2d[i], right=True)
    # shift_board_right(board2d)
    board2d = rotate_board(board2d)
    return board2d

def shift_board_up(board2d):
    board2d = rotate_board(board2d)
    for i in range(4):
        board2d[i] = shift(board2d[i], right=False)
    # shift_board_left(board2d)
    board2d = rotate_board(board2d)
    return board2d

# # directions are: 0: up, 1: right, 2: down, 3: left
# def play(gb, direction):
#     print("Direction: ", direction)


if __name__ == "__main__":
    game_board = [[0]*len(game_board[0]), [0]*len(game_board[0]), [0]*len(game_board[0]), [0]*len(game_board[0])]
    # game_board = [[7, 5, 9, 1],
    #       [5, 6, 12, 9],
    #       [34, 43, 31, 21],
    #       [12, 56, 67, 85]]

    place_new_value(game_board)
    place_new_value(game_board)
    while True:
        print_board(game_board)
        for each_row in game_board:
            for i in range(len(each_row)):
                if each_row[i] == 2048:
                    print(Fore.WHITE + '\033[14;15H' + 'Congratulations! You win!')
                    input(Fore.WHITE + '\033[15;15H' + 'Press Enter to quit')
                    os.system(exit())
        if game_over(game_board):
            print(Fore.WHITE + '\033[14;18H' + 'Game Over!')
            os.system(exit())
        if msvcrt.kbhit():
            c = msvcrt.getch()
            if c == b'\xe0':
                c = msvcrt.getch()
                if str(c) == "b'M'":
                    print(Fore.GREEN + '\033[1;1H' + 'right pressed')
                    game_board = shift_board_right(game_board)
                    place_new_value(game_board)
                elif str(c) == "b'K'":
                    print(Fore.GREEN + '\033[1;1H' + 'left pressed    ')
                    game_board = shift_board_left(game_board)
                    place_new_value(game_board)
                elif str(c) == "b'H'":
                    print(Fore.GREEN + '\033[1;1H' + 'up pressed    ')
                    game_board = shift_board_up(game_board)
                    place_new_value(game_board)
                elif str(c) == "b'P'":
                    print(Fore.GREEN + '\033[1;1H' + 'down pressed')
                    game_board = shift_board_down(game_board)
                    place_new_value(game_board)
        print_board(game_board)
        time.sleep(0.2)
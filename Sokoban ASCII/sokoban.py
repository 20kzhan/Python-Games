import msvcrt
import os, sys
from random import randint
from time import sleep
from colorama import Fore, Back, Style, init

board = []
board_width = 8
board_height = 4
numof1s = 0
count = 0

top_row = [1] * 8
middle_rows = [0] * 8
bottom_row = top_row

#for the 5th slide, i just need to print the top row and the bottom row in a loop

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

    # for i in range(int(board_width/2)):
        # a_row.append(1)
        # a_row.append(0)

    for row in range(board_height):
        a_row = []
        for col in range(board_width):
            a_row.append(randint(0, 3))
        board.append(a_row)

    for row in range(board_height):
        print(board[row])

    for each_row in board:
        for i in range(len(board[-1])):
            if each_row[i] == 0:
                each_row[i] = ' '
            elif each_row[i] == 1:
                each_row[i] = 'Ö'
            elif each_row[i] == 2:
                each_row[i] = '▓'
            else:
                each_row[i] = '░'

    for row in range(board_height):
        print(board[row])

# Ö▓░

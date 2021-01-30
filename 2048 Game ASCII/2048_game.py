from colorama import Fore
import msvcrt
import os, sys
import random
from random import randint
import time
import numpy as np
import keyboard

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
    if randint(0, 10) != 10:
        value = 4
    else:
        value = 2
    while True:
        x = randint(0, len(board_2d[0]))
        y = randint(0, len(board_2d))
        if board_2d[y][x] == 0:
            board_2d[y][x] = value
            break

print_board(game_board)

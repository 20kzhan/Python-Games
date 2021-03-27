import msvcrt
import os, sys
import random
from time import sleep
from colorama import Fore, Back, Style, init
from enum import Enum

ROVER_ROW = 40
ROVER_COL = 40
SCREEN_HEIGHT = 50
SCREEN_WIDTH = 100
TEXT_POS = '\033[{};{}H'

ROVER_IMAGE = ['Ö▓▓▓▓▓Ö',
               ' ▓▓░▓▓ ',
               ' ▓░Ö░▓ ',
               'Ö▓▓▓▓▓Ö']
ROVER_COLOR = Fore.RED

MISSILE_IMAGE = ['|']
MISSILE_COLOR = Fore.GREEN

BOULDER_IMAGE = [' O ',
                 'OOO',
                 ' O ']


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Missile:
    color = MISSILE_COLOR
    image = MISSILE_IMAGE

    def __init__(self, pos, pos_limits={'min_row': 2,
                                        'max_row': ROVER_ROW,
                                        'min_col': 1,
                                        'max_col': SCREEN_WIDTH}):
        self._pos = pos

    # I don't get what self._pos is or what use pos_limits has

    def draw(self):
        print(Fore.WHITE + '\033[{};{}H'.format(row, col) + MISSILE_IMAGE)

    def clear(self):
        print(Fore.WHITE + '\033[{};{}H'.format(row, col) + ' ')

    def move(self):
        # What am I supposed to do????
        pass

    def get_position(self):
        pass

    def is_done(self):
        pass


class Rover:
    image = ROVER_IMAGE
    color = ROVER_COLOR

    def __init__(self, rover_row=ROVER_ROW, rover_col=ROVER_COL):
        self._row = rover_row
        self._col = rover_col
        pass

    def draw(self):
        for n, line in enumerate(ROVER_IMAGE):
            print(Fore.RED + '\033[{};{}H'.format(self._row + n, self._col)
                  + ' ' + line + ' ')

            print(Fore.RED + '\033[{};{}H'.format(self._row - 1, self._col)
                  + ' ' * (len(ROVER_IMAGE[0]) + 1))

            print(Fore.RED + '\033[{};{}H'.format(self._row + len(ROVER_IMAGE), self._col)
                  + ' ' * (len(ROVER_IMAGE[0]) + 1))

    def clear(self):
        # no need look closely at draw() :)
        pass

    def move(self, direction):
        # is going to 
        # 1. call clear() to clear the rover from the screen
        # 2. change the rover's position (left, right, up, down) make changes to self._row or self._col
        # 3. call draw() to print the rover in the new position
        pass

    def has_collided(self, other):
        pass

    def get_position(self):
        pass

    def get_gun_position(self):
        pass


# for windows OS 
if os.name == "nt":
    os.system("cls")

    import msvcrt
    import ctypes


    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

rover = Rover()
rover.draw()

while True:
    if msvcrt.kbhit():
        c = msvcrt.getch()
        if c == b'\xe0':
            c = msvcrt.getch()
            if c == b'H':
                print(Fore.GREEN + '\033[1;1H' + "up pressed       ")
                rover.move(Direction.UP)
            elif c == b'M':
                rover.move(Direction.RIGHT)
                print(Fore.GREEN + '\033[1;1H' + "right pressed    ")
            elif c == b'K':
                rover.move(Direction.LEFT)
                print(Fore.GREEN + '\033[1;1H' + "left pressed     ")
            elif c == b'P':
                rover.move(Direction.DOWN)
                print(Fore.GREEN + '\033[1;1H' + "down pressed     ")
import msvcrt
import os, sys
from random import *
from time import *
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

class TermPos:
    def __init__(self, row, col):
        self._row = row
        self._col = col

    def __str__(self):
        s = '\033[{};{}H'.format(self._row, self._col)
        return s

class Boulder:
    def __init__(self, color=Fore.WHITE, col_inc=0,
                 row=1, col=randint(1, SCREEN_WIDTH - len(BOULDER_IMAGE[0]))):
        self._row = row
        self._col = col
        self._color = color
        self._col_inc = col_inc

    def draw(self):
        for n, line in enumerate(BOULDER_IMAGE):
            print(self._color + str(TermPos(self._row + n, self._col)) + line)

    def clear(self):
        for n, line in enumerate(BOULDER_IMAGE):
            print(self._color + str(TermPos(self._row + n, self._col)) + ' ' * len(line))

    def move(self):
        if self._row <= SCREEN_HEIGHT:
            self.clear()
            self._row += 1
            if 2 <= self._col <= SCREEN_WIDTH - len(BOULDER_IMAGE[0]):
                self._col += self._col_inc
            else:
                self._col_inc *= -1
                self._col += self._col_inc
            self.draw()

    def get_pos(self):
        return self._row, self._col

    def is_done(self):
        if self._row >= SCREEN_HEIGHT:
            return True

class Missile:
    color = MISSILE_COLOR
    image = MISSILE_IMAGE

    def __init__(self, row, col):

        self._row = row
        self._col = col

    # I don't get what self._pos is or what use pos_limits has

    def draw(self):
        for n, line in enumerate(MISSILE_IMAGE):
            print(Fore.WHITE + str(TermPos(self._row + n, self._col)) + line)

    def clear(self):
        for n, line in enumerate(MISSILE_IMAGE):
            print(str(TermPos(self._row + n, self._col)) + ' ' * len(line))

    def move(self):
        if self._row >= 2:
            self.clear()
            self._row -= 1
            self.draw()

    def get_position(self):
        return self._row, self._col

    def is_done(self):
        if self._row == 1:
            return True

class Obstacle:
    def __init__(self, num_boulders):
        self._boulders = []
        self._max_boulders = num_boulders

    def animate(self):
        if len(self._boulders) < self._max_boulders and randint(1, 2) == 1:
            self._boulders.append(Boulder(row=1, col=randint(1, SCREEN_WIDTH - len(BOULDER_IMAGE[0]))))
        for i, b in enumerate(self._boulders):
            b.move()
            if b.is_done():
                b.clear()
                self._boulders.pop(i)

class Weapon:
    def __init__(self, num_missiles):
        self._launched_missiles = []
        #self._standby_missiles = []
        #self._row, self._col = rover.get_gun_position()[0], rover.get_gun_position()[1]
        self._max_missiles = num_missiles
        #for i in range(num_missiles):
        #    self._standby_missiles.append(Missile(self._row, self._col))

    def fire(self, gun_pos_row, gun_pos_col):

        if len(self._launched_missiles) < self._max_missiles:
            self._launched_missiles.append(Missile(gun_pos_row, gun_pos_col))
            self._launched_missiles[-1].draw()
            return True
        return False

    def animate(self):
        for each_missile in self._launched_missiles:
            each_missile.move()
        i = 0
        while i < len(self._launched_missiles):
            if self._launched_missiles[i].is_done():
                self._launched_missiles[i].clear()
                self._launched_missiles.pop(i)
            else:
                i += 1



class Rover:
    image = ROVER_IMAGE
    color = ROVER_COLOR

    def __init__(self, rover_row=ROVER_ROW, rover_col=ROVER_COL):
        self._row = rover_row
        self._col = rover_col
        pass

    def draw(self):
        print(Fore.RED)
        for n, line in enumerate(ROVER_IMAGE):
            print(str(TermPos(self._row + n, self._col)) + line)

    def clear(self):
        print(Fore.RED)
        for n, line in enumerate(ROVER_IMAGE):
            print(str(TermPos(self._row + n, self._col)) + ' ' * len(line))

    def move(self, direction):
        if direction == Direction.UP and self._row >= 3:
            self.clear()
            self._row -= 1
            self.draw()
        if direction == Direction.DOWN and self._row <= 39:
            self.clear()
            self._row += 1
            self.draw()
        if direction == Direction.LEFT and self._col >= 4:
            self.clear()
            self._col -= 1
            self.draw()
        if direction == Direction.RIGHT and self._col <= 80:
            self.clear()
            self._col += 1
            self.draw()
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
        return (self._row - 1, self._col + len(ROVER_IMAGE[0]) // 2)

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

mars_obstacles1 = Obstacle(7)

weapon1 = Weapon(6)
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
        if c == b' ':
            print(Fore.GREEN + '\033[1;1H' + "space pressed     ")
            # weapon1.fire(rover.get_gun_position()[0], rover.get_gun_position()[1])
            weapon1.fire(*rover.get_gun_position())
    weapon1.animate()
    mars_obstacles1.animate()
    # print(str(TermPos(1, 1)) + ' ' * 80)
    sleep(.08)
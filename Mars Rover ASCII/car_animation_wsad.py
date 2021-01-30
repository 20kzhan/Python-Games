import msvcrt
import os, sys
from random import randint
from time import sleep
from colorama import Fore, Back, Style, init

init()

boulder = [' O ',
           'OOO',
           ' O ']

car = ['Ö▓▓▓▓▓Ö',
       ' ▓▓░▓▓ ',
       ' ▓░Ö░▓ ',
       'Ö▓▓▓▓▓Ö']

car_row = 40
car_col = 20
screen_row_min = 3
screen_row_max = 60
screen_col_min = 2
screen_col_max = 100

boulder_row = 1
boulder_col = randint(1, 100)

# for windows OS 
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

def draw_boulder(row, col, color, clear=False):
    if clear:  # clears the car
        for n, line in enumerate(boulder):
            print(color + '\033[{};{}H'.format(row + n, col) + ' '*len(line))
    else:  # prints the car
        for n, line in enumerate(boulder):
            print(color + '\033[{};{}H'.format(row + n, col) + line)

def draw_car():
    for n, line in enumerate(car):
        print(Fore.RED + '\033[{};{}H'.format(car_row + n, car_col) + ' ' + line + ' ')
        print(Fore.RED + '\033[{};{}H'.format(car_row - 1, car_col) + ' '*(len(car[0])+1))
        print(Fore.RED + '\033[{};{}H'.format(car_row + len(car), car_col) + ' '*(len(car[0])+1))


draw_car()

boulder1_row, boulder1_col, boulder2_row, boulder2_col = 30, randint(1, screen_col_max), 20, randint(1, screen_col_max)

col_shift = 2
row_shift = 1
col_shift1 = 2
row_shift1 = 1
col_shift2 = 2
row_shift2 = 1

while True:
    if msvcrt.kbhit():
        c = msvcrt.getch()
        if c == b'\xe0':
            c = msvcrt.getch()
            if str(c) == "b'M'":
                if car_col <= screen_col_max:
                    car_col += 1
                    print(Fore.GREEN + '\033[1;1H' + 'right pressed')
                    draw_car()
            elif str(c) == "b'K'":
                if car_col >= screen_col_min:
                    car_col -= 1
                    print(Fore.GREEN + '\033[1;1H' + 'left pressed    ')
                    draw_car()
            elif str(c) == "b'H'":
                if car_row > screen_row_min:
                    car_row -= 1
                    print(Fore.GREEN + '\033[1;1H' + 'up pressed    ')
                    draw_car()
            elif str(c) == "b'P'":
                if car_row <= screen_row_max:
                    car_row += 1
                    print(Fore.GREEN + '\033[1;1H' + 'down pressed')
                    draw_car()

    # make the boulder move down
    boulder_row += row_shift
    boulder1_row += row_shift
    boulder2_row += row_shift

    # clear trailing O
    for n, line in enumerate(boulder):
        print(Fore.GREEN + '\033[{};{}H'.format(boulder_row + n - row_shift, boulder_col - col_shift) + ' ' * len(boulder[0]))
        print(Fore.GREEN + '\033[{};{}H'.format(boulder1_row + n - row_shift, boulder1_col - col_shift1) + ' ' * len(boulder[0]))
        print(Fore.GREEN + '\033[{};{}H'.format(boulder2_row + n - row_shift, boulder2_col - col_shift2) + ' ' * len(boulder[0]))

    # draw boulder1
    draw_boulder(boulder_row, boulder_col, Fore.RED)
    # draw boulder2
    draw_boulder(boulder1_row, boulder1_col, Fore.GREEN)
    # draw boulder3
    draw_boulder(boulder2_row, boulder2_col, Fore.BLUE)

    # reset the row and the column of the boulder
    if boulder_row > screen_row_max + len(boulder):
        draw_boulder(boulder_row, boulder_col, Fore.GREEN, clear=True)
        boulder_row = 1
        boulder_col = randint(1, screen_col_max)
    if boulder_col > screen_col_max or boulder_col < screen_col_min:
        col_shift *= -1

    if boulder1_row > screen_row_max + len(boulder):
        draw_boulder(boulder1_row, boulder1_col, Fore.GREEN, clear=True)
        boulder1_row = 1
        boulder1_col = randint(1, screen_col_max)
    if boulder1_col > screen_col_max or boulder1_col < screen_col_min:
        col_shift1 *= -1

    if boulder2_row > screen_row_max + len(boulder):
        draw_boulder(boulder2_row, boulder2_col, Fore.GREEN, clear=True)
        boulder2_row = 1
        boulder2_col = randint(1, screen_col_max)
    if boulder2_col > screen_col_max or boulder2_col < screen_col_min:
        col_shift2 *= -1

    sleep(0.02)
    boulder_col += col_shift
    boulder1_col += col_shift1
    boulder2_col += col_shift2

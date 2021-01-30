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

col_shift = 2
row_shift = 1
col_shift1 = 2
row_shift1 = 1
col_shift2 = 2
row_shift2 = 1

boulders_info = [  # [boulder_row, boulder_col, row_shift, col_shift, color]
    [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.RED],
    [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.GREEN],
    [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.BLUE]
]

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
    for n, line in enumerate(boulder):
        print('\033[{};{}H'.format(row + n - row_shift, col - col_shift) + ' ' * len(line))

    if clear:  # clears the car
        for n, line in enumerate(boulder):
            print(color + '\033[{};{}H'.format(row + n, col) + ' ' * len(line))
    else:  # prints the car
        for n, line in enumerate(boulder):
            print(color + '\033[{};{}H'.format(row + n, col) + line)


def draw_car():
    for n, line in enumerate(car):
        print(Fore.RED + '\033[{};{}H'.format(car_row + n, car_col) + ' ' + line + ' ')
        print(Fore.RED + '\033[{};{}H'.format(car_row - 1, car_col) + ' ' * (len(car[0]) + 1))
        print(Fore.RED + '\033[{};{}H'.format(car_row + len(car), car_col) + ' ' * (len(car[0]) + 1))


draw_car()

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
    '''
    boulders_info = [  # [boulder_row, boulder_col, row_shift, col_shift, color]
        [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.RED],
        [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.GREEN],
        [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.BLUE]
    ]
    '''
    # make the boulder move down
    for each_boulder in boulders_info:
        each_boulder[0] += each_boulder[2]
        each_boulder[1] += each_boulder[3]
        draw_boulder(each_boulder[0], each_boulder[1], each_boulder[4])

        # clear trailing O
        for n, line in enumerate(boulder):
            print(Fore.GREEN + '\033[{};{}H'.format(each_boulder[0] + n - each_boulder[2], each_boulder[1] - each_boulder[3]) + ' ' * len(
                boulder[0]))

        # reset the row and the column of the boulder
        if each_boulder[0] > screen_row_max + len(boulder):
            draw_boulder(each_boulder[0], each_boulder[1], each_boulder[4], clear=True)
            each_boulder[0] = randint(1, 5)
            each_boulder[1] = randint(screen_col_min, screen_col_max)
        if each_boulder[1] > screen_col_max or each_boulder[1] < screen_col_min:
            each_boulder[3] *= -1

        sleep(0.02)

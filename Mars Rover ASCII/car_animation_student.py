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

boulder_row = 1
boulder_col = randint(1, 100)

boulder_row1, boulder_col1, boulder_row2, boulder_col2 = 1, randint(1, screen_)

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

def draw_car():
    for n, line in enumerate(car):
        print(Fore.RED + '\033[{};{}H'.format(car_row + n, car_col) + ' ' + line + ' ')

draw_car()

count=0
while True:
    if msvcrt.kbhit():
        c = msvcrt.getch()
        if c == b'\xe0':
            c = msvcrt.getch()
            if str(c) == "b'M'":
                if car_col <= 100:
                    car_col += 1
                    print(Fore.GREEN + '\033[1;1H' + 'right pressed')
                    draw_car()
            elif str(c) == "b'K'":
                if car_col >= 2:
                    car_col -= 1
                    print(Fore.GREEN + '\033[1;1H' + 'left pressed ')
                    draw_car()

    # make the boulder move down
    if count % 2== 0:
        boulder_row += 1

        for n, line in enumerate(boulder):
            # clear trailing O
            print(Fore.GREEN + '\033[{};{}H'.format(boulder_row - 1, boulder_col) + ' '*len(boulder[0]))
            # make boulder disappear behind car
            if boulder_row < car_row + 5:
                print(Fore.GREEN + '\033[{};{}H'.format(boulder_row + n, boulder_col) + line)
            else:
                # clear rock after it's behind car
                print(Fore.RED + '\033[{};{}H'.format(boulder_row + n, boulder_col) + '   ')

        # reset the row and the column of the boulder
        if boulder_row >= car_row + 5 + len(boulder):
            boulder_row = 1
            boulder_col = randint(1, 100)
    sleep(0.02)
    count+=1

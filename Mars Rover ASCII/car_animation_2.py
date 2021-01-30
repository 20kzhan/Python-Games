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

car_laser = '|'

game_menu = [' Welcome to the Mars Rover',
             '                          ',
             ' Config Options:          ',
             '                          ',
             ' 1. Set total boulders    ',
             ' 2. Set max missles       ',
             ' 3. Set total tunnel width',
             ' 4. Start game            ',
             ' 5. Quit                  ',]

car_row = 40
car_col = 20
screen_row_min = 3
screen_row_max = 60
screen_col_min = 4
screen_col_max = 100

col_shift = 2
row_shift = 1
col_shift1 = 2
row_shift1 = 1
col_shift2 = 2
row_shift2 = 1

total_boulders = 5
max_lasers = 3
boulder_maps = {}

tunnel_width = 30
tunnel_position = randint(20, 80)

boulders_info = [  # [boulder_row, boulder_col, row_shift, col_shift, tunnel_pos,color]
    # [randint(1, 5), randint(tunnel_position, tunnel_position+tunnel_width), 1, 2, Fore.RED],
    # [randint(1, 5), randint(tunnel_position, tunnel_position+tunnel_width), 1, 2, Fore.GREEN],
    # [randint(1, 5), randint(tunnel_position, tunnel_position+tunnel_width), 1, 2, Fore.BLUE]
]

lasers_info = [ # [laser_row, laser_col]
]

boulder_colors = [Fore.RED, Fore.GREEN, Fore.BLUE]

count = 0
laser_act = False

laser_row = car_row - 2
laser_col = car_col + (len(car[0]) // 2) + 1

paused = True

game_menu_enabled = True

score = 0

for i in range(total_boulders):
    tunnel_position = randint(20, 80)
    boulders_info.append(
        [randint(1, 5), randint(tunnel_position + 3, tunnel_position + tunnel_width - 3), 1, 2, tunnel_position,
         boulder_colors[randint(0, len(boulder_colors) - 1)]])

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


def get_map(row, col, object):
    output = {}
    obj_col = []
    for i in range(len(object)):
        for y in range(len(object[i])):
            if ' ' != object[i][y]:
                obj_col.append(col + y)
        output[row + i] = obj_col
        obj_col = []
    return output


def draw_laser(row, col, laser):
    print(Fore.WHITE + '\033[{};{}H'.format(row, col) + laser)
    print(Fore.WHITE + '\033[{};{}H'.format(row + 1, col) + ' ')

def common_keys(d1, d2):
    set1 = set(d1.keys())
    set2 = set(d2.keys())
    com_keys = set1.intersection(set2)
    return com_keys

def common_values(d1, d2):
    set1 = set(d1.keys())
    set2 = set(d2.keys())
    com_keys = set1.intersection(set2)
    com_values = []

    for key in com_keys:
        val1_set = set(d1[key])
        val2_set = set(d2[key])
        com_values += val1_set.intersection(val2_set)

    return com_values

for n, line in enumerate(game_menu):
    print(Fore.WHITE + '\033[{};{}H'.format(2 + n, 2) + line)

while True:
    if msvcrt.kbhit():
        c = msvcrt.getch()
        if c == b'\xe0':
            c = msvcrt.getch()
            if str(c) == "b'M'":
                if car_col <= screen_col_max:
                    if not paused:
                        car_col += 1
                        print(Fore.GREEN + '\033[1;1H' + 'right pressed')
                        draw_car()
                        car_map = get_map(car_row, car_col, car)
            elif str(c) == "b'K'":
                if car_col >= screen_col_min:
                    if not paused:
                        car_col -= 1
                        print(Fore.GREEN + '\033[1;1H' + 'left pressed    ')
                        draw_car()
                        car_map = get_map(car_row, car_col, car)
            elif str(c) == "b'H'":
                if car_row > screen_row_min:
                    if not paused:
                        car_row -= 1
                        print(Fore.GREEN + '\033[1;1H' + 'up pressed    ')
                        draw_car()
                        car_map = get_map(car_row, car_col, car)
            elif str(c) == "b'P'":
                if car_row <= screen_row_max:
                    if not paused:
                        car_row += 1
                        print(Fore.GREEN + '\033[1;1H' + 'down pressed')
                        draw_car()
                        car_map = get_map(car_row, car_col, car)
        elif c == b' ':
            if not laser_act:
                if not paused:
                    laser_act = True
                    print(Fore.GREEN + '\033[1;1H' + 'space pressed')
            if len(lasers_info) < int(max_lasers):
                if not paused:
                    lasers_info.append([car_row - 2, car_col + (len(car[0]) // 2) + 1])
        elif c == b'p':
            if paused:
                paused = False
            else:
                paused = True

        if game_menu_enabled:
            for n, line in enumerate(game_menu):
                print(Fore.WHITE + line)
                if c == b'1':
                    print(Fore.WHITE + ' ')
                    total_boulders = input(Fore.WHITE + ' Enter total boulders: ')
                    print(Fore.WHITE + ' Total number of boulders set to: ' + total_boulders)
                elif c == b'2':
                    print(Fore.WHITE + ' ')
                    max_lasers = input(Fore.WHITE + ' Enter max lasers: ')
                    print(Fore.WHITE + ' Max lasers set: ' + max_lasers)
                elif c == b'3':
                    print(Fore.WHITE + ' ')
                    tunnel_width = input(Fore.WHITE + ' Enter tunnel width (type "random" to make tunnel_width random): ')
                    if tunnel_width == 'random':
                        tunnel_width = randint(20, 50)
                    print(Fore.WHITE + ' Tunnel width set: ' + str(tunnel_width))
                elif c == b'4':
                    os.system('cls')
                    game_menu_enabled = False
                    paused = False
                    draw_car()
                    break
                elif c == b'5':
                    os.system('cls')
                    exit()
                c = ''

    '''
    boulders_info = [  # [boulder_row, boulder_col, row_shift, col_shift, color]
        [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.RED],
        [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.GREEN],
        [randint(1, 5), randint(screen_col_min, screen_col_max), 1, 2, Fore.BLUE]
    ]
    '''
    if count % 5 == 0:
        if not paused and not game_menu_enabled:
            # make the boulder move down
            for each_boulder in boulders_info:
                each_boulder[0] += each_boulder[2]
                each_boulder[1] += each_boulder[3]

                # clear trailing O
                for n, line in enumerate(boulder):
                    print(Fore.GREEN + '\033[{};{}H'.format(each_boulder[0] + n - each_boulder[2],
                                                            each_boulder[1] - each_boulder[3]) + ' ' * len(
                        boulder[0]))

                draw_boulder(each_boulder[0], each_boulder[1], each_boulder[5])

                # reset the row and the column of the boulder
                if each_boulder[0] > screen_row_max + len(boulder):
                    draw_boulder(each_boulder[0], each_boulder[1], each_boulder[5], clear=True)
                    each_boulder[0] = randint(1, 5)
                    each_boulder[1] = randint(tunnel_width, tunnel_position + tunnel_width)
                    each_boulder[5] = boulder_colors[randint(0, len(boulder_colors) - 1)]
                    each_boulder[4] = randint(20 + 3, 20 + tunnel_width - 3)
                if each_boulder[1] > tunnel_position + tunnel_width or each_boulder[1] < tunnel_position:
                    each_boulder[3] *= -1

                boulder_maps = get_map(each_boulder[0], each_boulder[1], boulder)
                car_map = get_map(car_row, car_col, car)
                laser_map = get_map(laser_row, laser_col, car_laser)
                row_collision = set(boulder_maps.keys()).intersection(set(car_map.keys()))

                print(Fore.GREEN + '\033[3;5H' + str(boulder_maps) + '    ')
                print(Fore.GREEN + '\033[4;5H' + str(car_map) + '    ')
                print(Fore.GREEN + '\033[5;5H' + str(laser_map) + '    ')

                for i in range(len(car) - 3):
                    if boulder_maps.get(each_boulder[0]) == car_map.get(car_row)[i]:
                        if boulder_maps.get(each_boulder[1]) == car_map.get(car_col)[i]:
                            print(Fore.GREEN + '\033[3;5H' + 'test')
            remove_laser = -1
            for n, each_laser in enumerate(lasers_info):
                if each_laser[0] <= 2:
                    print(Fore.WHITE + '\033[{};{}H'.format(each_laser[0], each_laser[1]) + ' ')
                    each_laser[1] = car_col + (len(car[0]) // 2) + 1
                    each_laser[0] = car_row - 2
                    remove_laser = n
                else:
                    each_laser[0] -= 1
                    draw_laser(each_laser[0], each_laser[1], car_laser)
            if remove_laser != -1:
                lasers_info.pop(remove_laser)

            if common_keys(boulder_maps, car_map):
                if common_values(boulder_maps, car_map):
                    print(Fore.RED + '\033[50;50H' + 'Game Over!')
                    while True:
                        sleep(1)

            print(Fore.RED + '\033[50;1H' + 'Score:' + str(score))
            boulder_maps = {}

    count += 1
    sleep(0.025)

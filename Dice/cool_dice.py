import msvcrt
from time import sleep
from colorama import Fore, Style, init
from random import randint, shuffle
import os

DICE_IMG = [  # "---------\n",
    ["|       |\n",
     "|   O   |\n",
     "|       |\n"],
    ["| O     |\n",
     "|       |\n",
     "|     O |\n"],
    ["| O     |\n",
     "|   O   |\n",
     "|     O |\n"],
    ["| O   O |\n",
     "|       |\n",
     "| O   O |\n"],
    ["| O   O |\n",
     "|   O   |\n",
     "| O   O |\n"],
    ["| O   O |\n",
     "| O   O |\n",
     "| O   O |\n"]]

"""
0 1 1
0 0 1
0 1 1
"""
# 5 down and 4 further

init()

colors = [Fore.BLUE, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTCYAN_EX,
          Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX]

dice_colors = {1: colors[randint(0, len(colors) - 1)],
               2: colors[randint(0, len(colors) - 1)],
               3: colors[randint(0, len(colors) - 1)],
               4: colors[randint(0, len(colors) - 1)],
               5: colors[randint(0, len(colors) - 1)],
               6: colors[randint(0, len(colors) - 1)]}

dice_values = [1, 2, 3, 4, 5, 6]
shuffle(dice_values)

dice = {'color1': colors[randint(0, len(colors) - 1)],
         'value1': dice_values.pop(),
         'row1': 5,
         'col1': 10,
         'color2': colors[randint(0, len(colors) - 1)],
         'value2': dice_values.pop(),
         'row2': 12,
         'col2': 10,
         'color3': colors[randint(0, len(colors) - 1)],
         'value3': dice_values.pop(),
         'row3': 5,
         'col3': 30,
         'color4': colors[randint(0, len(colors) - 1)],
         'value4': dice_values.pop(),
         'row4': 12,
         'col4': 30}

# clear the screen
if os.name == "nt":
    os.system("cls")
else:
    print(f"\033[2J ")


def reroll_dice():
    global dice_values
    dice_values = [1, 2, 3, 4, 5, 6]
    shuffle(dice_values)
    for i in range(1, 5):
        dice['value' + str(i)] = dice_values.pop()
        dice['color' + str(i)] = colors[randint(0, len(colors) - 1)]


def print_dice(DICE_IMG):
    dice_offset = 0
    offset = 0
    # for i, each_row in enumerate(DICE_IMG):
    #     for x in range(len(each_row)):
    #         print(dice_colors[i + 1] + '\033[{};{}H'.format(5 + offset + dice_offset, 10) + each_row[x], end='')
    #         offset += 1
    for i in range(1, 5):
        for x in range(3):
            print(dice['color' + str(i)] + '\033[{};{}H'.format(dice['row' + str(i)] + offset, dice['col' + str(i)]) +
                  DICE_IMG[dice['value' + str(i)]-1][x], end='')
            offset += 1


if __name__ == "__main__":
    print(Fore.RED + '\033[1;1H' + 'Press R to reroll dice and Hold R to have an epileptic seizure')
    print_dice(DICE_IMG)
    while True:
        if msvcrt.kbhit():
            c = msvcrt.getch()
            if c == b'r':
                os.system('cls')
                print(Fore.RED + '\033[3;1H' + 'Press R to reroll dice and Hold R to have an epileptic seizure')
                reroll_dice()
                print_dice(DICE_IMG)

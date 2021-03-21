import msvcrt
from time import sleep
from colorama import Fore, Style, init
from random import *
import os

class Dice:
    def __init__(self, row, col):
        self._colorchoices = [Fore.BLUE, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTCYAN_EX,
          Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX]
        self._color = choices(self._colorchoices)
        self._row = row
        self._col = col
        self._value = randint(1, 6)

    def roll(self):
        self._value = randint(1, 6)

    def set_color(self):
        self._color = choices(self._colorchoices)

    def dump_properties(self):
        color = str(self._color)

        print("Here are the dice properties: ")
        print(self._color[0] + 'the color of this text')
        print(Fore.WHITE + str(self._row) + ', ' + str(self._col))
        print(Fore.WHITE + str(self._value) + '\n')

    def print_dice(self):
        offset = 0
        # for i in range(1, 5):
        for x in range(3):
            print(self._color[0] + '\033[{};{}H'.format(self._row + offset, self._col) +
                DICE_IMG[self._value-1][x], end='')
            offset += 1

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
shuffle(colors)

dice_values = list(range(1,7))
shuffle(dice_values)

dice = {'color1': colors.pop(),
         'value1': dice_values.pop(),
         'row1': 5,
         'col1': 10,
         'color2': colors.pop(),
         'value2': dice_values.pop(),
         'row2': 12,
         'col2': 10,
         'color3': colors.pop(),
         'value3': dice_values.pop(),
         'row3': 5,
         'col3': 30,
         'color4': colors.pop(),
         'value4': dice_values.pop(),
         'row4': 12,
         'col4': 30}

# clear the screen
if os.name == "nt":
    os.system("cls")
else:
    print(f"\033[2J ")


def reroll_dice():
    global dice_values, colors
    dice_values = [1, 2, 3, 4, 5, 6]
    shuffle(dice_values)
    colors = [Fore.BLUE, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA,
              Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTCYAN_EX,
              Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX]
    shuffle(colors)
    for i in range(1, 5):
        dice['value' + str(i)] = dice_values.pop()
        dice['color' + str(i)] = colors.pop()


def print_dice(DICE_IMG):
    offset = 0
    for i in range(1, 5):
        for x in range(3):
            print(dice['color' + str(i)] + '\033[{};{}H'.format(dice['row' + str(i)] + offset, dice['col' + str(i)]) +
                  DICE_IMG[dice['value' + str(i)]-1][x], end='')
            offset += 1


if __name__ == "__main__":
    print('Scroll to the bottom of the code to find how to change the number of dies', end='')
    sleep(4)
    os.system('cls')
    dice_list = []
    # 4 Dice
    for n, pos in [(5, 10), (12, 10), (5, 30), (12, 30)]:
        dice_list.append(Dice(row=n, col=pos))

    # 8 Dice
    # for n, pos in [(5, 10), (12, 10), (5, 30), (12, 30), (5, 50), (12, 50), (5, 70), (12, 70)]:
    #     dice_list.append(Dice(row=n, col=pos))

    while True:
        for dice in dice_list:
            dice.roll()
            dice.set_color()
            dice.print_dice()
            # dice.dump_properties()

        sleep(1)
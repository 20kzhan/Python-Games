import pygame
from random import randint

pygame.init()


class Tile2048:
    COLORS = {0: (205, 193, 180),
              2: (238, 228, 218),
              4: (237, 224, 200),
              8: (242, 177, 121),
              16: (245, 149, 99),
              32: (246, 124, 96),
              64: (246, 94, 59),
              128: (237, 207, 115),
              256: (237, 204, 98),
              512: (237, 200, 80),
              1024: (237, 197, 63),
              2048: (237, 194, 45)}

    TILE_SIZE = 100

    FONT = pygame.font.SysFont('Clear Sans', TILE_SIZE // 100 * 50)

    '''
    This class is responsible for the display
    '''

    def __init__(self, value, pos, display):
        '''
        initializes a tile based on its value
        automatically figures out font size and color
        '''
        # calling the value.setter becuase need to set the tile colorNone
        self._x, self._y = pos
        self._display = display
        self.value = value

    #def text_center(self, row, col, size):  # size[0] is the width, size[1] is the height
    def _text_center(self, position, size):
        # this function will return the x, y position to center the text on cell row, col
        # pass
        x_res, y_res = int(__class__.TILE_SIZE / 2) + position[0], int(__class__.TILE_SIZE / 2) + position[1]
        x_res -= size[0] // 2
        y_res -= size[1] // 2
        return x_res, y_res

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._update_tile_color()
        self._update_text_size()
        self._rasterize()

    @property
    def color(self):
        return self._color

    def _update_tile_color(self):
        # this method will change self._tile_color depending on the value
        if self.value <= max(__class__.COLORS):
            self._tile_color = __class__.COLORS[self.value]
        else:
            self._tile_color = __class__.COLORS[max(__class__.COLORS)]

    def _update_text_size(self):
        # needed to support different font size depending on
        # value
        # this method will change self._text_font
        self._text_font = __class__.FONT

    def _rasterize(self):
        # screen is pygame display (screen)
        # position is a tuple of (x, y) cartesian position within
        # the screen
        # will use self.value, self._tile_color, self._text_font to display the
        # tile on the screen (is passed in as a pygame display) at position
        pygame.draw.rect(self._display, self._tile_color,
                         (self._x, self._y, __class__.TILE_SIZE, __class__.TILE_SIZE))

        if self.value == 2 or self.value == 4:
            text_surface = self._text_font.render(str(self.value), False, (119, 110, 101))
            self._display.blit(text_surface, self._text_center((self._x, self._y), text_surface.get_size()))

        elif self.value != 0:
            text_surface = self._text_font.render(str(self.value), False, (255, 255, 255))
            self._display.blit(text_surface, self._text_center((self._x, self._y), text_surface.get_size()))


class Board2048:
    '''
    This class manages the entire 4x4 2048 board.  It maintains the values in the
    board as well as the display of the board
    '''
    BKGROUND_COLOR = (255, 255, 255)  # set board boackground color to white
    TILE_OFFSET = Tile2048.TILE_SIZE // 10
    DISPLAY_OFFSET = 50
    NCOLS = 4
    NROWS = 4

    def __init__(self,
                 tile_size=Tile2048.TILE_SIZE,
                 tile_offset=TILE_OFFSET,
                 display_offest=DISPLAY_OFFSET):
        # let's compute the board size using tile_size and tile_offset
        self.board_width = (4 * tile_size) + (5 * tile_offset)
        self.board = []
        self.reset()

    def reset(self):
        # resets the game board: clears all cells and seed the first two random cells
        self.board = [[0]*4]*4
        self._place_new_value()
        self._place_new_value()

    def _rotate_board(self):
        board_col = len(self.board[0])
        new = []
        for i in range(board_col):
            new.append([0] * board_col)
        for col in range(len(self.board[0])):
            for row in range(len(self.board)):
                new[row][col] = self.board[col][row]
        return new


    def _place_new_value(self):
        value = 0
        if randint(0, 9) != 9:
            value = 2
        else:
            value = 4
        while True:
            x = randint(0, len(self.board[0]) - 1)
            y = randint(0, len(self.board) - 1)
            if self.board[y][x] == 0:
                self.board[y][x] = value
                break

    def _shift_cells(self, cell_list):
        # always shifts cell_list to the left (towards 0 index)
        # there are 4 elements, may have element with 0 value (
        # empty cells)
        # 1. remove the 0 value cells (clear the spaces)
        # 2. shift cell_list to the left
        #       i. if len(cell_list)>1 then start with the 0 element and
        #           check if neighbors are the same and combine
        #       ii. move on to the next elements to check for neighbors
        #           to combine.  At most, there are only two combinations
        # 3. add in the correct number of 0 (empty spaces) to the right
        #   to make the final length = 4
        # returns True/False if cells shifted
        orig_list = cell_list.copy()
        while 0 in cell_list:
            cell_list.remove(0)

        i = 0
        while i + 1 < len(cell_list):
            if cell_list[i] == cell_list[i + 1]:
                cell_list[i] *= 2
                cell_list.pop(i + 1)
            i += 1

        cell_list += [0] * (4 - len(cell_list))
        return not orig_list == cell_list

    def shift_up(self):
        for i in range(3):
            self.board = zip(*self.board[::-1])
        for i in range(__class__.NCOLS):
            self.board[i] = self._shift_cells(self.board[i])
        self.board = zip(*self.board[::-1])

    def shift_right(self):
        for i in range(2):
            self.board = zip(*self.board[::-1])
        for i in range(__class__.NCOLS):
            self.board[i] = self._shift_cells(self.board[i])
        for i in range(2):
            self.board = zip(*self.board[::-1])

    def shift_down(self):
        self.board = zip(*self.board[::-1])
        for i in range(__class__.NCOLS):
            self.board[i] = self._shift_cells(self.board[i])
        for i in range(3):
            self.board = zip(*self.board[::-1])

    def shift_left(self):
        for i in range(__class__.NCOLS):
            self.board[i] = self._shift_cells(self.board[i])


class Game2048:
    '''
    This class manages the playing of the game
    Creates
        1. Board2048
        2. pygame initialization
    Exposes play() method which will return when the game ends
    Can restart() after play() returns
    '''

    pass


def main():
    import time
    display = pygame.display.set_mode((500, 300))
    for value in [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
        tile1 = Tile2048(value, (100, 50), display)
        tile2 = Tile2048(value * 2, (220, 50), display)

        tile3 = Tile2048(value * 2, (100, 150 + 20), display)
        tile4 = Tile2048(value, (220, 150 + 20), display)
        pygame.display.update()
        time.sleep(1.5)
    pygame.quit()


if __name__ == "__main__":
    main()
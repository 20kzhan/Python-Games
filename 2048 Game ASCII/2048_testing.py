from game_2048 import *



# test cases for game_over
# make sure your code can pass these test cases

gb = [[0, 2, 2, 2],
      [2, 0, 2, 2],
      [2, 2, 0, 2],
      [2, 2, 2, 0]]

shifted_board = shift_board_down(gb)

for each_row in shifted_board:
    print(each_row)

print('\n')

gb = [[0, 2, 2, 2],
      [2, 0, 2, 2],
      [2, 2, 0, 2],
      [2, 2, 2, 0]]

shifted_board = shift_board_up(gb)

for each_row in shifted_board:
    print(each_row)

print('\n')

gb = [[0, 2, 4, 8],
      [2, 4, 8, 2],
      [4, 8, 2, 4],
      [8, 2, 4, 2]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')
print('\n')

gb = [[4, 2, 4, 8],
      [2, 0, 8, 2],
      [4, 8, 2, 4],
      [8, 2, 4, 2]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

gb = [[4, 2, 4, 8],
      [2, 4, 8, 2],
      [4, 8, 0, 4],
      [8, 2, 4, 2]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

gb = [[4, 2, 4, 8],
      [2, 4, 8, 2],
      [4, 8, 2, 4],
      [8, 2, 4, 0]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

gb = [[0, 2, 4, 8],
      [2, 4, 8, 2],
      [4, 8, 2, 4],
      [8, 2, 4, 0]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

gb = [[0, 2, 4, 8],
      [2, 4, 0, 2],
      [4, 8, 2, 4],
      [8, 2, 4, 0]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

gb = [[0, 2, 4, 8],
      [2, 4, 0, 2],
      [4, 0, 2, 4],
      [8, 2, 4, 0]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

gb = [[4, 2, 4, 8],
      [2, 4, 8, 2],
      [4, 8, 2, 4],
      [8, 2, 4, 2]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

gb = [[8, 2, 4, 8],
      [2, 4, 16, 2],
      [4, 32, 2, 4],
      [8, 2, 4, 64]]

for each_row in gb:
    print(each_row)
print("After: ")
for each_row in shift_board_left(gb):
    print(each_row)
print('\n')

# test cases for shift_left
# make sure your code can pass these test cases

sl = [0] * 4
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 0, 0, 0]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [0, 2, 0, 0]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [0, 0, 0, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [0, 2, 0, 4]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [0, 2, 4, 8]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 2, 0, 0]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 0, 2, 0]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 0, 0, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 2, 0, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 0, 2, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 2, 2, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [4, 2, 4, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [0, 2, 2, 0]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [0, 2, 2, 4]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [8, 4, 2, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 2, 8, 4]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [8, 4, 0, 4]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 16, 4, 4]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [4, 16, 4, 4]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 2, 16, 8]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 4, 16, 16]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 2, 0, 32]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 2, 4, 32]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [0, 8, 8, 2]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 8, 8, 0]
print(f'original list: {sl}')
print(shift(sl, right=False))

sl = [2, 0, 8, 8]
print(f'original list: {sl}')
print(shift(sl, right=False))


m_even_row_odd_col = \
    [['i', 'm', 'x', 't', 'l', 'i'],
     ['i', 'c', 'n', 'a', 'm', 'q'],
     ['f', 'y', 'o', 'e', 'e', 's'],
     ['d', 'l', 'z', 't', 'u', 'g'],
     ['c', ' ', 'k', ' ', 'y', ' '],
     ['z', 'v', 'l', 'n', 'i', 'r'],
     ['q', 'f', 'w', 'c', 'w', 'b'],
     ['p', 'f', 'y', 'n', 'u', 'd'],
     ['z', 'a', 'c', 'o', 'v', 'l'],
     ['g', 'b', 't', 'm', 'o', 'l'],
     ['e', 'v', 'y', 'l', 'e', 'u'],
     ['l', 'f', 'y', 'p', 'j', 'm'],
     ['j', 'o', 'n', 'o', 'o', 'e'],
     ['x', 'j', 'k', 'x', 'n', 'j'],
     ['q', 'r', 's', 'r', 'y', ' '],
     ['s', 'w', 'j', 'w', 'k', 'k'],
     ['h', 'i', 'j', ' ', 'u', ' '],
     ['i', 'r', 'h', 's', 'p', 'm']]

m_even_col_odd_row = \
    [['l', 'x', 'h', 'v', 'f', 'q'],
     ['m', 'c', 'y', 'g', ' ', 's'],
     ['x', 'd', 'z', 'm', 'x', 'a'],
     ['f', 'k', 'a', 'd', 'v', 't'],
     ['l', 'd', 'f', 'm', 'g', 'y'],
     ['o', 's', 'r', 's', 'i', 'o'],
     ['g', 'u', 'w', 'u', 's', 'j'],
     ['t', 'o', 'e', 'z', ' ', 'q'],
     ['p', 's', 't', 'n', 'q', 'l'],
     ['c', 'y', 'o', 'i', 'l', 'q'],
     ['m', 'q', 'j', 'g', 'j', 'r'],
     ['o', 'r', 'r', 'h', ' ', 'f'],
     ['d', 'z', 'v', 'z', 'a', 'y'],
     ['i', 'd', 's', 'v', ' ', 'c'],
     ['g', 'r', 'e', 'w', 'm', 'f'],
     ['b', 'h', 'l', 'i', 'u', 'g'],
     ['q', 'l', 'l', 'u', 's', 'k'],
     ['e', 'l', ' ', 'a', ' ', 'd']]

secret_message = ''
row_message = []

for col in range(1, len(m_even_row_odd_col[0]), 2):
    for row in range(0, len(m_even_row_odd_col), 2):
        secret_message += str(m_even_row_odd_col[row][col])
    row_message.append(secret_message)
    secret_message = ''

# print(secret_message)
print(row_message)

secret_message = ''
row_message = []

for row in range(1, len(m_even_col_odd_row), 2):
    for col in range(0, len(m_even_col_odd_row[0]), 2):
        secret_message += str(m_even_col_odd_row[row][col])
    row_message.append(secret_message)
    secret_message = ''

# print(secret_message)
print(row_message)

secret_message = ''
row_message = []

for row in range(1, len(m_even_col_odd_row)):
    if row % 2 == 1:
        for col in range(0, len(m_even_col_odd_row[0])):
            if col % 2 == 0:
                secret_message += str(m_even_col_odd_row[row][col])
        row_message.append(secret_message)
        secret_message = ''

# print(secret_message)
print(row_message)
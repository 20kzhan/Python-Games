def print_one_ring(alist):
    result = []
    for i in range(len(alist[0])):
        result.append(alist[0][i])
    for i in range(len(alist)):
        result.append(alist[i][len(alist)-1])
    for i in range(len(alist[0])-1, -1, -1):
        result.append(alist[len(alist)-1][i])
    for i in range(len(alist)-1, -1, -1):
        result.append(alist[i][0])
    return result

def print_perfect_ring(alist):
    result = []
    x = 0
    for i in range(x, len(alist[0]) - x):
        result.append(alist[x][i])
    for i in range(x + 1, len(alist) - x):
        result.append(alist[i][len(alist) - 1 - x])
    for i in range(len(alist[0]) - 2 - x, x, -1):
        result.append(alist[len(alist) - 1 - x][i])
    for i in range(len(alist) - (1 + x), x, -1):
        result.append(alist[i][x])
    return result


def print_circular_rings(alist, num_rings):
    result = []
    for x in range(num_rings):
        for i in range(x, len(alist[0])-x):
            result.append(alist[x][i])
        for i in range(x+1, len(alist)-x):
            result.append(alist[i][len(alist)-1-x])
        for i in range(len(alist[0])-2-x, x, -1):
            result.append(alist[len(alist)-1-x][i])
        for i in range(len(alist)-(1+x), x, -1):
            result.append(alist[i][x])

    return result

def create_2D_list(num_rows, num_cols):
    return [[num_cols*row + col for col in range(num_cols)] for row in
            range(num_rows)]

matrix = create_2D_list(10, 10)

print(print_one_ring(matrix))
print(print_perfect_ring(matrix))
print(print_circular_rings(matrix, 2))


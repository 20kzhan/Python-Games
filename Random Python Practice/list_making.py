def list_pattern(height, width):
    pattern = []
    temp_pattern = []
    # for i in range(height):
    #     for x in range(width):
    #         temp_pattern.append(0)
    #     pattern.append(temp_pattern)
    #     temp_pattern = []
    for x in range(height):
        for i in range(0, width*height, height):
            temp_pattern.append(i+x)
        pattern.append(temp_pattern)
        temp_pattern = []
    # for i in range(height):
    #     for x in range(i, width+i):
    #         temp_pattern.append(x)
    #     pattern.append(temp_pattern)
    #     temp_pattern = []
    # return pattern
    for i in range(len(pattern)):
        print(pattern[i])

list_pattern(10, 8)

def list_pattern2(width, height):
    pattern = []
    temp_pattern = []

    for i in range(height):
        for x in range(width):
            temp_pattern.append(0)
        pattern.append(temp_pattern)
        temp_pattern = []

    # pattern[0][width - 1] = 1
    # pattern[0][width - 2] = 1
    # pattern[1][width - 1] = 1
    # pattern[-1][0] = 2
    # pattern[-1][1] = 2
    # pattern[-2][0] = 2

    # for x in range(0, height):
    #     for i in range(0+x, width):
    #         pattern[i][i-x] = 1

    for i in range(height):
        for x in range(width):
            if i == x:
                pattern[i][x] = 0
            elif i < x:
                pattern[i][x] = 1
            elif i > x:
                pattern[i][x] = 2

    for i in range(len(pattern)):
        print(pattern[i])

list_pattern2(5, 5)

m = [[0,   1,  2,  3,  4],
     [5,   6,  7,  8,  9],
     [10, 11, 12, 13, 14],
     [15, 16, 17, 18, 19]]

def list_pattern3(alist):
    for col in range(len(alist[0])):
        # col = 0
        #     for row in range(len(alist)-1, -1, -1):
        if col % 2 == 0:
            for row in range(len(alist)):
                print(alist[row][col], end=', ')
        else:
            for row in range(len(alist) - 1, -1, -1):
                print(alist[row][col], end=', ')

list_pattern3(m)


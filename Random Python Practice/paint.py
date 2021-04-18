def total_paint(building_map):
    paint = 0
    col = len(building_map[0])
    row = len(building_map)
    paint += row * col
    # paint += building_map[0][0] * 2
    # paint += 1
    #
    # print(paint)
    #
    # paint += building_map[0][1] - building_map[0][0]
    # paint += building_map[0][1] * 2
    # paint += 1
    #
    # print(paint)
    #
    # paint += building_map[1][0] - building_map[0][0]
    # paint += building_map[1][0] * 2
    # paint += 1
    #
    # print(paint)
    #
    # paint += building_map[1][1] - building_map[0][1]
    # paint += building_map[1][1] - building_map[1][0]
    # paint += building_map[1][1] * 2
    # paint +=

    for i in range(row):
        for x in range(col):
            if x == 0:
                paint += abs(building_map[i][x])
            else:
                paint += abs(building_map[i][x] - building_map[i][x - 1])
                if x == col - 1:
                    paint += abs(building_map[i][x])

    for x in range(col):
        for i in range(row):
            if i == 0:
                paint += abs(building_map[i][x])
            else:
                paint += abs(building_map[i][x] - building_map[i - 1][x])
                if i == row - 1:
                    paint += abs(building_map[i][x])

    return paint


print(total_paint([[2, 2, 2],
                   [1, 2, 2],
                   [2, 2, 2]]))

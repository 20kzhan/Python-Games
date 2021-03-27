def total_fence(land_map):
    perimeter = 0
    for r in range(len(land_map)):
        for c in range(len(land_map[0])):
            if land_map[r][c] == 1:
                if r != 0:
                    if land_map[r - 1][c] == 0:
                        perimeter += 1
                else:
                    perimeter += 1

                if r != len(land_map) - 1:
                    if land_map[r + 1][c] == 0:
                        perimeter += 1
                else:
                    perimeter += 1

                if c != 0:
                    if land_map[r][c - 1] == 0:
                        perimeter += 1
                else:
                    perimeter += 1

                if c != len(land_map[0]) - 1:
                    if land_map[r][c + 1] == 0:
                        perimeter += 1
                else:
                    perimeter += 1
    return perimeter


land_map = [[0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0]]

print(total_fence(land_map))
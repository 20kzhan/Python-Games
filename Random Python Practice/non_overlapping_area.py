def transform_rectangle(p1, p2):
    xlist = [p1[0], p2[0]]
    ylist = [p1[1], p2[1]]

    res1 = min(xlist), min(ylist)
    res2 = max(xlist), max(ylist)

    return res1, res2

def non_overlapping_area(r1, r2):
    # ???
    r1 = transform_rectangle(r1[0], r1[1])
    print(r1)
    r2 = transform_rectangle(r2[0], r2[1])
    print(r2)

    if r1[0][0] < r2[0][0]:
        small_x = r2[0][0]
    else:
        small_x = r1[0][0]
    if r1[1][0] < r2[1][0]:
        big_x = r1[1][0]
    else:
        big_x = r2[1][0]
    print(big_x-small_x)

    if r1[0][1] < r2[0][1]:
        small_y = r2[0][1]
    else:
        small_y = r1[0][1]
    if r1[1][1] < r2[1][1]:
        big_y = r1[1][1]
    else:
        big_y = r2[1][1]
    print(big_y-small_y)

    r1_area = (r1[1][0] - r1[0][0]) * (r1[1][1] - r1[0][1])
    print(r1_area)
    r2_area = (r2[1][0] - r2[0][0]) * (r2[1][1] - r2[0][1])
    print(r2_area)

    return r1_area + r2_area - ((big_y-small_y) * (big_x-small_x)) * 2

print(non_overlapping_area(((-1, -1), (3, -4)), ((-3, -2), (1, 3))))
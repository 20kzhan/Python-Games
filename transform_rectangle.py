def transform_rectangle(p1, p2):
    xlist = [p1[0], p2[0]]
    ylist = [p1[1], p2[1]]

    res1 = min(xlist), min(ylist)
    res2 = max(xlist), max(ylist)

    return res1, res2

print(transform_rectangle((1, -2), (-3, 3)))

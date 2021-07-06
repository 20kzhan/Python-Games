def on_same_line(points):
    point1 = points[0]
    angles = []
    # for p in points[1:]:
    #     angles.append((p[0] - point1[0]) / (p[1] - point1[1]))
    for p in points[1:]:
        try:
            angles.append((p[0] - point1[0]) / (p[1] - point1[1]))
        except ZeroDivisionError:
            pass

    if len(list(set(angles))) < 1:
        return False
    else:
        return True


print(on_same_line([[-3, 0], [0, 0], [5, 0], [100, 0]]))
# print(on_same_line([[0, -1], [0, 13], [0, -55]]))
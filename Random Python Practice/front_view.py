def front_view(heights):
    view_list = []
    tallest = max(heights)
    if heights.index(tallest) == 0:
        return [0]
    for i in range(len(heights)):
        if heights[i] > heights[i - 1] and i != 0:
            view_list.append(i)
        if i == 0:
            view_list.append(i)

    return view_list


print(front_view([1, 2, 3, 4]))

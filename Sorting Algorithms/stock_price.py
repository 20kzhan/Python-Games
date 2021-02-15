def stock_price(alist):
    smallestprice = 0
    m = len(alist)
    sortedlist = alist.copy()
    alist_copy = sortedlist.copy()
    alist_copy2 = alist_copy.copy()
    sell_value = 0

    for u in range(m):
        for v in range(0, m - u - 1):
            if sortedlist[v] > sortedlist[v + 1]:
                sortedlist[v], sortedlist[v + 1] = sortedlist[v + 1], sortedlist[v]
    while True:
        if alist_copy.index(sortedlist[0]) != len(alist_copy)-1:
            smallestprice = sortedlist[0]
            break
        else:
            alist_copy.remove(alist_copy.index(sortedlist[0]))

    for u in range(m):
        for v in range(alist.index(smallestprice), m - u - 1):
            if alist_copy2[v] > alist_copy2[v + 1]:
                alist_copy2[v], alist_copy2[v + 1] = alist_copy2[v + 1], alist_copy2[v]

    sell_value = alist_copy2[-1]
    return (alist.index(smallestprice), alist.index(sell_value), sell_value-smallestprice)

print(stock_price([9, 8, 7, 1, 5, 3, 6, 4]))
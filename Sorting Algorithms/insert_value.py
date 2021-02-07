def bubble_sort(arr):
    m = len(arr)

    for u in range(m):
        for v in range(0, m-u-1):
            if arr[v] > arr[v+1]:
                arr[v], arr[v + 1] = arr[v + 1], arr[v]

def insert_value(alist, value):
    alist.append(value)
    bubble_sort(alist)
    return alist
alist = [1, 2, 3, 4, 5, 9, 8]
print(insert_value(alist, 7))
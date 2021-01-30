from time import sleep
def bubble_sort(arr):
    m = len(arr)

    for u in range(m):
        for v in range(0, m-u-1):
            if arr[v] > arr[v+1]:
                arr[v], arr[v + 1] = arr[v + 1], arr[v]

array = [1, 9, -1, 4, 5, 6, 0]
bubble_sort(array)
print(array)

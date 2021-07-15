def three_equal_parts(alist):
    first_index = 0
    second_index = 0
    if sum(alist) % 3 != 0:
        print("List not compatible!")
        return False

    for i in range(1, len(alist)-1):
        if sum(alist[:i]) == int(sum(alist) / 3):
            print(sum(alist[:i]))
            first_index = i
            break

    if first_index == 0:
        print("First Index Failed")
        return False

    for x in range(first_index, len(alist)):
        if sum(alist[first_index:x]) == int(sum(alist) / 3):
            second_index = x
            break

    if second_index == 0:
        print("Second Index Failed")
        return False

    return True


print(three_equal_parts([1, 1, 1]))
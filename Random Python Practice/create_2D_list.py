def create_2D_list(row, col):
    ans = []
    temp_ans = []
    offset = 0
    for i in range(0, row):
        for x in range(offset, (col*2)+offset, 2):
            temp_ans.append(x)
            print(x)
        offset += 4
        ans.append(temp_ans)
        temp_ans = []
    return ans

print(create_2D_list(6, 8))
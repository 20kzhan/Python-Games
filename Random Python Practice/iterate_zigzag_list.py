def printDiagnol(lst):
    temp_list = []
    for each_row in lst:
        temp_list.append(each_row[0])
    print(temp_list)
    temp_list = []
    for i in range(len(lst) - 1, -1, -1):
        temp_list.append(lst[i][len(lst) - i - 1])
    print(temp_list)

    temp_list = []
    for each_row in lst:
        temp_list.append(each_row[-1])
    print(temp_list)
    temp_list = []
    for i in range(len(lst) - 1, -1, -1):
        temp_list.append(lst[i][i])
    print(temp_list)

def iterate_up_down(alist):
    row_count = 0
    row_increase = 1
    temp_list = []
    for every_other_col in range(0, len(alist[0])):
        while True:
            temp_list.append(alist[row_count][every_other_col])
            if row_count == len(alist)-1 and row_increase == 1 or row_count == 0 and row_increase == -1:
                row_increase *= -1
                break
            row_count += row_increase
    print(temp_list)

def iterate_up_down2(alist):
    row_count = 0
    row_increase = 1
    temp_list = []
    for every_other_col in range(0, len(alist[0]), 2):
        while True:
            temp_list.append(alist[row_count][every_other_col])
            if row_count == len(alist)-1 and row_increase == 1 or row_count == 0 and row_increase == -1:
                row_increase *= -1
                break
            row_count += row_increase
    print(temp_list)

def iterate_up_down3(blist):
    output = []
    for col_index in range(0, len(blist), 2):
        if col_index % 4 == 0:
            for row_index in range(len(blist)):
                 output.append(blist[row_index][col_index])
        else:
            for rowindex in range(len(blist) - 1, -1, -1):
             output.append(blist[rowindex][col_index])
    return output

def create_2D_list(num_rows, num_cols):
    return [[num_cols*row + col for col in range(num_cols)] for row in
            range(num_rows)]


matrix = create_2D_list(10, 10)

printDiagnol(matrix)
# iterate_up_down(matrix)
# iterate_up_down2(matrix)
# print(iterate_up_down3(matrix))
alist = [[2, 0, 1, 13],
         [0, 9, 9, 1],
         [1, 0, 1, 1],
         [0, 0, 0, 1]]

sum_of_rows = []
sum_of_col = []
column0sum = []

sum = 0

for each_row in alist:
    for i in range(len(alist[0])):
        sum += each_row[i]
    sum_of_rows.append(sum)
    sum = 0

# for row in range(len(alist)):m
#     column0sum.append(alist[row][0])

column_sum = [0] * len(alist[0]) # [0,0,/ 0,0/]

# col = 0
# column_sum[col] = 0
# for row in range(len(alist)):
#     column_sum[col] += alist[row][col]
#
# col = 1
# column_sum[col] = 0
# for row in range(len(alist)):
#     column_sum[col] += alist[row][col]
#
# col = 2
# column_sum[col] = 0
# for row in range(len(alist)):
#     column_sum[col] += alist[row][col]
#
# col = 3
# column_sum[col] = 0
# for row in range(len(alist)):
#     column_sum[col] += alist[row][col]

column_sum = []
for col in range(len(alist[0])):
    # problem column_sum[col] = 0
    col_sum = 0
    for row in range(len(alist)):
        col_sum += alist[row][col]
        # column_sum[col] += alist[row][col]
    # col_sum is ready!
    column_sum.append(col_sum)

cross0sum = alist[0][0] + alist[1][1] + alist[2][2] + alist[3][3]
cross0sum = 0
for i in range(len(alist)):
    cross0sum += alist[i][i]

cross1sum = alist[3][0] + alist[2][1] + alist[1][2] + alist[0][3]

i = 0
#cross1sum += alist[3][i]
cross1sum += alist[3 - i][i]


i = 1
#cross1sum += alist[2][i]
cross1sum += alist[3 - i][i]

i = 2
#cross1sum += alist[1][i]
cross1sum += alist[3 - i][i]


i = 3
#cross1sum += alist[0][i]
cross1sum += alist[3 - i][i]






cross1sum = 0
for i in range(len(alist)):
    cross1sum += alist[(len(alist[0])-1) - i][i]

# column0sum = 0
# column1sum = 0
# column2sum = 0
# column3sum = 0
# for row in range(len(alist)):
#     column_sum[0] += alist[row][0]
#     column_sum[1] += alist[row][1]
#     column_sum[2] += alist[row][2]
#     column_sum[3] += alist[row][3]

print(sum_of_rows)
print(column_sum)
print(cross0sum)
print(cross1sum)
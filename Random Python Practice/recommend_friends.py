def recommend_friends(friends_list):
    output = []
    for i in range(len(friends_list)):
        for j in range(len(friends_list[i])):
            output.append(friends_list[i][j])

    return output


print(recommend_friends([[1, 2, 3, 4, 5],
                         [6, 7, 8, 9, 10]]))

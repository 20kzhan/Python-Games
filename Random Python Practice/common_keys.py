def common_keys(d1, d2):
    set1 = set(d1.keys())
    set2 = set(d2.keys())
    com_keys = set1.intersection(set2)
    return com_keys

def common_values(d1, d2):
    set1 = set(d1.keys())
    set2 = set(d2.keys())
    com_keys = set1.intersection(set2)
    com_values = []

    for key in com_keys:
        val1_set = set(d1[key])
        val2_set = set(d2[key])
        com_values += val1_set.intersection(val2_set)

    return com_values

dict1 = {3: [2], 4: [2, 3, 4], 5: [2, 3, 4]}
dict2 = {3: [3], 9: [2, 5, 4], 5: [3, 5], 6: [4, 5, 6]}

print(common_keys(dict1, dict2))
print(common_values(dict1, dict2))

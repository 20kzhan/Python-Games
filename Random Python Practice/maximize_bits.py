def maxSum(string):
    maximum_sum = 0

    # To store the total ones

    # Count the total numbers of ones
    # in str
    total_ones = 0
    for i in string:
        if i == '1':
            total_ones += 1

    # To store the count of zeros and
    # ones while traversing string
    zero = 0
    ones = 0

    # Interate the given and
    # update the maximum sum
    i = 0
    while i < len(string):

        if string[i] == '0':
            zero += 1
        else:
            ones += 1

        # Update the maximum Sum
        maximum_sum = max(maximum_sum, zero + (total_ones - ones))
        i += 1

    return maximum_sum

if __name__ == '__main__':
    string = "011101"

    # Function call
    print(maxSum(string))
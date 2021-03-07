def max_num_ppl(weights, max_weight):
    len_weight = len(weights)
    num_ppl = 0
    while True:
        for x in range(len(weights)):
            low = weights[0]  # need to start with some value
            for i in weights:
                if i < low:
                    low = i
            num_ppl += low
            if num_ppl > max_weight:
                num_ppl -= low
                break
            print(low)
            weights.remove(low)
        return len_weight-len(weights)

print(max_num_ppl([161, 192, 178, 30, 71, 45], 400))
def longest_chain(string, letter_group):
    chain = 0
    all_chains = []
    for c in string:
        if c in letter_group:
            chain += 1
        else:
            if chain > 0:
                all_chains.append(chain)
            chain = 0

    return max(all_chains)


print(longest_chain("abbacdefghjkabcclzvx", "abc"))

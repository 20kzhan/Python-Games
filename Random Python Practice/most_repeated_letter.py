def most_repeated_letters(word_1):
    letters_count = {}
    for ch in word_1:
        if ch not in letters_count:
            letters_count[ch] = 1
        else:
            letters_count[ch] += 1

    return max(letters_count, key=letters_count.get)


print(most_repeated_letters("hello world"))
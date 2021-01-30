def count_letters(string):
    all_freq = {}
    string = string.lower()

    for char in string:
        if char.isalpha():
            if char in all_freq:
                all_freq[char] += 1
            else:
                all_freq[char] = 1
    return all_freq


print(count_letters('hello world'))
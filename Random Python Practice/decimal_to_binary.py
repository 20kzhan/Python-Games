def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num // 2)
    return num % 2

if __name__ == '__main__':
    dec_val = 24
    print(decimal_to_binary(dec_val))

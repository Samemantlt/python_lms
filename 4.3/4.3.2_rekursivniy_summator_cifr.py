def recursive_digit_sum(num):
    if num // 10 == 0:
        return num
    else:
        return num % 10 + recursive_digit_sum(num // 10)

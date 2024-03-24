def find_pair(*numbers, div=6):
    result = None
    result_sum = -1

    for right_index in range(len(numbers) - 1, 0, -1):
        right = numbers[right_index]

        for left_index in range(0, right_index):
            left = numbers[left_index]

            if (left + right) % div != 0:
                continue

            if left + right > result_sum:
                result = (left, right)
                result_sum = left + right
    
    return result

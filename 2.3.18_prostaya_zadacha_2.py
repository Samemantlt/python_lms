def prostie(number: int) -> list:
    result = []
    for i in range(2, number):
        while number % i == 0:
            result.append(i)
            number //= i

    return result


def main():
    number = int(input())
    arr = prostie(number)

    for i in range(len(arr) - 1):
        print(arr[i], end=" * ")
    
    print(arr[-1])


if __name__ == '__main__':
    main()

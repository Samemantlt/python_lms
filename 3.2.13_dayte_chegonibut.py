def main():
    possible_values = set()

    for _ in range(int(input())):
        value = input()
        possible_values.add(value)
    
    used_values = set()

    for _ in range(int(input())):
        for _ in range(int(input())):
            used_values.add(input())
    
    result = possible_values - used_values

    if len(result) == 0:
        print('Готовить нечего')
        return
    
    for value in sorted(result):
        print(value)


if __name__ == '__main__':
    main()

def main():
    count_map = dict()

    for _ in range(int(input())):
        x, y = map(int, input().split(' '))
        key = (x // 10, y // 10)
        if key in count_map:
            count_map[key] += 1
        else:
            count_map[key] = 1
    
    print(max(count_map.values()))


if __name__ == '__main__':
    main()

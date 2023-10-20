def main():
    all_toys = []

    for _ in range(int(input())):
        line = input()
        words = line[line.find(':') + 2:].split(', ')
        toys = set(words)

        for toy in toys:
            all_toys.append(toy)
    
    for toy in sorted(set(all_toys)):
        if all_toys.count(toy) == 1:
            print(toy)


if __name__ == '__main__':
    main()

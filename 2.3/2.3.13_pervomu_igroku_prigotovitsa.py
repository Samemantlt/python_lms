def main():
    count = int(input())

    names = []
    for _ in range(count):
        name = input()
        names.append(name)
    
    print(min(names))


if __name__ == '__main__':
    main()

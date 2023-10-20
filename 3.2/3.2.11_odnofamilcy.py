def main():
    names = []

    for _ in range(int(input())):
        names.append(input())
    
    result = 0
    for name in set(names):
        if names.count(name) > 1:
            result += names.count(name)
    
    print(result)


if __name__ == '__main__':
    main()

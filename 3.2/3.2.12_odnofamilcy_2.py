def main():
    names = []

    for _ in range(int(input())):
        names.append(input())
    
    found = False
    for name in sorted(set(names)):
        n = names.count(name)
        if n > 1:
            print(f'{name} - {n}')
            found = True
    
    if not found:
        print('Однофамильцев нет')


if __name__ == '__main__':
    main()

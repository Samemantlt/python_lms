def main():
    n_mannaya = int(input())
    n_ovsyanaya = int(input())

    mannaya = set()
    ovsyanaya = set()

    for _ in range(n_mannaya):
        name = input()
        mannaya.add(name)

    for _ in range(n_ovsyanaya):
        name = input()
        ovsyanaya.add(name)

    love_all = ovsyanaya.intersection(mannaya)
    
    if len(love_all) == 0:
        print('Таких нет')
    else:
        print(len(love_all))


if __name__ == '__main__':
    main()

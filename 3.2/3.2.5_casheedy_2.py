def main():
    n_mannaya = int(input())
    n_ovsyanaya = int(input())

    people = set()
    lovers = 0

    for _ in range(n_mannaya + n_ovsyanaya):
        person = input()

        if person not in people:
            lovers += 1
        else:
            lovers -= 1
        
        people.add(person)

    if lovers == 0:
        print('Таких нет')
    else:
        print(lovers)


if __name__ == '__main__':
    main()

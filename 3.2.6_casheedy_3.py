def main():
    n_mannaya = int(input())
    n_ovsyanaya = int(input())

    people = set()
    lovers = set()

    for _ in range(n_mannaya + n_ovsyanaya):
        person = input()

        lovers.add(person)
        if person in people:
            lovers.remove(person)
        
        people.add(person)

    if len(lovers) == 0:
        print('Таких нет')
    else:
        for lover in sorted(lovers):
            print(lover)


if __name__ == '__main__':
    main()

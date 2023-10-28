def main():
    people1 = input().split(', ')
    people2 = input().split(', ')

    for i in range(min(len(people1), len(people2))):
        print(f'{people1[i]} - {people2[i]}')


if __name__ == '__main__':
    main()

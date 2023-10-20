def main():
    possible_starts = 'абв'
    
    for _ in range(int(input())):
        word = input().lower()
        if word[0] not in possible_starts:
            print('NO')
            break
    else:
        print('YES')


if __name__ == '__main__':
    main()

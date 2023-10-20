def main():
    a = input()
    print('YES' if ''.join(reversed(a)) == a else 'NO')


if __name__ == '__main__':
    main()

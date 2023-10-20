def main():
    num = input()
    result = ''.join(filter(lambda a: a in '13579', list(num)))

    print(result)


if __name__ == '__main__':
    main()

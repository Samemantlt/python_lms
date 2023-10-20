def main():
    count = 0

    while (text := input()) != 'Приехали!':
        count += text.count('зайка')
    
    print(count)


if __name__ == '__main__':
    main()
